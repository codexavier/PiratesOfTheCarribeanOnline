# File: D (Python 2.4)

from direct.distributed.DistributedCartesianGrid import DistributedCartesianGrid
from direct.showbase.PythonUtil import report
from pirates.world import WorldGlobals
from pirates.seapatch.SeaPatch import SeaPatch
from pirates.seapatch.Reflection import Reflection
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import PLocalizer
from pandac.PandaModules import *
from OceanGridBase import OceanGridBase
from pirates.map.Minimap import OceanMap
from pirates.map.Mappable import MappableGrid

class DistributedOceanGrid(DistributedCartesianGrid, OceanGridBase, MappableGrid):

    def __init__(self, cr):
        DistributedCartesianGrid.__init__(self, cr)
        OceanGridBase.__init__(self)
        self.islandGrids = { }
        self.minimap = None
        self.water = None


    def generate(self):
        DistributedCartesianGrid.generate(self)
        self.setupWater()
        self.setupShipBarrier()


    def announceGenerate(self):
        DistributedCartesianGrid.announceGenerate(self)
        self.setupMinimap()


    def setLocation(self, parentId, zoneId):
        DistributedCartesianGrid.setLocation(self, parentId, zoneId)
        world = self.cr.doId2do.get(self.parentId)
        if parentId not in (0, self.cr.getGameDoId()):
            pass
        1


    def disable(self):
        DistributedCartesianGrid.disable(self)
        if hasattr(base, 'localAvatar') and base.localAvatar is not None:
            self.removeObjectFromGrid(base.localAvatar)

        self.destroyMinimap()
        self.shipBarrierNP.removeNode()
        self.ignore('enter' + self.cName)


    def delete(self):
        self.cleanupWater()
        DistributedCartesianGrid.delete(self)


    def setupWater(self):
        r = Reflection.getGlobalReflection()
        water = SeaPatch(self, reflection = r)
        water.loadSeaPatchFile('out.spf')
        self.water = water


    def cleanupWater(self):
        self.water.delete()
        self.water = None


    def setupShipBarrier(self):
        worldRadius = WorldGlobals.OCEAN_GRID_SIZE * WorldGlobals.OCEAN_CELL_SIZE / 2.0 - 50
        shipBarrier = CollisionInvSphere(0.0, 0.0, 0.0, worldRadius)
        shipBarrier.setTangible(1)
        self.cName = self.uniqueName('ShipBarrier')
        cSphereNode = CollisionNode(self.cName)
        cSphereNode.setIntoCollideMask(PiratesGlobals.ShipCollideBitmask)
        cSphereNode.addSolid(shipBarrier)
        self.shipBarrierNP = self.attachNewNode(cSphereNode)
        self.accept('enter' + self.cName, self.handleEdgeOfWorld)


    def handleEdgeOfWorld(self, event):
        localAvatar.guiMgr.messageStack.addTextMessage(PLocalizer.EdgeOfWorldWarning)


    def handleChildArrive(self, childObj, zoneId):
        DistributedCartesianGrid.handleChildArrive(self, childObj, zoneId)
        if self.minimap and hasattr(childObj, 'getMinimapObject'):
            if childObj.getMinimapObject():
                self.minimap.addObject(childObj.getMinimapObject())




    def handleChildLeave(self, childObj, zoneId):
        if self.minimap and hasattr(childObj, 'getMinimapObject'):
            if childObj.getMinimapObject():
                self.minimap.removeObject(childObj.getMinimapObject())


        DistributedCartesianGrid.handleChildLeave(self, childObj, zoneId)


    def reparentLocalAvatarToWorld(self, parent = None):
        if parent:
            parent.addObjectToGrid(base.localAvatar)
        elif len(self.islandGrids) > 0:
            islandIds = self.islandGrids.keys()
            island = self.islandGrids[islandIds[0]]
            island.addObjectToGrid(base.localAvatar)
        else:
            self.addObjectToGrid(base.localAvatar)

    oceanAreas = { }

    def addOceanArea(self, pos1, pos2, name, uid):
        ul = Point3(min(pos2.getX(), pos1.getX()), max(pos2.getY(), pos1.getY()), 0)
        lr = Point3(max(pos2.getX(), pos1.getX()), min(pos2.getY(), pos1.getY()), 0)
        if name in self.oceanAreas:
            (pos1, pos2) = self.oceanAreas[name][0:2]
            ul = Point3(min(ul.getX(), pos1.getX()), max(ul.getY(), pos1.getY()), 0)
            lr = Point3(max(lr.getX(), pos2.getX()), min(lr.getY(), pos2.getY()), 0)

        self.oceanAreas[name] = [
            ul,
            lr,
            uid]


    def addOceanAreasToMap(self):
        mapPage = base.localAvatar.guiMgr.mapPage
        areaNames = self.oceanAreas.keys()
        for name in areaNames:
            mapPage.addOceanArea(name, self.oceanAreas[name][2], self.oceanAreas[name][0], self.oceanAreas[name][1])



    def addIslandGrid(self, island):
        self.islandGrids[island.doId] = island
        self.updateLocalAvatarParent(island)


    def removeIslandGrid(self, island):
        islandId = island.doId
        if self.islandGrids.get(islandId):
            del self.islandGrids[islandId]

        self.updateLocalAvatarParent()


    def updateLocalAvatarParent(self, parent = None):
        if base.localAvatar.ship:
            return None

        self.reparentLocalAvatarToWorld(parent)


    def turnOff(self):
        DistributedCartesianGrid.turnOff(self)
        self.stash()
        if self.water:
            self.water.disable()



    def turnOn(self, av):
        DistributedCartesianGrid.turnOn(self, av)
        self.unstash()
        if self.water:
            self.water.enable()



    def stopProcessVisibility(self, *args, **kw):
        DistributedCartesianGrid.stopProcessVisibility(self, *args, **kw)

    stopProcessVisibility = report(types = [
        'deltaStamp',
        'avLocation',
        'args'], dConfigParam = [
        'connector',
        'shipboard'])(stopProcessVisibility)

    def getTeleportDestPosH(self, index = 0):
        return (0, 0, 0, 0)


    def getFootprintNode(self):
        return NodePath('footprint-empty')


    def getShopData(self):
        return ()


    def getGridParameters(self):
        return (self.cellWidth, self.viewingRadius)


    def getZoomLevels(self):
        return ((3000, 5000, 7000, 10000), 1)


    def getMapNode(self):
        mapNode = self.find('minimap')
        if mapNode.isEmpty():
            cm = CardMaker('minimap-card')
            sideWidth = self.cellWidth * self.gridSize
            cm.setFrame(-sideWidth, sideWidth, -sideWidth, sideWidth)
            modelNode = ModelNode('minimap')
            modelNode.setPreserveTransform(1)
            mapNode = self.attachNewNode(modelNode)
            mapGeom = mapNode.attachNewNode(cm.generate())
            mapGeom.setP(-90)
            mapGeom.hide()

        return mapNode


    def getMinimap(self):
        if not self.minimap:
            self.setupMinimap()

        return self.minimap


    def setupMinimap(self):
        if not (self.minimap) and not self.getMapNode().isEmpty():
            self.minimap = OceanMap(self)



    def destroyMinimap(self):
        if self.minimap:
            self.minimap.destroy()
            self.minimap = None



