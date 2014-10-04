# 2014.05.21 01:51:59 Central Daylight Time
#Embedded file name: otp\level\DistributedEntity.py
from direct.distributed import DistributedObject
import Entity
from direct.directnotify import DirectNotifyGlobal

class DistributedEntity(DistributedObject.DistributedObject, Entity.Entity):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedEntity')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        Entity.Entity.__init__(self)
        self.levelDoId = 0
        self.entId = 0
        self.level = None

    def generateInit(self):
        DistributedEntity.notify.debug('generateInit')
        DistributedObject.DistributedObject.generateInit(self)

    def generate(self):
        DistributedEntity.notify.debug('generate')
        DistributedObject.DistributedObject.generate(self)

    def setLevelDoId(self, levelDoId):
        DistributedEntity.notify.debug('setLevelDoId: %s' % levelDoId)
        self.levelDoId = levelDoId

    def setEntId(self, entId):
        DistributedEntity.notify.debug('setEntId: %s' % entId)
        self.entId = entId

    def announceGenerate(self):
        DistributedEntity.notify.debug('announceGenerate (%s)' % self.entId)
        if self.levelDoId != 0:
            level = base.cr.doId2do[self.levelDoId]
            self.initializeEntity(level, self.entId)
            self.level.onEntityCreate(self.entId)
        else:
            self.level = None
        DistributedObject.DistributedObject.announceGenerate(self)

    def disable(self):
        DistributedEntity.notify.debug('disable (%s)' % self.entId)
        self.destroy()
        DistributedObject.DistributedObject.disable(self)

    def delete(self):
        DistributedEntity.notify.debug('delete')
        DistributedObject.DistributedObject.delete(self)
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\level\DistributedEntity.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:59 Central Daylight Time
