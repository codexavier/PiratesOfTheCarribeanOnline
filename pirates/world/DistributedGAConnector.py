# File: D (Python 2.4)

from pandac.PandaModules import *
from direct.distributed import DistributedNode
from direct.distributed import DistributedObject
from pirates.piratesbase import PiratesGlobals
from pirates.world import DistributedGameArea
from pirates.world import DistributedIsland
from pirates.effects import EnvironmentEffects
from pirates.tutorial import CrewTutorial
from direct.showbase.PythonUtil import report
from pirates.piratesbase import PLocalizer
from pirates.world import ZoneLOD
from pirates.map.MinimapObject import MinimapObject

class DistributedGAConnector(DistributedNode.DistributedNode):
    notify = directNotify.newCategory('DistributedGAConnector')

    def __init__(self, cr, name = 'DistributedGAConnector'):
        DistributedNode.DistributedNode.__init__(self, cr)
        NodePath.__init__(self, name)
        self.fakeZoneId = PiratesGlobals.FakeZoneId
        self.GridLOD = { }
        self.uniqueId = ''
        self.interior = None
        self.visNodes = { }
        self.geom = None
        self.visContext = None
        self.envEffects = None
        self.connectorNodes = []
        self.connectorNodePosHpr = []
        self.areaId = [
            None,
            None]
        self.areaUid = [
            None,
            None]
        self.areaWorldZone = [
            None,
            None]
        self.areaNode = [
            None,
            None]
        self.areaLookupDict = [
            base.cr.doId2do,
            base.cr.doId2do]
        self._DistributedGAConnector__connectorLoaded = 0
        self._DistributedGAConnector__loadedArea = None
        self.areaIndexLoading = None
        self.pendingAreaLoad = False
        self.pendingAreaUnload = False
        self.pendingArea = None
        self.minimapObj = None


    def announceGenerate(self):
        self.notify.debug('%s announceGenerate' % self.doId)
        DistributedNode.DistributedNode.announceGenerate(self)
        self.setupConnectorNodes()
        self.setupCollisions()
        self.setupEntranceNodes()
        self.startCustomEffects()


    def setLocation(self, parentId, zoneId, teleport = 0):
        DistributedObject.DistributedObject.setLocation(self, parentId, zoneId)


    def isGridParent(self):
        return 0


    def setUniqueId(self, uid):
        if self.uniqueId != '':
            self.cr.uidMgr.removeUid(self.uniqueId)

        self.uniqueId = uid
        self.cr.uidMgr.addUid(self.uniqueId, self.getDoId())


    def getUniqueId(self):
        return self.uniqueId


    def reparentConnector(self):
        side0 = self.getAreaObject(0)
        side1 = self.getAreaObject(1)
        if side0 and side1:
            if side0.isStashed() and not side1.isStashed():
                self.reparentConnectorToArea(side1)
            elif side1.isStashed() and not side0.isStashed():
                self.reparentConnectorToArea(side0)

            return None

        if side0:
            self.notify.debug('reparentConnector to side 0')
            self.reparentConnectorToArea(side0)
        elif side1:
            self.notify.debug('reparentConnector to side 1')
            self.reparentConnectorToArea(side1)



    def delete(self):
        self.destroyMinimapObject()
        for doId in self.areaId:
            area = base.cr.doId2do.get(doId)
            if area:
                uid = area.uniqueId
                area.builder.removeLargeObj(self.visNodes[uid], self.uniqueId)
                continue

        if self.pendingArea:
            self.cr.relatedObjectMgr.abortRequest(self.pendingArea)
            self.pendingArea = None

        for node in self.visNodes.values():
            node.detachNode()

        self.visNodes = { }
        self.notify.debug('delete %s' % self.doId)
        DistributedNode.DistributedNode.delete(self)
        self.stopCustomEffects()
        if self.fakeZoneId != None:
            for node in self.GridLOD.values():
                node.cleanup()

            del self.GridLOD

        self.removeNode()
        self._DistributedGAConnector__loadedArea = None
        self.visContext = None
        self.ignoreAll()
        del self.interior
        del self.areaLookupDict
        del self.fakeZoneId


    def setModelPath(self, modelPath):
        self.notify.debug('setModelPath %s' % modelPath)
        self.modelPath = modelPath
        self.loadModel()


    def loadWholeModel(self):
        modelBaseName = self.modelPath
        self.geom = loader.loadModel(modelBaseName)


    def loadModelParts(self):
        modelBaseName = self.modelPath
        terrainModel = loader.loadModel(modelBaseName + '_terrain', okMissing = True)
        if terrainModel:
            self.geom = terrainModel.getChild(0)
            self.geom.setName(terrainModel.getName())
        else:
            self.geom = loader.loadModel(modelBaseName)
            return None
        pierModel = loader.loadModel(modelBaseName + '_pier', okMissing = True)
        if pierModel:
            pierModel.getChild(0).reparentTo(self.geom)

        vegeWallModel = loader.loadModel(modelBaseName + '_nat_wall', okMissing = True)
        if vegeWallModel:
            vegeWallModel.getChild(0).reparentTo(self.geom)

        vegModel = loader.loadModel(modelBaseName + '_veg', okMissing = True)
        if vegModel:
            vegModel.getChild(0).reparentTo(self.geom)

        rockModel = loader.loadModel(modelBaseName + '_rocks', okMissing = True)
        if rockModel:
            rockModel.getChild(0).reparentTo(self.geom)

        logModel = loader.loadModel(modelBaseName + '_logs', okMissing = True)
        if logModel:
            logModel.getChild(0).reparentTo(self.geom)

        miscModel = loader.loadModel(modelBaseName + '_misc', okMissing = True)
        if miscModel:
            miscModel.getChild(0).reparentTo(self.geom)



    def loadModel(self):
        if not self.geom:
            self.loadWholeModel()
            self.geom.flattenStrong()
            self.geom.reparentTo(self)



    def setLinks(self, isExterior, exteriorUid, links):
        self.notify.debug('%s(%s) setLinks %s %s' % (self, self.doId, isExterior, links))
        self.isExterior = isExterior
        self.exteriorUid = exteriorUid
        for link in links:
            (connectorNode, areaId, areaUid, areaParent, areaZone, areaNode, areaWorldId, areaWorldZone) = link
            if not self.visNodes.get(areaUid):
                self.visNodes[areaUid] = NodePath('vis-%s-%s' % (self.uniqueId, areaUid))

            aInd = self.connectorNodes.index(connectorNode)
            self.areaId[aInd] = areaId
            self.areaUid[aInd] = areaUid
            self.areaNode[aInd] = areaNode
            self.areaWorldZone[aInd] = [
                areaWorldId,
                areaWorldZone]

        self.reparentConnector()
        self._DistributedGAConnector__connectorLoaded = 1
        messenger.send('tunnelSetLinks', [
            self])


    def isConnectorLoaded(self):
        return self._DistributedGAConnector__connectorLoaded


    def getAreaIndex(self, area):
        if area.getUniqueId() == self.areaUid[0]:
            return 0
        elif area.getUniqueId() == self.areaUid[1]:
            return 1



    def getAreaIndexFromDoId(self, areaDoId):
        area = self.cr.doId2do.get(areaDoId)
        if area:
            return self.getAreaIndex(area)



    def getAreaObject(self, index):
        areaUid = self.areaUid[index]
        areaLookupDict = self.areaLookupDict[index]
        area = areaLookupDict.get(base.cr.uidMgr.getDoId(areaUid))
        return area


    def setupConnectorNodes(self):
        for locator in self.connectorNodes:
            locatorNode = self.find('**/' + locator)
            pos = self.getPos(locatorNode)
            hpr = self.getHpr(locatorNode)
            self.connectorNodePosHpr.append([
                pos,
                hpr])



    def getConnectorNodePosHpr(self, index):
        if index < len(self.connectorNodePosHpr):
            return self.connectorNodePosHpr[index]

        return (Point3(0), Vec3(0))


    def setupEntranceNodes(self):
        entranceNodes = self.findAllMatches('**/entrance_locator_*')
        eNodeMap = [](_[1]([ node.getName() for node in entranceNodes ], entranceNodes))
        eNodeMapKeys = eNodeMap.keys()
        eNodeMapKeys.sort()
        self.entranceNodes = [ eNodeMap[key] for key in eNodeMapKeys ]


    def getEntranceNode(self, index):
        if index < len(self.entranceNodes):
            return self.entranceNodes[index]



    def setupCollisions(self):
        pass


    def setLoadedArea(self, area):
        self._DistributedGAConnector__loadedArea = area

    setLoadedArea = report(types = [
        'frameCount'], dConfigParam = 'connector')(setLoadedArea)

    def getLoadedArea(self):
        return self._DistributedGAConnector__loadedArea

    getLoadedArea = report(types = [
        'frameCount'], dConfigParam = 'connector')(getLoadedArea)

    def getLoadedAreaIndex(self):
        return self.getAreaIndex(self._DistributedGAConnector__loadedArea)

    getLoadedAreaIndex = report(types = [
        'frameCount'], dConfigParam = 'connector')(getLoadedAreaIndex)

    def unloadLoadedArea(self, entry = None):
        if self.getLoadedArea():
            self.unloadArea(self.getLoadedAreaIndex())
            self.setLoadedArea(None)


    unloadLoadedArea = report(types = [
        'frameCount',
        'args'], dConfigParam = 'connector')(unloadLoadedArea)

    def unloadArea(self, areaIndex, entry = None):
        self.notify.debug('%s unloadArea %s' % (self.doId, areaIndex))
        area = self.getAreaObject(areaIndex)
        if area:
            self.wrtReparentTo(render)
            self.pendingAreaUnload = area.getDoId()
            world = area.getParentObj()
            (worldLocationId, worldLocationZone) = world.getLocation()
            world.removeWorldInterest(area)
            worldEvent = 'unloadWorld-' + str(worldLocationId)
            self.acceptOnce(worldEvent, self.unloadWorldFinished, extraArgs = [
                self.pendingAreaUnload])
            localAvatar.clearInterestNamed(worldEvent, [
                'instanceInterest'])
        else:
            self.notify.warning('no area to be removed for connector entry')

    unloadArea = report(types = [
        'frameCount',
        'args'], dConfigParam = 'connector')(unloadArea)

    def loadArea(self, areaIndex, showLoadingScreen = False):
        if showLoadingScreen:
            base.cr.loadingScreen.show(waitForLocation = True)

        locationUid = self.areaUid[areaIndex]
        base.cr.loadingScreen.showTarget(locationUid)
        base.cr.loadingScreen.showHint(locationUid)
        self.notify.debug('%s loadArea %s' % (self.doId, areaIndex))
        (worldId, worldZoneId) = self.areaWorldZone[areaIndex]
        area = self.getLoadedArea()
        if area and self.getAreaIndex(area) == areaIndex:
            self.notify.debug('%s already loaded game area %s' % (self.doId, areaIndex))
            return None
        else:
            self.notify.debug('%s Loading game area %s' % (self.doId, areaIndex))
            areaDoId = self.areaId[areaIndex]
            area = base.cr.doId2do.get(areaDoId)
            if area and not (self.pendingAreaUnload):
                self.loadAreaFinished(area)
            else:
                areaUid = self.areaUid[areaIndex]
                aDoId = base.cr.uidMgr.getDoId(areaUid)
                if aDoId:
                    area = base.cr.doId2do.get(aDoId)

                if not area and not (self.pendingAreaLoad):
                    self.areaIndexLoading = areaIndex
                    self.requestPrivateArea(areaDoId)
                elif area:
                    if aDoId != self.pendingAreaUnload:
                        self.notify.debug('%s already have interest %s %s' % (self.doId, area.getLocation()[0], area.getLocation()[1]))
                        self.loadAreaFinished(area)
                    else:
                        self.areaIndexLoading = areaIndex
                        self.requestPrivateArea(areaDoId)


    loadArea = report(types = [
        'frameCount',
        'args'], dConfigParam = 'connector')(loadArea)

    def requestPrivateArea(self, areaDoId):
        self.pendingAreaLoad = True
        self.sendUpdate('requestPrivateArea', [
            areaDoId])

    requestPrivateArea = report(types = [
        'frameCount',
        'args'], dConfigParam = 'connector')(requestPrivateArea)

    def setPrivateArea(self, worldId, worldZoneId, areaDoId, autoFadeIn = True):
        areaIndex = self.areaIndexLoading
        self.notify.debug('setPrivateArea: worldId %s worldZoneId %s' % (worldId, worldZoneId))
        if worldId == 0 and worldZoneId == 0:
            (worldId, worldZoneId) = self.areaWorldZone[areaIndex]

        self.setArea(worldId, worldZoneId, areaDoId, autoFadeIn)

    setPrivateArea = report(types = [
        'frameCount',
        'args'], dConfigParam = 'connector')(setPrivateArea)

    def setArea(self, worldLocationId, worldLocationZone, areaDoId, autoFadeIn = True):
        localAvatar.setInterest(worldLocationId, worldLocationZone, [
            'instanceInterest'])

        def areaFinishedCallback(area):
            self.pendingArea = None
            self.loadAreaFinished(area, autoFadeIn)

        areaFinishedCallback = report(types = [
            'frameCount'], dConfigParam = 'connector')(areaFinishedCallback)
        if self.pendingArea:
            self.cr.relatedObjectMgr.abortRequest(self.pendingArea)

        self.pendingArea = self.cr.relatedObjectMgr.requestObjects([
            areaDoId], eachCallback = areaFinishedCallback)

    setArea = report(types = [
        'frameCount',
        'args'], dConfigParam = 'connector')(setArea)

    def unloadWorldFinished(self, areaDoId):
        self.pendingAreaUnload = None

    unloadWorldFinished = report(types = [
        'frameCount',
        'args'], dConfigParam = 'connector')(unloadWorldFinished)

    def loadAreaFinished(self, area, autoFadeIn = True):
        self.notify.debug('loadAreaFinished %s' % area.doId)
        self.pendingAreaLoad = False
        if isinstance(area, ZoneLOD.ZoneLOD):
            area.setZoneLevel(0)

        self.reparentConnector()
        localAvatar.wrtReparentTo(area)
        localAvatar.setScale(1)
        world = area.getParentObj()
        world.addWorldInterest(area)
        messenger.send('loadAreaFinished')
        area.getParentObj().addWorldInterest(area)
        area.handleEnterGameArea(None)

    loadAreaFinished = report(types = [
        'frameCount',
        'args'], dConfigParam = 'connector')(loadAreaFinished)

    def isExteriorIndex(self, index):
        if index != None:
            areaLocatorName = self.areaNode[index]
            if self.isExterior and 'exterior' in areaLocatorName:
                return True


        return False


    def reparentConnectorToArea(self, area):
        self.notify.debug('%s reparentConnectorToArea %s' % (self.doId, area))
        areaIndex = self.getAreaIndex(area)
        entranceNode = self.areaNode[areaIndex]
        entryLocator = area.find('**/' + entranceNode + '*')
        if entryLocator.isEmpty():
            return None

        entryLocator.setScale(1)
        entryLocator.setP(0)
        entryLocator.setR(0)
        rootNode = self.visNodes[area.uniqueId]
        rootNode.reparentTo(area)
        rootNode.setTransform(entryLocator.getTransform(area))
        lightAttrib = entryLocator.getAttrib(LightAttrib.getClassType())
        if lightAttrib:
            rootNode.setAttrib(lightAttrib, 1)

        area.builder.addLargeObj(rootNode, self.uniqueId)
        self.reparentTo(entryLocator)
        (pos, hpr) = self.connectorNodePosHpr[areaIndex]
        self.setPos(pos)
        self.setHpr(hpr[0], 0, 0)
        self.wrtReparentTo(rootNode)
        self.setLoadedArea(area)
        if area.showTunnelOnMinimap(self.uniqueId):
            obj = self.getMinimapObject(entryLocator)
            area.addMinimapObject(obj)
            obj.updateWorldNode(entryLocator)


    reparentConnectorToArea = report(types = [
        'frameCount',
        'args'], dConfigParam = 'connector')(reparentConnectorToArea)

    def startCustomEffects(self):
        if self.envEffects:
            self.envEffects.delete()
            self.envEffects = None

        self.envEffects = EnvironmentEffects.EnvironmentEffects(self.geom, self.modelPath)


    def stopCustomEffects(self):
        if self.envEffects:
            self.envEffects.delete()
            self.envEffects = None



    def handleChildArrive(self, childObj, zoneId):
        DistributedNode.DistributedNode.handleChildArrive(self, childObj, zoneId)
        if childObj.isLocal():
            childObj.refreshActiveQuestStep(forceClear = True)
            childObj.lastConnectorId = self.doId



    def turnOn(self):
        pass


    def turnOff(self):
        pass


    def getMinimapObject(self, worldNode):
        if not (self.minimapObj) and not self.isDisabled():
            self.minimapObj = MinimapTunnel(worldNode)

        return self.minimapObj


    def destroyMinimapObject(self):
        if self.minimapObj:
            self.minimapObj.removeFromMap()
            self.minimapObj = None




