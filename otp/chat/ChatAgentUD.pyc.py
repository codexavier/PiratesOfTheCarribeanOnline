# 2014.05.21 01:51:41 Central Daylight Time
#Embedded file name: otp\chat\ChatAgentUD.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from toontown.chat.TTWhiteList import TTWhiteList

class ChatAgentUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('ChatAgentUD')

    def announceGenerate(self):
        DistributedObjectGlobalUD.announceGenerate(self)
        self.whiteList = TTWhiteList()

    def chatMessage(self, message):
        sender = self.air.getAvatarIdFromSender()
        if sender == 0:
            self.air.writeServerEvent('suspicious', self.air.getAccountIdFromSender(), 'Account sent chat without an avatar', message)
            return
        modifications = []
        words = message.split(' ')
        offset = 0
        WantWhitelist = self.air.config.GetBool('want-whitelist', True)
        for word in words:
            if word and not self.whiteList.isWord(word) and WantWhitelist:
                modifications.append((offset, offset + len(word) - 1))
            offset += len(word) + 1

        cleanMessage = message
        for modStart, modStop in modifications:
            cleanMessage = cleanMessage[:modStart] + '*' * (modStop - modStart + 1) + cleanMessage[modStop + 1:]

        self.air.writeServerEvent('chat-said', sender, message, cleanMessage)
        DistributedAvatar = self.air.dclassesByName['DistributedAvatarUD']
        dg = DistributedAvatar.aiFormatUpdate('setTalk', sender, sender, self.air.ourChannel, [0,
         0,
         '',
         cleanMessage,
         modifications,
         0])
        self.air.send(dg)
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\chat\ChatAgentUD.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:41 Central Daylight Time
