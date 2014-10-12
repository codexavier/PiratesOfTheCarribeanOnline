from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.PythonUtil import DelayedCall, makeList
from direct.showbase.DirectObject import DirectObject
from pirates.pirate import AvatarTypes
from pirates.cutscene import CutsceneData, CutsceneActor, CutsceneIvals
from pirates.effects.CameraShaker import CameraShaker
from direct.gui.DirectGui import *
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesbase import TimeOfDayManager, TODGlobals
from direct.task import Task


class Cutscene(NodePath, DirectObject):
    notify = directNotify.newCategory('Cutscene')

    def __init__(self, cr, cutsceneName, doneCallback, giverId):
        self.__destoryed = False
        self.cr = cr
        self.__serial = serialNum()
        self.__ival = None
        self.__data = CutsceneData.CutsceneData[cutsceneName]
        NodePath.__init__(self, 'Cutscene(%s)' % self.getName())
        self.cutsceneName = cutsceneName
        self.showTimer = False
        self.timerStartTime = 0
        self.timerTotalPauseTime = 0
        self.timerPauseTime = 0
        self.allowSkip = True
        self.initialize(doneCallback, giverId)
        self.__loadActors()
        self.__loadSound()
        self.startedCallback = False
        self.setShowTimer(self.showTimer)
        self.delayedStarts = []

    def initialize(self, doneCallback, giverId):
        pass

    def patch(self):
        for actor in self.__actors:
            if actor.Uid:
                actor.handelModelHiding()

    def getEnvEffects(self):
        self.envEffects = None
        if self.cr:
            ga = localAvatar.getParentObj()
            if ga:
                if hasattr(ga, 'envEffects'):
                    self.envEffects = ga.envEffects
                    self.gameArea = ga
        else:
            self.envEffects = base.pe.envEffects

    def getShowTimer(self, showTimer=True):
        if showTimer:
            if not hasattr(self, 'timer'):
                self.timer = DirectLabel(parent=render2d, pos=(0.0, 0.0, 0.9),
                                         frameSize=(0.0, 0.16, 0.0, 0.12),
                                         text='0.0', text_align=TextNode.ARight,
                                         text_scale=0.05, text_pos=(0.149, 0.05),
                                         text_shadow=PiratesGuiGlobals.TextShadow,
                                         textMayChange=True)
        else:
            if hasattr(self, 'timer'):
                self.timer.removeNode()
                del self.timer

    def addFlatWell(self):
        water = None
        if self.cr:
            water = self.cr.activeWorld.getWater()
        if water:
            water.patch.addFlatWell(self.getName(), self, 0, 0, 400, 600)


    def destory(self):
        if self.__destoryed:
            return

        self.__destoryed = True

        if hasattr(self, '__axis'):
            self.__axis.removeNode()
            del self.__axis

        if self.__ival:
            self.__ival.finish()
            base.sfxManagerList[0].stopAllSounds()
        self.__ival = None

        for currDelayedStart in self.delayedStarts:
            currDelayedStart.destory()
        self.delayedStarts = []

        water = None
        if self.cr:
            if self.cr.activeWorld:
                water = self.cr.activeWorld.getWater()
        if water:
            water.patch.removeFlatWell(self.getName())

        self.__unloadActors()
        self.__unloadSound()

        del self.__serial

        self.removeNode()

        if hasattr(self, 'timer'):
            self.timer.removeNode()
            del self.timer

        self.ignore('cutscene-finish')

    def getName(self):
        return '%s-%s' % (self.__data.id, self.__serial)

    def getDoneEvent(self):
        return '%s-done' % self.getName()

    def setCallback(self, callback):
        self.__callback = callback

    def getActor(self, actorKey):
        return self.__actorKey2actor[actorKey]

    def forceOriginNode(self):
        pass

    def __loadActors(self):
        pass

    def __unloadActors(self):
        pass

    def getActor(self):
        pass

    def __loadSound(self):
        pass

    def __unloadSound(self):
        del self.__sounds

    def __startCutscene(self):
        if not base.win.getGsg():
            self.skipNow()
            return

        if self.cr:
            localAvatar.stopCombatMusic()
            base.musicMgr.requestCurMusicFadeOut(1.0, 0.0)

        aspect2d.hide()
        for actor in self.__actors:
            actor.startCutscene(self.__locators)

        CameraShaker.setCutsceneScale(0.1)
        self.acceptOnce('escape', self.__skip)

        if self.startedCallback:
            self.startedCallback()

        render.prepareScene(base.win.getGsg())

    def __skip(self):
        if self.allowSkip:
            self.__ival.finish()
            base.sfxManagerList[0].stopAllSounds()
            messenger.send('cutscene-skipped')
            return
        messenger.send('cutscene-not-skipped')

    def skipNow(self):
        self.ival.finish()
        base.sfxManagerList[0].stopAllSounds()
        messenger.send('cutscene-skipped')

    def __finishCutscene(self):
        if self.cr:
            if base.musicMgr.current:
                vol = base.musicMgr.current.volume
                base.musicMgr.requestCurMusicFadeIn(3.0, vol)

        self.ignore('escape')
        CameraShaker.clearCutsceneScale()

        for actor in self.__actors:
            actor.finishCutscene()

        base.sfxManagerList[0].stopAllSounds()
        aspect2d.show()

        if self.oldTodState:
            if self.cr:
                self.cr.timeOfDayManager.setEnvironment(self.oldTodState)
            else:
                base.pe.changeTimeOfDay()

        messenger.send('cutscene-finish')

    def startTimer(self):
        self.__resetTimer()
        taskMgr.add(self.updateTimer, 'cutsceneTimerUpdate')
        self.acceptOnce('cutscene-finish', self.stopTimer)

    def stopTimer(self):
        taskMgr.remove('cutsceneTimerUpdate')

    def updateTimer(self):
        if self.__ival.isPlaying():
            totalPlayTime = globalClock.getRealTime() - self.timerStartTime - self.timerTotalPauseTime
            self.timer['text'] = '%.2f' % totalPlayTime
        return Task.cont

    def play(self):
        pass

    def isPlaying(self):
        pass

    def __resetTimer(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def restart(self):
        pass

    def overrideOldAvState(self):
        pass

    def setStartCallback(self, callback):
        self.startedCallback = callback
