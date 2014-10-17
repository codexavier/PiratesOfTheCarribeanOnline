# File: M (Python 2.4)

from pandac.PandaModules import *
from direct.gui.DirectGui import *
from pirates.piratesbase import PLocalizer, PiratesGlobals
from pirates.piratesgui import InventoryPage, BorderFrame, ShardPanel, PiratesGuiGlobals, GuiButton
from pirates.piratesgui.DownloadBlockerPanel import DownloadBlockerPanel
from pirates.map.WorldMap import WorldMap

class MapPage(InventoryPage.InventoryPage):

    def __init__(self):
        InventoryPage.InventoryPage.__init__(self)
        self.initialiseoptions(MapPage)
        self.shardPanel = None
        self.worldMap = None
        self.gear = None
        self.portOfCall = ''
        self.portOfCallLabel = None
        self.portOfCallButton = None
        self.minimapButton = None
        self.createPortOfCall()
        self.createWorldMap()
        self.createFrontOrnament()
        self.createShardPanel()
        self.createButtons()
        self.hide()


    def destroy(self):
        InventoryPage.InventoryPage.destroy(self)
        self.shardPanel = None
        self.gear = None
        self.worldMap = None
        self.portOfCallLabel = None
        self.portOfCallButton = None
        self.minimapButton = None


    def show(self, *args, **kwargs):
        super(self.__class__, self).show(*args, **kwargs)
        self.worldMap.enable()
        self.worldMap.show()


    def slideOpenCallback(self):
        self.worldMap.resetArcBall()
        self.worldMap.rotateAvatarToCenter()


    def hide(self, *args, **kwargs):
        super(self.__class__, self).hide(*args, **kwargs)
        self.worldMap.disable()
        self.worldMap.hide()


    def slideCloseCallback(self):
        self.shardPanel.hideIfShown()


    def createPortOfCall(self):
        if self.portOfCallLabel:
            self.portOfCallLabel.destroy()

        if self.portOfCallButton:
            self.portOfCallButton.destroy()

        compassGui = loader.loadModel('models/gui/compass_gui')
        topGui = loader.loadModel('models/gui/toplevel_gui')
        teleportIcon = topGui.find('**/treasure_w_b_slot_empty').copyTo(NodePath(''))
        compassGui.find('**/compass_icon_objective_green').copyTo(teleportIcon)
        teleportIcon.flattenStrong()
        self.portOfCallLabel = DirectLabel(parent = self, text = '', text_align = TextNode.ALeft, text_font = PiratesGlobals.getPirateOutlineFont(), text_scale = 0.044999999999999998, text_fg = PiratesGuiGlobals.TextFG2, textMayChange = 1, pos = (0.48999999999999999, 0, 0.072999999999999995))
        self.portOfCallButton = GuiButton.GuiButton(parent = self, pos = (0.38, 0, 0.085000000000000006), scale = 0.84999999999999998, text = PLocalizer.Return, text_pos = (0.033000000000000002, -0.014), text_scale = 0.044999999999999998, textMayChange = 1, image3_color = (0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1), geom = teleportIcon, geom_pos = (-0.065000000000000002, 0, 0), geom_scale = 0.20000000000000001, command = self.handlePortOfCall)


    def createFrontOrnament(self):
        geom = loader.loadModel('models/gui/gui_map_window')
        geom.reparentTo(self)
        geom.setPos(0.54000000000000004, 0, 0.72499999999999998)
        geom.setScale(0.32000000000000001)
        geom.flattenStrong()


    def createButtons(self):
        if not base.config.GetBool('want-momentary-minimap', 1):
            guiMain = loader.loadModel('models/gui/gui_main')
            btImages = (guiMain.find('**/minimap_button'), guiMain.find('**/minimap_button'), guiMain.find('**/minimap_button_over'), guiMain.find('**/minimap_button'))
            self.minimapButton = GuiButton.GuiButton(parent = self, image = btImages, selectedImage = btImages, pos = (0.90000000000000002, 0, 1.1599999999999999), scale = 1.5, hotkeys = [
                'f8'], hotkeyLabel = 'F8', command = self.handleMinimapButton)
            self.minimapButton.hotkeyLabel.setPos(-0.050000000000000003, 0.0, -0.050000000000000003)
            self.minimapButton.hotkeyLabel.setScale(0.75)
        else:
            self.minimapButton = None


    def createWorldMap(self):
        self.worldMap = WorldMap(parent = self, state = DGG.NORMAL, pos = (0.55000000000000004, 0, 0.62), scale = 0.46999999999999997)
        if __dev__ and 0:

            def changeMouseMode():
                self.worldMap.mapBall.rMode += 1
                self.worldMap.mapBall.rMode %= 2
                self.mouseModeLabel['text'] = `self.worldMap.mapBall.rMode`

            self.mouseModeButton = DirectButton(parent = self, text = 'MouseMode', scale = 0.065000000000000002, pos = (0.25, 0, 0.089999999999999997), command = changeMouseMode)
            self.mouseModeLabel = DirectLabel(parent = self, scale = 0.074999999999999997, pos = (0.5, 0, 0.086999999999999994), text = `self.worldMap.mapBall.rMode`, text_fg = (1, 1, 1, 1), textMayChange = 1)



    def createShardPanel(self):
        if self.shardPanel:
            self.shardPanel.destroy()
            self.clearClipPlane()

        if self.gear:
            self.gear.detachNode()

        gui = loader.loadModel('models/gui/gui_map_window_drawer')
        gui.reparentTo(self)
        gui.setPos(0.55000000000000004, 0, 0.72499999999999998)
        gui.setScale(0.32000000000000001)
        self.gear = gui.find('**/gear')
        self.gear.wrtReparentTo(self)
        gui.detachNode()
        self.shardPanel = ShardPanel.ShardPanel(parent = self, relief = None, gear = self.gear)
        self.setScissor(Point3(-2, 0, -2), Point3(2.0, 0, 1.3500000000000001))
        if __dev__ and 0:

            def showShardList():
                self.shardPanel.show()
                self.shardButton['text'] = 'Hide Shards'
                self.shardButton['command'] = hideShardList


            def hideShardList():
                self.shardPanel.hide()
                self.shardButton['text'] = 'Show Shards'
                self.shardButton['command'] = showShardList

            self.shardButton = DirectButton(parent = self, text = 'Show Shards', scale = 0.065000000000000002, pos = (0.75, 0, 0.089999999999999997), command = showShardList, textMayChange = 1)



    def handleMinimapButton(self, *args):
        localAvatar.guiMgr.nextMinimap()


    def updateTeleportIsland(self, teleportToken, amt):
        self.worldMap.updateTeleportIsland(teleportToken)


    def setReturnIsland(self, islandUid):
        self.worldMap.setReturnIsland(islandUid)
        self.setPortOfCall(islandUid)


    def setCurrentIsland(self, islandUid):
        self.worldMap.setCurrentIsland(islandUid)


    def setPortOfCall(self, islandUid):
        self.portOfCall = islandUid
        self.worldMap.setPortOfCall(self.portOfCall)
        if self.portOfCall:
            self.portOfCallLabel.show()
            self.portOfCallButton.show()
            islandName = PLocalizer.LocationNames.get(islandUid)
            if islandName:
                self.portOfCallLabel['text'] = '%s %s' % (PLocalizer.WordTo, islandName)
            else:
                self.portOfCallLabel['text'] = '%s %s' % (PLocalizer.WordTo, 'Unknown Island')
        else:
            self.portOfCallLabel.hide()
            self.portOfCallButton.hide()
            self.portOfCallLabel['text'] = ''


    def handlePortOfCall(self):
        if self.portOfCall:
            if launcher.canLeaveFirstIsland():
                base.cr.teleportMgr.requestTeleportToIsland(self.portOfCall)
            else:
                base.cr.centralLogger.writeClientEvent('Player encountered phase 4 blocker trying to teleport to port-of-call')
                localAvatar.guiMgr.showDownloadBlocker(DownloadBlockerPanel.Reasons.TELEPORT)



    def addQuestDart(self, questId, worldPos):
        return self.worldMap.addQuestDart(questId, worldPos)


    def updateQuestDart(self, questId, worldPos):
        return self.worldMap.updateQuestDart(questId, worldPos)


    def removeQuestDart(self, questId):
        return self.worldMap.removeQuestDart(questId)


    def addLocalAvDart(self, worldPos = Vec3(0)):
        return self.worldMap.addLocalAvDart(worldPos)


    def updateLocalAvDart(self, worldPos):
        return self.worldMap.updateLocalAvDart(worldPos)


    def addIsland(self, name, islandUid, modelPath, pos, h):
        return self.worldMap.addIsland(name, islandUid, modelPath, pos, h)


    def updateIsland(self, name, worldPos = None, rotation = None):
        return self.worldMap.updateIsland(name, worldPos, rotation)


    def removeIsland(self, name):
        return self.worldMap.removeIsland(name)


    def addOceanArea(self, name, areaUid, pos1, pos2):
        self.worldMap.addOceanArea(name, areaUid, pos1, pos2)


    def addShip(self, shipInfo, worldPos):
        self.worldMap.addShip(shipInfo, worldPos)


    def removeShip(self, shipDoId):
        self.worldMap.removeShip(shipDoId)


    def addFleet(self, fleetObj):
        self.worldMap.addFleet(fleetObj)


    def removeFleet(self, fleetObj):
        self.worldMap.removeFleet(fleetObj)


    def addPath(self, pathInfo):
        self.worldMap.addPath(pathInfo)


    def removePath(self, pathInfo):
        self.worldMap.removePath(pathInfo)


