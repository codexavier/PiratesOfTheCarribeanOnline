import types
import random
import gc
import __builtin__
base.loadingScreen.beginStep('PCR', 20, 15)
from direct.showbase.ShowBaseGlobal import *
base.loadingScreen.tick()
from direct.distributed.ClockDelta import *
base.loadingScreen.tick()
from direct.gui.DirectGui import *
base.loadingScreen.tick()
from pandac.PandaModules import *
base.loadingScreen.tick()
from otp.nametag import NametagGlobals
base.loadingScreen.tick()
from direct.interval.IntervalGlobal import *
base.loadingScreen.tick()
from direct.showbase.EventGroup import EventGroup
base.loadingScreen.tick()
from direct.showbase.PythonUtil import report
base.loadingScreen.tick()
from pirates.piratesbase.PiratesGlobals import *
base.loadingScreen.tick()
from PiratesMsgTypes import *
base.loadingScreen.tick()
from direct.directnotify.DirectNotifyGlobal import directNotify
base.loadingScreen.tick()
from direct.fsm import ClassicFSM
base.loadingScreen.tick()
from direct.fsm import State
base.loadingScreen.tick()
from direct.task import Task
base.loadingScreen.tick()
from direct.distributed.PyDatagram import PyDatagram
base.loadingScreen.tick()
from direct.distributed.PyDatagramIterator import PyDatagramIterator
base.loadingScreen.tick()
from direct.distributed import DistributedSmoothNode
base.loadingScreen.tick()
from direct.distributed.InterestWatcher import InterestWatcher
base.loadingScreen.tick()
from direct.distributed import DoInterestManager
from direct.distributed.ClientRepositoryBase import ClientRepositoryBase
from otp.distributed.OTPClientRepository import OTPClientRepository
from otp.distributed import PotentialShard
from otp.distributed.PotentialAvatar import PotentialAvatar
from otp.distributed import DistributedDistrict
from otp.distributed import OtpDoGlobals
from otp.otpbase import OTPGlobals
from otp.friends import FriendSecret
from otp.uberdog.AccountDetailRecord import AccountDetailRecord, SubDetailRecord
from otp.otpgui import OTPDialog
from pirates.login.AvatarChooser import AvatarChooser
from pirates.makeapirate.MakeAPirate import MakeAPirate
from pirates.pirate import HumanDNA
from pirates.pirate import MasterHuman, Human
from pirates.pirate import AvatarTypes
from pirates.pirate.LocalPirate import LocalPirate
from pirates.pirate import DistributedPlayerPirate
from pirates.piratesbase import PLocalizer
from pirates.world import WorldGlobals
from pirates.world.DistributedGameArea import DistributedGameArea
from pirates.battle import BattleManager
from pirates.battle import DistributedBattleNPC
from pirates.battle import CombatAnimations
from pirates.band import DistributedBandMember
from pirates.cutscene import Cutscene
import PlayGame
from pirates.piratesbase import PiratesGlobals
from pirates.battle import DistributedBattleNPC
from pirates.ship import DistributedSimpleShip
from pirates.interact import InteractionManager
from pirates.piratesbase import UniqueIdManager
from pirates.piratesgui.DialMeter import DialMeter
from pirates.piratesgui import PiratesGuiGlobals
from pirates.uberdog.UberDogGlobals import InventoryType
from pirates.reputation import ReputationGlobals
from pirates.piratesbase import PLocalizer
from pirates.piratesbase import LoadingScreen
from pirates.ai import NewsManager
from pirates.makeapirate import PCPickANamePattern
from pirates.coderedemption.CodeRedemption import CodeRedemption
base.loadingScreen.endStep('PCR')
from pirates.quest import QuestLadderDynMap
from pirates.quest.QuestLadderDependency import QuestLadderDependency
from pirates.quest.QuestChoiceDynMap import QuestChoiceDynMap
from pirates.npc import NPCManager
from pirates.audio import SoundGlobals
from pirates.audio.SoundGlobals import loadSfx
from pirates.login.AccountDetailRecord import AccountDetailRecord