class MinimapTunnel(MinimapObject):
    ICON = None
    OUTOFRANGE_ICON = None

    def __init__(self, worldNode):
        if not MinimapTunnel.ICON:
            compass = loader.loadModel('models/gui/compass_main')
            MinimapTunnel.ICON = compass.find('**/icon_rectangle_hollow').getChild(0).copyTo(NodePath('tunnel'))
            MinimapTunnel.ICON.clearTransform()
            MinimapTunnel.ICON.setHpr(90, 90, 0)
            MinimapTunnel.ICON.setScale(300)
            MinimapTunnel.ICON.flattenStrong()
            MinimapTunnel.OUTOFRANGE_ICON = compass.find('**/icon_rectangle_hollow').getChild(0).copyTo(NodePath('tunnel-outofrange'))
            MinimapTunnel.OUTOFRANGE_ICON.clearTransform()
            MinimapTunnel.OUTOFRANGE_ICON.setPosHpr(1, 0, 0, 0, 0, 90)
            MinimapTunnel.OUTOFRANGE_ICON.flattenStrong()

        MinimapObject.__init__(self, 'tunnel', worldNode, self.ICON)
        self.outOfRangeGeom = NodePath('outOfRange')
        icon = MinimapTunnel.OUTOFRANGE_ICON.copyTo(self.outOfRangeGeom)


    def updateWorldNode(self, worldNode):
        self.worldNode = worldNode
        if self.map:
            self.map.addObject(self)



    def _updateOnMap(self, map):
        localAvatar.guiMgr.radarGui.updateOutOfRange(map, self, self.outOfRangeGeom)


    def _removedFromMap(self, map):
        self.outOfRangeGeom.detachNode()


