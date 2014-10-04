# 2014.05.21 01:52:25 Central Daylight Time
#Embedded file name: otp\uberdog\OtpAvatarManagerUD.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class OtpAvatarManagerUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('OtpAvatarManagerUD')

    def online(self):
        pass

    def requestAvatarList(self, todo0):
        pass

    def rejectAvatarList(self, todo0):
        pass

    def avatarListResponse(self, todo0):
        pass

    def requestAvatarSlot(self, todo0, todo1, todo2):
        pass

    def rejectAvatarSlot(self, todo0, todo1, todo2):
        pass

    def avatarSlotResponse(self, todo0, todo1):
        pass

    def requestPlayAvatar(self, todo0, todo1, todo2):
        pass

    def rejectPlayAvatar(self, todo0, todo1):
        pass

    def playAvatarResponse(self, todo0, todo1, todo2, todo3):
        pass

    def rejectCreateAvatar(self, todo0):
        pass

    def createAvatarResponse(self, todo0, todo1, todo2, todo3):
        pass

    def requestRemoveAvatar(self, todo0, todo1, todo2, todo3):
        pass

    def rejectRemoveAvatar(self, todo0):
        pass

    def removeAvatarResponse(self, todo0, todo1):
        pass

    def requestShareAvatar(self, todo0, todo1, todo2, todo3):
        pass

    def rejectShareAvatar(self, todo0):
        pass

    def shareAvatarResponse(self, todo0, todo1, todo2):
        pass
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\uberdog\OtpAvatarManagerUD.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:25 Central Daylight Time
