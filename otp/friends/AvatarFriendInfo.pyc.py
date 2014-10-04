# 2014.05.21 01:51:51 Central Daylight Time
#Embedded file name: otp\friends\AvatarFriendInfo.py
from otp.avatar.AvatarHandle import AvatarHandle

class AvatarFriendInfo(AvatarHandle):

    def __init__(self, avatarName = '', playerName = '', playerId = 0, onlineYesNo = 0, openChatEnabledYesNo = 0, openChatFriendshipYesNo = 0, wlChatEnabledYesNo = 0):
        self.avatarName = avatarName
        self.playerName = playerName
        self.playerId = playerId
        self.onlineYesNo = onlineYesNo
        self.openChatEnabledYesNo = openChatEnabledYesNo
        self.openChatFriendshipYesNo = openChatFriendshipYesNo
        self.wlChatEnabledYesNo = wlChatEnabledYesNo
        self.understandableYesNo = self.isUnderstandable()

    def calcUnderstandableYesNo(self):
        self.understandableYesNo = self.isUnderstandable()

    def getName(self):
        if self.avatarName:
            return self.avatarName
        elif self.playerName:
            return self.playerName
        else:
            return ''

    def isUnderstandable(self):
        result = False
        try:
            if self.openChatFriendshipYesNo:
                result = True
            elif self.openChatEnabledYesNo and base.cr.openChatEnabled:
                result = True
            elif self.wlChatEnabledYesNo and base.cr.whiteListChatEnabled:
                result = True
        except:
            pass

        return result

    def isOnline(self):
        return self.onlineYesNo
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\friends\AvatarFriendInfo.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:51 Central Daylight Time
