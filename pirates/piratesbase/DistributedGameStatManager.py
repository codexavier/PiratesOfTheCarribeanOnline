# File: D (Python 2.4)

from direct.distributed.DistributedObject import DistributedObject
from GameStatManagerBase import GameStatManagerBase

class DistributedGameStatManager(DistributedObject, GameStatManagerBase):
    from direct.directnotify import DirectNotifyGlobal
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGameStatManager')
    
    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        GameStatManagerBase.__init__(self)
        self.aggroModelIndex = None

    
    def generate(self):
        self.cr.gameStatManager = self
        DistributedObject.generate(self)

    
    def announceGenerate(self):
        DistributedObject.announceGenerate(self)

    
    def disable(self):
        GameStatManagerBase.disable(self)
        DistributedObject.disable(self)
        self.ignoreAll()
        if self.cr.gameStatManager == self:
            self.cr.gameStatManager = None
        

    
    def delete(self):
        GameStatManagerBase.delete(self)
        DistributedObject.delete(self)

    
    def setAggroModelIndex(self, modelIndex):
        self.aggroModelIndex = modelIndex
        messenger.send('SwitchAgrroModel')

    
    def getAggroModelIndex(self):
        return self.aggroModelIndex


