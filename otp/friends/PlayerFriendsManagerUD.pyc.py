# 2014.05.21 01:51:55 Central Daylight Time
#Embedded file name: otp\friends\PlayerFriendsManagerUD.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class PlayerFriendsManagerUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('PlayerFriendsManagerUD')

    def requestInvite(self, todo0, todo1, todo2):
        pass

    def invitationFrom(self, todo0, todo1):
        pass

    def retractInvite(self, todo0):
        pass

    def invitationResponse(self, todo0, todo1, todo2):
        pass

    def requestDecline(self, todo0, todo1):
        pass

    def requestDeclineWithReason(self, todo0, todo1, todo2):
        pass

    def requestRemove(self, todo0, todo1):
        pass

    def secretResponse(self, todo0):
        pass

    def rejectSecret(self, todo0):
        pass

    def rejectUseSecret(self, todo0):
        pass

    def updatePlayerFriend(self, todo0, todo1, todo2):
        pass

    def removePlayerFriend(self, todo0):
        pass
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\friends\PlayerFriendsManagerUD.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:55 Central Daylight Time
