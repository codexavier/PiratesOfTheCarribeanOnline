# File: H (Python 2.4)

from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.distributed.ClockDelta import *
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import PLocalizer
from pirates.piratesbase import Freebooter
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesgui import GuiPanel
from pirates.piratesgui import Scoreboard
from pirates.piratesgui import DialogButton
from pirates.piratesgui import GuiButton
from pirates.ai import HolidayGlobals
from pirates.uberdog.UberDogGlobals import *
from pirates.economy import EconomyGlobals
from pirates.ship import ShipGlobals
from pirates.inventory.InventoryUIGlobals import *
from pirates.inventory import InventoryUIPlunderGridContainer
from pirates.battle import WeaponGlobals
import time

class HighSeasScoreboard(GuiPanel.GuiPanel):
    width = PiratesGuiGlobals.PortPanelWidth
    height = PiratesGuiGlobals.PortPanelHeight
    titleHeight = PiratesGuiGlobals.PortTitleHeight
    buffer = 0.050000000000000003
    
    def __init__(self, name, stats, playerStats, ship):
        GuiPanel.GuiPanel.__init__(self, '', self.width, self.height, showClose = False)
        self.ship = ship
        self.stats = stats
        self.playerStats = playerStats
        self.initialiseoptions(HighSeasScoreboard)
        self.leftPanel = None
        self.rightPanel = None
        titleTxt = PLocalizer.ScoreboardTitle
        if self.ship.shipClass == ShipGlobals.BLACK_PEARL:
            titleTxt = PLocalizer.BlackPearlScoreboard
        else:
            titleTxt = PLocalizer.LootScoreboard
        self.title = DirectLabel(parent = self, relief = None, text = titleTxt, text_align = TextNode.ALeft, text_scale = self.titleHeight, text_fg = PiratesGuiGlobals.TextFG10, text_shadow = PiratesGuiGlobals.TextShadow, pos = (0.029999999999999999, 0, self.height - self.titleHeight - 0.029999999999999999), text_font = PiratesGlobals.getPirateOutlineFont(), textMayChange = 1)
        self.closeButton = DialogButton.DialogButton(parent = self, buttonStyle = DialogButton.DialogButton.NO, text = PLocalizer.lClose, pos = (1.05, 0, 0.074999999999999997), command = self.closePanel)
        self.grids = { }
        self.manager = base.localAvatar.guiMgr.inventoryUIManager
        self.buttonSize = self.manager.standardButtonSize
        main_gui = loader.loadModel('models/gui/gui_main')
        generic_x = main_gui.find('**/x2')
        generic_box = main_gui.find('**/exit_button')
        generic_box_over = main_gui.find('**/exit_button_over')
        main_gui.removeNode()
        self.newCloseButton = GuiButton.GuiButton(parent = self, relief = None, pos = (2.2999999999999998, 0, 1.0800000000000001), image = (generic_box, generic_box, generic_box_over, generic_box), image_scale = 0.40000000000000002, command = self.closePanel)
        xButton = OnscreenImage(parent = self.newCloseButton, image = generic_x, scale = 0.20000000000000001, pos = (-0.25600000000000001, 0, 0.76600000000000001))
        gui = loader.loadModel('models/gui/toplevel_gui')
        buttonImage = (gui.find('**/generic_button'), gui.find('**/generic_button_down'), gui.find('**/generic_button_over'), gui.find('**/generic_button_disabled'))
        gui.removeNode()
        self.takeAllButton = DirectButton(parent = self, relief = None, image = buttonImage, image_scale = (0.26000000000000001, 1.0, 0.22), image0_color = VBase4(0.65000000000000002, 0.65000000000000002, 0.65000000000000002, 1), image1_color = VBase4(0.40000000000000002, 0.40000000000000002, 0.40000000000000002, 1), image2_color = VBase4(0.90000000000000002, 0.90000000000000002, 0.90000000000000002, 1), image3_color = VBase4(0.40999999999999998, 0.40000000000000002, 0.40000000000000002, 1), text = PLocalizer.InventoryPlunderTakeAll, text_font = PiratesGlobals.getPirateBoldOutlineFont(), text_align = TextNode.ACenter, text_pos = (0, -0.01), text_scale = PiratesGuiGlobals.TextScaleLarge, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, pos = (1.05, 0, 0.074999999999999997), command = self.takeAllLoot)
        self.setBin('gui-fixed', -1)
        self.createScoreboard()

    
    def destroy(self):
        if self.leftPanel:
            self.leftPanel.destroy()
            self.leftPanel = None
        
        if self.rightPanel:
            self.rightPanel.destroy()
            self.rightPanel = None
        
        for grid in self.grids.values():
            grid.destroy()
        
        self.grids = { }
        if self.manager:
            self.manager.removeScoreboard()
            self.manager = None
        
        GuiPanel.GuiPanel.destroy(self)

    
    def getMissionResults(self):
        (missionTime, shipDamage, skeletonKills, navyKills, creatureKills, seamonsterKills, pirateKills, townfolkKills, shipKills, repairCost, exp, gold, cargo, numCrew) = self.stats
        (pMissionTime, pShipDamage, pSkeletonKills, pNavyKills, pCreatureKills, pSeamonsterKills, pPirateKills, pTownfolkKills, pShipKills, pRepairCost, pExp, pGold, pCargo, pLootBoxes, dummyCrew) = self.playerStats
        inventory = base.localAvatar.getInventory()
        if inventory:
            currentGold = inventory.getGoldInPocket()
        
        t = time.gmtime(missionTime)
        totalTime = str(t[3]) + '"' + str(t[4]) + "'" + str(t[5])
        self.cargo = cargo
        cargoValue = EconomyGlobals.getCargoTotalValue(cargo)
        totalGold = max(cargoValue + gold - repairCost, 0)
        self.results = []
        self.results.append({
            'Type': 'Title',
            'Text': PLocalizer.PlunderedLootContainers,
            'Value1': '' })
        if len(pLootBoxes) == 0:
            self.results.append({
                'Type': 'Entry',
                'Text': PLocalizer.NoLootContainersPlundered,
                'Value1': '',
                'UnwrapMode': 1 })
        else:
            gold = 0
            height = 1.6499999999999999
            for lootBox in pLootBoxes:
                plunderList = lootBox[1]
                if lootBox[2] == PiratesGlobals.ITEM_SAC:
                    self.makeLootLabel(PLocalizer.LootContainerItemSac, height)
                elif lootBox[2] == PiratesGlobals.TREASURE_CHEST:
                    self.makeLootLabel(PLocalizer.LootContainerTreasureChest, height)
                elif lootBox[2] == PiratesGlobals.RARE_CHEST:
                    self.makeLootLabel(PLocalizer.LootContainerRareChest, height)
                
                height -= 0.029999999999999999
                ammoAmountIndex = 0
                self.setupPlunderGrid(plunderList, height, lootBox[0])
                plunderLength = len(plunderList)
                while plunderLength > 0:
                    height -= self.buttonSize
                    plunderLength -= 2
                height -= 0.10000000000000001
            
            self.manager.addScoreboard(self)
        return self.results

    
    def getCargoResults(self):
        (missionTime, shipDamage, skeletonKills, navyKills, creatureKills, seamonsterKills, pirateKills, townfolkKills, shipKills, repairCost, exp, gold, cargo, numCrew) = self.stats
        (pMissionTime, pShipDamage, pSkeletonKills, pNavyKills, pCreatureKills, pSeamonsterKills, pPirateKills, pTownfolkKills, pShipKills, pRepairCost, pExp, pGold, pCargo, pLootBoxes, dummyCrew) = self.playerStats
        inventory = base.localAvatar.getInventory()
        if inventory:
            currentGold = inventory.getGoldInPocket()
        
        avId = base.localAvatar.getDoId()
        cargoValue = EconomyGlobals.getCargoTotalValue(pCargo)
        totalGold = cargoValue + pGold
        bonusGold = 0
        if base.localAvatar.ship:
            if base.localAvatar.ship.getOwnerId() == avId and len(base.localAvatar.ship.getCrew()) > 1:
                bonusGold = int(totalGold * EconomyGlobals.CAPTAIN_LOOT_MULTIPLIER)
                totalGold += bonusGold
            
        
        if base.cr.newsManager:
            if base.cr.newsManager.getHoliday(HolidayGlobals.DOUBLEGOLDHOLIDAYPAID) or Freebooter.getPaidStatus(avId) or base.cr.newsManager.getHoliday(HolidayGlobals.DOUBLEGOLDHOLIDAY):
                totalGold *= 2
            
        netGold = totalGold - pRepairCost
        self.results = []
        self.results.append({
            'Type': 'Title',
            'Text': PLocalizer.CargoPlunder,
            'Value1': '' })
        if pGold:
            self.results.append({
                'Type': 'Entry',
                'Text': PLocalizer.GoldLooted,
                'Value1': pGold,
                'Value2': gold })
        
        if len(pCargo) == 0:
            self.results.append({
                'Type': 'Entry',
                'Text': PLocalizer.NoCargoLooted,
                'Value1': '',
                'UnwrapMode': 1 })
        else:
            for itemId in pCargo:
                self.results.append({
                    'Type': 'Cargo',
                    'Text': '',
                    'Value1': itemId,
                    'UnwrapMode': 1 })
            
        if bonusGold > 0:
            self.results.append({
                'Type': 'Space',
                'Text': '',
                'Value1': '',
                'UnwrapMode': 1 })
            self.results.append({
                'Type': 'Entry',
                'Text': PLocalizer.CaptainsBonus,
                'Value1': str(bonusGold) + ' ' + PLocalizer.MoneyName,
                'UnwrapMode': 1 })
        
        if base.cr.newsManager:
            if base.cr.newsManager.getHoliday(HolidayGlobals.DOUBLEGOLDHOLIDAYPAID) or Freebooter.getPaidStatus(avId) or base.cr.newsManager.getHoliday(HolidayGlobals.DOUBLEGOLDHOLIDAY):
                self.results.append({
                    'Type': 'Space',
                    'Text': '',
                    'Value1': '',
                    'UnwrapMode': 1 })
                self.results.append({
                    'Type': 'Entry',
                    'Text': PLocalizer.DoubleGoldBonus,
                    'Value1': str(totalGold / 2) + ' ' + PLocalizer.MoneyName,
                    'UnwrapMode': 1 })
            
        self.results.append({
            'Type': 'Space',
            'Text': '',
            'Value1': '',
            'UnwrapMode': 1 })
        self.results.append({
            'Type': 'Title',
            'Text': PLocalizer.PlunderShare,
            'Value1': str(netGold) + ' ' + PLocalizer.MoneyName,
            'UnwrapMode': 1 })
        return self.results

    
    def createScoreboard(self):
        (pMissionTime, pShipDamage, pSkeletonKills, pNavyKills, pCreatureKills, pSeamonsterKills, pPirateKills, pTownfolkKills, pShipKills, pRepairCost, pExp, pGold, pCargo, pLootBoxes, dummyCrew) = self.playerStats
        missionResults = self.getMissionResults()
        self.leftPanel = Scoreboard.Scoreboard('', (self.width - self.buffer * 2) / 2.0, self.height - 0.10000000000000001, missionResults, self.titleHeight)
        self.leftPanel.reparentTo(self)
        self.leftPanel.setPos(self.buffer, 0, 0.20000000000000001)
        cargoResults = self.getCargoResults()
        self.rightPanel = Scoreboard.Scoreboard('', (self.width - self.buffer * 2) / 2.0, self.height - 0.10000000000000001, cargoResults, self.titleHeight)
        self.rightPanel.reparentTo(self)
        self.rightPanel.setPos((self.width + self.buffer) / 2.0, 0, 0.20000000000000001)
        if len(pLootBoxes) == 0:
            self.leftPanel.hide()
            self.configure(frameSize = (self.width / 4.0, self.width * 3.0 / 4.0, 0, self.height))
            self.title.setX(self.width / 4.0 + 0.029999999999999999)
            self.rightPanel.setX(self.width / 4.0 + self.buffer)
        
        if len(pLootBoxes) == 0 and len(pCargo) == 0:
            self.takeAllButton.hide()
            self.newCloseButton.hide()
        elif len(pLootBoxes) == 0:
            self.closeButton.hide()
            self.newCloseButton.setX(1.77)
        else:
            self.closeButton.hide()
        self.accept('lootsystem-plunderContainer-Empty', self.checkAllContainers, [
            False])

    
    def getListFinishedMessage(self):
        return 'listFinished'

    
    def setupPlunderGrid(self, plunderList, height, containerId):
        if hasattr(base, 'localAvatar') and base.localAvatar.guiMgr:
            plunderLength = len(plunderList)
            odd = plunderLength % 2
            if odd:
                plunderLength += 1
            
            gridHeight = plunderLength / 2
            grid = InventoryUIPlunderGridContainer.InventoryUIPlunderGridContainer(self.manager, self.buttonSize * 6.5, self.buttonSize * float(gridHeight), 2, gridHeight)
            grid.reparentTo(self)
            grid.setPos(0.10000000000000001, 0, height - self.buttonSize * float(gridHeight))
            grid.setupPlunder(plunderList)
            self.grids[containerId] = grid
        

    
    def takeAllLoot(self, playSound = True):
        if not self.grids:
            if not self.isEmpty():
                self.closePanel()
            
            return None
        
        self.manager.takeAllLoot(self.grids.values(), playSound = playSound)
        self.checkAllContainers()

    
    def checkAllContainers(self, event = None):
        for grid in self.grids.values():
            for cell in grid.cellList:
                if cell.inventoryItem:
                    return None
                    continue
            
        
        if not self.isEmpty():
            self.closePanel()
        

    
    def makeLootLabel(self, text, height):
        label = DirectLabel(parent = self, relief = None, text = text, text_align = TextNode.ALeft, text_scale = PiratesGuiGlobals.TextScaleExtraLarge, text_fg = PiratesGuiGlobals.TextFG2, text_shadow = PiratesGuiGlobals.TextShadow, pos = (0.10000000000000001, 0, height))

    
    def payForShipRepairs(self):
        self.ship.requestRepairAll()

    
    def getShowNextItemMessage(self):
        return 'showNextHighSeaStat'

    
    def destroy(self):
        GuiPanel.GuiPanel.destroy(self)

    
    def closePanel(self):
        GuiPanel.GuiPanel.closePanel(self)
        self.destroy()
        messenger.send('highSeasScoreBoardClose')

    
    def requestItem(self, item):
        (pMissionTime, pShipDamage, pSkeletonKills, pNavyKills, pCreatureKills, pSeamonsterKills, pPirateKills, pTownfolkKills, pShipKills, pRepairCost, pExp, pGold, pCargo, pLootBoxes, dummyCrew) = self.playerStats
        for lootBox in pLootBoxes:
            for lootInfo in lootBox[1]:
                if item[0] == lootInfo[0] and item[1] == lootInfo[1] and item[2] == lootInfo[2]:
                    base.cr.lootMgr.d_requestItemFromContainer(lootBox[0], item)
                    return None
                    continue
            
        

    
    def removeLootContainer(self, containerId):
        grid = self.grids.pop(containerId, None)
        if grid:
            grid.destroy()
        

    
    def requestItems(self, items):
        (pMissionTime, pShipDamage, pSkeletonKills, pNavyKills, pCreatureKills, pSeamonsterKills, pPirateKills, pTownfolkKills, pShipKills, pRepairCost, pExp, pGold, pCargo, pLootBoxes, dummyCrew) = self.playerStats
        containers = { }
        for item in items:
            for lootBox in pLootBoxes:
                for lootInfo in lootBox[1]:
                    if item[0] == lootInfo[0] and item[1] == lootInfo[1] and item[2] == lootInfo[2]:
                        if lootBox[0] in containers:
                            containers[lootBox[0]].append(item)
                            continue
                        containers[lootBox[0]] = [
                            item]
                        continue
                        continue
                
            
        
        if base.cr.lootMgr and containers:
            base.cr.lootMgr.d_requestItems(list(containers.iteritems()))
        


