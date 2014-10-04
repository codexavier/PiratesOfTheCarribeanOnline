# 2014.05.21 01:51:47 Central Daylight Time
#Embedded file name: otp\distributed\DistributedDistrictAI.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedDistrictAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedDistrictAI')
    name = 'District'
    available = 0

    def setName(self, name):
        self.name = name

    def d_setName(self, name):
        self.sendUpdate('setName', [name])

    def b_setName(self, name):
        self.setName(name)
        self.d_setName(name)

    def getName(self):
        return self.name

    def setAvailable(self, available):
        self.available = available

    def d_setAvailable(self, available):
        self.sendUpdate('setAvailable', [available])

    def b_setAvailable(self, available):
        self.setAvailable(available)
        self.d_setAvailable(available)

    def getAvailable(self):
        return self.available
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\distributed\DistributedDistrictAI.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:47 Central Daylight Time