class bp:
    loginCfg = bpdb.bpGroup(iff = True, cfg = 'loginCfg', static = 1)


class PiratesClientRepository(OTPClientRepository):
    notify = directNotify.newCategory('PiratesClientRepository')
    SupportTutorial = 0
    GameGlobalsId = OTP_DO_ID_PIRATES
    StopVisibilityEvent = 'pirates-stop-visibility'

    def __init__(self, serverVersion, launcher = None):
        self.loadingScreen = base.loadingScreen
        self.loadingScreen.parent = self
        self.accept('connectionIssue', self.loadingScreen.hide)
        self.accept('connectionRetrying', self.loadingScreen.show)
        OTPClientRepository.__init__(self, serverVersion, launcher, playGame = PlayGame.PlayGame)
        self.createAvatarClass = DistributedPlayerPirate.DistributedPlayerPirate
        self.tradeManager = None
        self.pvpManager = None
        self.csm = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_CLIENT_SERVICES_MANAGER, 'ClientServicesManager')
        #self.avatarManager = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_PIRATES_AVATAR_MANAGER, 'DistributedAvatarManager')
        #self.chatManager = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_CHAT_MANAGER, 'DistributedChatManager')
        #self.crewMatchManager = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_PIRATES_CREW_MATCH_MANAGER, 'DistributedCrewMatchManager')
        #self.avatarFriendsManager = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_AVATAR_FRIENDS_MANAGER, 'PCAvatarFriendsManager')
        #self.playerFriendsManager = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_PLAYER_FRIENDS_MANAGER, 'PCPlayerFriendsManager')
        #self.guildManager = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_PIRATES_GUILD_MANAGER, 'PCGuildManager')
        #self.speedchatRelay = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_PIRATES_SPEEDCHAT_RELAY, 'PiratesSpeedchatRelay')
        #self.shipLoader = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_PIRATES_SHIP_MANAGER, 'DistributedShipLoader')
        #self.matchMaker = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_PIRATES_MATCH_MAKER, 'DistributedMatchMaker')
        base.loadingScreen.tick()
        #self.codeRedemption = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_PIRATES_CODE_REDEMPTION, 'CodeRedemption')
        base.loadingScreen.tick()
        #self.settingsMgr = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_PIRATES_SETTINGS_MANAGER, 'PiratesSettingsMgr')
        #self.statusDatabase = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_STATUS_DATABASE, 'StatusDatabase')
        self.wantSeapatch = base.config.GetBool('want-seapatch', 1)
        self.wantSpecialEffects = base.config.GetBool('want-special-effects', 1)
        self.wantMakeAPirate = base.config.GetBool('wantMakeAPirate', 0)
        self.forceTutorial = base.config.GetBool('force-tutorial', 0)
        self.skipTutorial = base.config.GetBool('skip-tutorial', 0)
        self.tutorialObject = None
        self.avChoiceDoneEvent = None
        self.avChoice = None
        self.avCreate = None
        self.currentCutscene = None
        self.activeWorld = None
        self.oldWorld = None
        self.teleportMgr = None
        self.treasureMap = None
        self.newsManager = None
        self.distributedDistrict = None
        self.district = None
        self.profileMgr = None
        self.battleMgr = BattleManager.BattleManager(self)
        self.combatAnims = CombatAnimations.CombatAnimations()
        self.interactionMgr = InteractionManager.InteractionManager()
        self.currCamParent = None
        self.uidMgr = UniqueIdManager.UniqueIdManager(self)
        self.fakeMSP = None
        self.questDynMap = QuestLadderDynMap.QuestLadderDynMap()
        self.questDependency = QuestLadderDependency()
        self.questChoiceSibsMap = QuestChoiceDynMap()
        base.loadingScreen.beginStep('MasterHumans', 52, 45)
        self.humanHigh = [
            MasterHuman.MasterHuman(),
            MasterHuman.MasterHuman()]
        self.humanHigh[0].billboardNode.removeNode()
        self.humanHigh[1].billboardNode.removeNode()
        self.humanHigh[0].style = HumanDNA.HumanDNA('m')
        self.humanHigh[1].style = HumanDNA.HumanDNA('f')
        self.humanHigh[0].generateHuman('m')
        base.loadingScreen.tick()
        self.humanHigh[1].generateHuman('f')
        base.loadingScreen.tick()
        self.humanHigh[0].ignoreAll()
        self.humanHigh[1].ignoreAll()
        self.humanHigh[0].stopBlink()
        self.humanHigh[1].stopBlink()
        self.humanLow = [
            MasterHuman.MasterHuman(),
            MasterHuman.MasterHuman()]
        self.humanLow[0].billboardNode.removeNode()
        self.humanLow[1].billboardNode.removeNode()
        self.humanLow[0].style = HumanDNA.HumanDNA('m')
        self.humanLow[1].style = HumanDNA.HumanDNA('f')
        self.humanLow[0].generateHuman('m')
        base.loadingScreen.tick()
        self.humanLow[1].generateHuman('f')
        base.loadingScreen.tick()
        base.loadingScreen.endStep('MasterHumans')
        self.humanLow[0].ignoreAll()
        self.humanLow[1].ignoreAll()
        self.humanLow[0].stopBlink()
        self.humanLow[1].stopBlink()
        for i in range(2):
            self.humanLow[i]._Actor__sortedLODNames = [
                '500']
            del self.humanLow[i]._Actor__partBundleDict['2000']
            del self.humanLow[i]._Actor__partBundleDict['1000']
            self.humanLow[i].getLOD('2000').detachNode()
            self.humanLow[i].getLOD('1000').detachNode()
            self.humanLow[i].getLODNode().clearSwitches()
            self.humanLow[i].getLODNode().addSwitch(10000, 0)

        if base.options.getCharacterDetailSetting() == 0:
            self.human = self.humanLow
        else:
            self.human = self.humanHigh
        A = AvatarTypes
        del A
        self.preloadedCutscenes = { }
        self.defaultShard = 0
        if __dev__:
            __builtin__.go = self.getDo
            self.effectTypes = {
                'damageSmoke': [
                    'BlackSmoke'],
                'damageFire': [
                    'Fire'],
                'cannonDeckFire': [
                    'CannonSmokeSimple',
                    'CannonBlastSmoke'],
                'cannonBSFire': [
                    'MuzzleFlameBS',
                    'CannonSmokeSimpleBS',
                    'CannonBlastSmokeBS',
                    'GrapeshotEffectBS'],
                'cannonHit': [
                    'SimpleSmokeCloud',
                    'ExplosionFlip'],
                'cannonSplash': [
                    'CannonSplash'] }
            self.effectToggles = { }

        self.cannonballCollisionDebug = 1
        self.npcManager = NPCManager.NPCManager()
        self.accountDetailRecord = AccountDetailRecord()


    def gotoFirstScreen(self):
        base.loadingScreen.beginStep('PrepLogin', 9, 0.14000000000000001)
        self.startReaderPollTask()
        #self.startHeartbeat()
        base.loadingScreen.tick()
        self.loginFSM.request('login')
        base.loadingScreen.tick()
        base.loadingScreen.endStep('PrepLogin')

    gotoFirstScreen = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(gotoFirstScreen)

    def getOldWorld(self):
        return self.oldWorld


    def getActiveWorld(self):
        return self.activeWorld


    def preloadCutscene(self, name):
        if name not in self.preloadedCutscenes:
            newCutscene = Cutscene.Cutscene(self, name)
            self.preloadedCutscenes[name] = newCutscene



    def getPreloadedCutsceneInfo(self, name):
        return self.preloadedCutscenes.get(name)


    def cleanupPreloadedCutscene(self, name):
        plCutscene = self.preloadedCutscenes.get(name)
        if plCutscene:
            if not plCutscene.isEmpty():
                plCutscene.destroy()

            del self.preloadedCutscenes[name]



    def setActiveWorld(self, world):
        if self.activeWorld != world:
            self.oldWorld = self.activeWorld

        self.activeWorld = world

    setActiveWorld = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(setActiveWorld)

    def getWaterHeight(self, node):
        if self.wantSeapatch and self.activeWorld:
            water = self.activeWorld.getWater()
            if water:
                return water.calcHeight(node = node)

        else:
            return 0.0


    def isOceanEnabled(self):
        if self.wantSeapatch and self.activeWorld and self.activeWorld.hasWater():
            return self.activeWorld.getWater().enabled

        return 0


    def enterChooseAvatar(self, avList):
        base.loadingScreen.beginStep('AvChooser', 14, 10)
        self.sendSetAvatarIdMsg(0)
        self.handler = self.handleMessageType
        if __dev__:
            bp.loginCfg()
            config_slot = base.config.GetInt('login-pirate-slot', -1)
            if config_slot >= 0 and len(avList) > 0:
                config_subId = base.config.GetInt('login-pirate-subId', avList.keys()[0])
                slots = avList.get(config_subId, [])
                if config_slot in range(len(slots)):
                    potAv = slots[config_slot]
                    if isinstance(potAv, PotentialAvatar):
                        base.cr.loadingScreen.hide()
                        ConfigVariableInt('login-pirate-slot').setValue(-1)
                        base.loadingScreen.endStep('AvChooser')
                        base.cr.avatarManager.sendRequestPlayAvatar(potAv.id, config_subId)
                        self.handleAvatarChoice('chose', config_subId, config_slot)
                        return None




        self.avChoiceDoneEvent = 'avatarChooserDone'
        self.avChoice = AvatarChooser(self.loginFSM, self.avChoiceDoneEvent)
        base.loadingScreen.tick()
        self.avChoice.load()
        base.loadingScreen.tick()
        self.avChoice.enter()
        base.loadingScreen.tick()
        self.accept(self.avChoiceDoneEvent, self.__handleAvatarChooserDone)
        base.loadingScreen.endStep('AvChooser')
        base.cr.loadingScreen.hide()

    enterChooseAvatar = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(enterChooseAvatar)

    def __handleAvatarChooserDone(self, doneStatus):
        done = doneStatus['mode']
        if done == 'exit':
            self.notify.info('handleAvatarChooserDone: shutting down')
            self.loginFSM.request('shutdown')
            return None

        (subId, slot) = self.avChoice.getChoice()
        self.avChoice.exit()
        self.handleAvatarChoice(done, subId, slot)

    __handleAvatarChooserDone = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(__handleAvatarChooserDone)

    def handleAvatarChoice(self, done, subId, slot):
        access = self.accountDetailRecord.subDetails[subId].subAccess
        base.setEmbeddedFrameMode(access)
        if done == 'chose':
            av = self.avList[subId][slot]
            if av.dna.getTutorial() < 3 and self.skipTutorial == 0:
                self.tutorial = 1
            else:
                self.tutorial = 0
            self.loadingScreen.beginStep('waitForAv')
            self.loginFSM.request('waitForSetAvatarResponse', [
                av])
        elif done == 'create':
            self.loginFSM.request('createAvatar', [
                self.avList[subId],
                slot,
                subId])



    def exitChooseAvatar(self):
        self.handler = None
        if self.avChoice:
            self.avChoice.exit()
            self.avChoice.unload()
            self.avChoice = None

        if self.avChoiceDoneEvent:
            self.ignore(self.avChoiceDoneEvent)
            self.avChoiceDoneEvent = None


    exitChooseAvatar = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(exitChooseAvatar)

    def enterCreateAvatar(self, avList, index, subId):
        self.tutorial = 0
        self.avCreate = MakeAPirate(avList, 'makeAPirateComplete', subId, index, self.isPaid())
        self.avCreate.load()
        self.avCreate.enter()
        self.accept('makeAPirateComplete', self.__handleMakeAPirate)

    enterCreateAvatar = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(enterCreateAvatar)

    def handleAvatarCreated(self, newPotAv, avatarId, subId):
        newPotAv.id = avatarId
        self.loginFSM.request('waitForSetAvatarResponse', [newPotAv])

    handleAvatarCreated = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(handleAvatarCreated)

    def __handleMakeAPirate(self):
        done = self.avCreate.getDoneStatus()
        if done == 'cancel':
            self.avCreate.exit()
            self.loginFSM.request('chooseAvatar', [self.avList])
        elif done == 'created':
            self.handleAvatarCreated(self.avCreate.newPotAv, self.avCreate.avId, self.avCreate.subId)
        else:
            self.notify.error('Invalid doneStatus from MakeAPirate: ' + str(done))

    __handleMakeAPirate = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(__handleMakeAPirate)

    def exitCreateAvatar(self):
        if self.skipTutorial:
            self.ignore('makeAPirateComplete')
            self.ignore('nameShopPost')
            self.ignore('nameShopCreateAvatar')
            self.avCreate.exit()
            self.avCreate.unload()
            self.avCreate = None
            self.handler = None

        self.ignore('createdNewAvatar')

    exitCreateAvatar = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(exitCreateAvatar)

    def handleCreateAvatarResponse(self, avId):
        self.avId = avId
        newPotAv = PotentialAvatar(self.avId, [self.newName, '', '', ''], self.newDNA, self.newPosition, 1)
        self.loginFSM.request('waitForSetAvatarResponse', [newPotAv])

    def avatarListFailed(self, reason):
        dialogClass = OTPGlobals.getGlobalDialogClass()
        self.avatarListFailedBox = dialogClass(message = PLocalizer.CRAvatarListFailed, doneEvent = 'avatarListFailedAck', text_wordwrap = 18, style = OTPDialog.Acknowledge)
        self.avatarListFailedBox.show()
        self.acceptOnce('avatarListFailedAck', self.__handleAvatarListFailedAck)

    avatarListFailed = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(avatarListFailed)

    def __handleAvatarListFailedAck(self):
        self.ignore('avatarListFailedAck')
        self.avatarListFailedBox.cleanup()
        self.loginFSM.request('shutdown')

    __handleAvatarListFailedAck = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(__handleAvatarListFailedAck)

    def avatarList(self, avatars):
        self.ignore('avatarListFailed')
        self.ignore('avatarList')
        self.avList = avatars
        if self.loginFSM.getCurrentState().getName() == 'chooseAvatar':
            self.avChoice.updateAvatarList()
        else:
            self.loginFSM.request('chooseAvatar', [self.avList])

    avatarList = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(avatarList)

    def handleGetAvatarsRespMsg(self, di):
        pass

    handleGetAvatarsRespMsg = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(handleGetAvatarsRespMsg)

    def handleGetAvatarsResp2Msg(self, di):
        pass

    handleGetAvatarsResp2Msg = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(handleGetAvatarsResp2Msg)

    def handleAvatarResponseMsg(self, di):
        self.loadingScreen.endStep('waitForAv')
        self.cleanupWaitingForDatabase()
        avatarId = di.getUint32()
        returnCode = di.getUint8()
        if returnCode == 0:
            dclass = self.dclassesByName['DistributedPlayerPirate']
            NametagGlobals.setMasterArrowsOn(0)
            self.loadingScreen.show(waitForLocation = True, expectedLoadScale = 4)
            self.loadingScreen.beginStep('LocalAvatar', 36, 120)
            localAvatar = LocalPirate(self)
            localAvatar.dclass = dclass
            if __dev__:
                __builtins__['lu'] = self.getDo

            localAvatar.doId = avatarId
            self.localAvatarDoId = avatarId
            self.doId2do[avatarId] = localAvatar
            parentId = None
            zoneId = None
            localAvatar.setLocation(parentId, zoneId)
            localAvatar.generate()
            localAvatar.updateAllRequiredFields(dclass, di)
            locUID = localAvatar.getReturnLocation()
            if __dev__ and not getBase().config.GetBool('login-location-used-pcr', False):
                bp.loginCfg()
                ConfigVariableBool('login-location-used-pcr').setValue(True)
                config_location = getBase().config.GetString('login-location', '').lower()
                config_location_uid = PLocalizer.LocationUids.get(config_location)
                if config_location and config_location_uid:
                    locUID = config_location_uid
                    localAvatar.setReturnLocation(locUID)


            if locUID:
                self.loadingScreen.showTarget(locUID)
                self.loadingScreen.showHint(locUID)
            else:
                locUID = '1150922126.8dzlu'
                localAvatar.setReturnLocation(locUID)
                self.loadingScreen.showTarget(jail = True)
            self.loadingScreen.endStep('LocalAvatar')
            self.loginFSM.request('playingGame')
        else:
            self.notify.error('Bad avatar: return code %d' % returnCode)

    handleAvatarResponseMsg = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(handleAvatarResponseMsg)

    def enterWaitForDeleteAvatarResponse(self, potentialAvatar):
        raise StandardError, 'This should be handled within AvatarChooser.py'

    enterWaitForDeleteAvatarResponse = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(enterWaitForDeleteAvatarResponse)

    def exitWaitForDeleteAvatarResponse(self):
        raise StandardError, 'This should be handled within AvatarChooser.py'

    exitWaitForDeleteAvatarResponse = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(exitWaitForDeleteAvatarResponse)

    def sendUpdateToGlobalDoId(self, dclassName, fieldName, doId, args):
        dcfile = self.getDcFile()
        dclass = dcfile.getClassByName(dclassName)
        dg = dclass.clientFormatUpdate(fieldName, doId, args)
        self.send(dg)

    sendUpdateToGlobalDoId = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(sendUpdateToGlobalDoId)

    def sendMsgToTravelAgent(self, fieldName, args):
        self.sendUpdateToGlobalDoId('DistributedTravelAgent', fieldName, OtpDoGlobals.OTP_DO_ID_PIRATES_TRAVEL_AGENT, args)

    sendMsgToTravelAgent = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(sendMsgToTravelAgent)

    def enterPlayingGame(self):
        OTPClientRepository.enterPlayingGame(self)
        if __dev__ and config.GetDouble('want-dev-hotkeys', 0):

            def toggleKraken():
                if base.localAvatar:
                    if base.localAvatar.ship:
                        messenger.send('magicWord', [
                            '~kraken',
                            base.localAvatar.getDoId(),
                            base.localAvatar.zoneId])



            self.accept(PiratesGlobals.KrakenHotkey, toggleKraken)


        def logout():
            if not base.config.GetBool('location-kiosk', 0) and hasattr(base, 'localAvatar') and localAvatar.getCanLogout():
                self._userLoggingOut = True
                self.gameFSM.request('closeShard', [
                    'waitForAvatarList'])


        self._userLoggingOut = False
        self.accept(PiratesGlobals.LogoutHotkey, logout)
        if __dev__ and config.GetDouble('want-dev-hotkeys', 0):

            def deployShip():
                messenger.send('magicWord', [
                    '~deployShip',
                    base.localAvatar.getDoId(),
                    base.localAvatar.zoneId])

            self.accept(PiratesGlobals.ShipHotkey, deployShip)

        if localAvatar.style.getTutorial() < PiratesGlobals.TUT_MET_JOLLY_ROGER and self.skipTutorial == 0:
            localAvatar.teleportToType = PiratesGlobals.INSTANCE_TUTORIAL
            localAvatar.teleportToName = WorldGlobals.PiratesTutorialSceneFileBase
            self.sendMsgToTravelAgent('requestInitLocUD', [
                'unused',
                0])
        elif localAvatar.onWelcomeWorld and self.defaultShard != 0 and config.GetBool('want-welcome-worlds', 0):
            localAvatar.teleportToType = PiratesGlobals.INSTANCE_WELCOME
            localAvatar.teleportToName = 'Welcome World'
            self.sendMsgToTravelAgent('requestInitLocUD', [
                'unused',
                0])
        else:
            desiredShard = self.defaultShard
            localAvatar.teleportToType = PiratesGlobals.INSTANCE_MAIN
            localAvatar.teleportToName = WorldGlobals.PiratesWorldSceneFileBase
            self.sendMsgToTravelAgent('requestInitLocUD', [
                'unused',
                desiredShard])
        base.loadingScreen.beginStep('beginTeleport', 11, 32)

    enterPlayingGame = report(types = [
        'args',
        'deltaStamp',
        'module'], dConfigParam = 'teleport')(enterPlayingGame)

    def playingGameLocReceived(self, shardId, zoneId):
        self.gameFSM.request('waitOnEnterResponses', [
            shardId,
            zoneId,
            zoneId,
            -1])

    playingGameLocReceived = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(playingGameLocReceived)

    def exitPlayingGame(self):
        self.notify.info('exitPlayingGame')
        ivalMgr.interrupt()
        self.notify.info('sending clientLogout')
        messenger.send('clientLogout')
        if config.GetDouble('want-dev-hotkeys', 0):
            self.ignore(PiratesGlobals.KrakenHotkey)
            self.ignore(PiratesGlobals.ShipHotkey)
            self.ignore(PiratesGlobals.LogoutHotkey)

        self.uidMgr.reset()
        if self.distributedDistrict:
            self.distributedDistrict.worldCreator.cleanupAllAreas()

        for (doId, obj) in self.doId2do.items():
            if not isinstance(obj, LocalPirate) and not isinstance(obj, DistributedDistrict.DistributedDistrict):
                if hasattr(self, 'disableObject'):
                    self.disableObject(doId)

            hasattr(self, 'disableObject')

        if hasattr(base, 'localAvatar'):
            camera.reparentTo(render)
            camera.setPos(0, 0, 0)
            camera.setHpr(0, 0, 0)

        base.transitions.noTransitions()
        if self._userLoggingOut:
            self.detectLeaks(okTasks = [
                'physics-avatar',
                'memory-monitor-task',
                'multitexFlatten'], okEvents = [
                'destroy-ToontownLoadingScreenTitle',
                'destroy-ToontownLoadingScreenTip',
                'destroy-ToontownLoadingScreenWaitBar',
                'f12',
                'f7',
                'close_main_window',
                'open_main_window',
                PiratesGlobals.LogoutHotkey])

        OTPClientRepository.exitPlayingGame(self)

    exitPlayingGame = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(exitPlayingGame)

    def enterTutorialQuestion(self, hoodId, zoneId, avId):
        self.__requestTutorial(hoodId, zoneId, avId)

    enterTutorialQuestion = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(enterTutorialQuestion)

    def handleTutorialQuestion(self, msgType, di):
        if msgType == CLIENT_CREATE_OBJECT_REQUIRED:
            self.handleGenerateWithRequired(di)
        elif msgType == CLIENT_CREATE_OBJECT_REQUIRED_OTHER:
            self.handleGenerateWithRequiredOther(di)
        elif msgType == CLIENT_OBJECT_UPDATE_FIELD:
            self.handleUpdateField(di)
        elif msgType == CLIENT_OBJECT_DISABLE:
            self.handleDisable(di)
        elif msgType == CLIENT_OBJECT_DISABLE_OWNER:
            self.handleDisableOwner(di)
        elif msgType == CLIENT_OBJECT_DELETE_RESP:
             self.handleDelete(di)
        elif msgType == CLIENT_GET_AVATAR_DETAILS_RESP:
            self.handleGetAvatarDetailsResp(di)
        else:
            self.handleUnexpectedMsgType(msgType, di)

    handleTutorialQuestion = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(handleTutorialQuestion)

    def exitTutorialQuestion(self):
        self.handler = None
        self.handlerArgs = None
        self.ignore('startTutorial')
        taskMgr.remove('waitingForTutorial')

    exitTutorialQuestion = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(exitTutorialQuestion)

    def __requestTutorial(self, hoodId, zoneId, avId):
        self.acceptOnce('startTutorial', self.__handleStartTutorial, [
            avId])
        messenger.send('requestTutorial')

    __requestTutorial = report(types = [
        'args',
        'deltaStamp'], dConfigParam = 'teleport')(__requestTutorial)

    def __handleStartTutorial(self, avId, zoneId):
        pass # TODO

    def isShardInterestOpen(self):
        return False # TODO: When should this return true? :(