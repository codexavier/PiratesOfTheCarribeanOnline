# 2014.05.21 01:51:59 Central Daylight Time
#Embedded file name: otp\level\DistributedInteractiveEntityAI.py
from direct.directnotify import DirectNotifyGlobal
from otp.level.DistributedEntityAI import DistributedEntityAI

class DistributedInteractiveEntityAI(DistributedEntityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedInteractiveEntityAI')

    def setAvatarInteract(self, todo0):
        pass

    def requestInteract(self):
        pass

    def rejectInteract(self):
        pass

    def requestExit(self):
        pass

    def avatarExit(self, todo0):
        pass

    def setState(self, todo0, todo1):
        pass
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\level\DistributedInteractiveEntityAI.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:59 Central Daylight Time
