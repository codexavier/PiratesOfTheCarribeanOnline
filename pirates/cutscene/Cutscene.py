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
        pass # TODO

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
        pass

    def getDoneEvent(self):
        pass

    def setCallback(self):
        pass

    def getActor(self):
        pass

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
        pass

    def __startCutscene(self):
        pass

    def __skip(self):
        pass

    def skipNow(self):
        pass

    def __finishCutscene(self):
        pass

    def startTimer(self):
        pass

    def stopTimer(self):
        pass

    def updateTimer(self):
        pass

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

    def setStartCallback(self):
        pass
