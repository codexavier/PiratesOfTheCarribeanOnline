# 2014.05.21 01:51:46 Central Daylight Time
#Embedded file name: otp\distributed\DistributedDistrict.py
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObject import DistributedObject

class DistributedDistrict(DistributedObject):
    notify = directNotify.newCategory('DistributedDistrict')
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self.name = 'NotGiven'
        self.available = 0
        self.avatarCount = 0
        self.newAvatarCount = 0

    def announceGenerate(self):
        DistributedObject.announceGenerate(self)
        self.cr.activeDistrictMap[self.doId] = self
        messenger.send('shardInfoUpdated')

    def delete(self):
        if base.cr.distributedDistrict is self:
            base.cr.distributedDistrict = None
        if self.cr.activeDistrictMap.has_key(self.doId):
            del self.cr.activeDistrictMap[self.doId]
        DistributedObject.delete(self)
        messenger.send('shardInfoUpdated')

    def setAvailable(self, available):
        self.available = available
        messenger.send('shardInfoUpdated')

    def setName(self, name):
        self.name = name
        messenger.send('shardInfoUpdated')
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\distributed\DistributedDistrict.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:46 Central Daylight Time
