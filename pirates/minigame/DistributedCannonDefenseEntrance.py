# File: D (Python 2.4)

from pandac.PandaModules import *
from direct.distributed.DistributedObject import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import *
from pirates.piratesbase import PiratesGlobals
from pirates.piratesbase import PLocalizer
from pirates.piratesgui import PiratesGuiGlobals
from pirates.minigame import CannonDefenseGlobals

class DistributedCannonDefenseEntrance(DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedInteractive')
    
    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self._gameFullTxt = None
        self._gameFullSeq = None

    
    def generate(self):
        DistributedObject.generate(self)

    
    def announceGenerate(self):
        DistributedObject.announceGenerate(self)

    
    def teleport(self):
        base.loadingScreen.showTarget(cannonDefense = True)
        base.cr.loadingScreen.show()


