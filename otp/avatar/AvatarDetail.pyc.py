# 2014.05.21 01:51:34 Central Daylight Time
#Embedded file name: otp\avatar\AvatarDetail.py
from direct.directnotify.DirectNotifyGlobal import directNotify
from otp.avatar import Avatar

class AvatarDetail:
    notify = directNotify.newCategory('AvatarDetail')

    def __init__(self, doId, callWhenDone):
        self.id = doId
        self.callWhenDone = callWhenDone
        self.enterQuery()

    def isReady(self):
        return true

    def getId(self):
        return self.id

    def enterQuery(self):
        self.avatar = base.cr.doId2do.get(self.id)
        if self.avatar != None and not self.avatar.ghostMode:
            self.createdAvatar = 0
            dclass = self.getDClass()
            self.__handleResponse(True, self.avatar, dclass)
        else:
            self.avatar = self.createHolder()
            self.createdAvatar = 1
            self.avatar.doId = self.id
            dclass = self.getDClass()
            base.cr.getAvatarDetails(self.avatar, self.__handleResponse, dclass)

    def exitQuery(self):
        return true

    def createHolder(self):
        pass

    def getDClass(self):
        pass

    def __handleResponse(self, gotData, avatar, dclass):
        if avatar != self.avatar:
            self.notify.warning('Ignoring unexpected request for avatar %s' % avatar.doId)
            return
        if gotData:
            self.callWhenDone(self.avatar)
            del self.callWhenDone
        else:
            self.callWhenDone(None)
            del self.callWhenDone
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\avatar\AvatarDetail.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:34 Central Daylight Time
