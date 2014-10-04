# 2014.05.21 01:52:18 Central Daylight Time
#Embedded file name: otp\snapshot\SnapshotDispatcherAI.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class SnapshotDispatcherAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('SnapshotDispatcherAI')

    def online(self):
        pass

    def requestRender(self, todo0):
        pass

    def avatarDeleted(self, todo0):
        pass

    def requestNewWork(self, todo0):
        pass

    def errorFetchingAvatar(self, todo0, todo1):
        pass

    def errorRenderingAvatar(self, todo0, todo1):
        pass

    def renderSuccessful(self, todo0, todo1):
        pass
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\snapshot\SnapshotDispatcherAI.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:18 Central Daylight Time
