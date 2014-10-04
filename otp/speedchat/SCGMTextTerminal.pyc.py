# 2014.05.21 01:52:21 Central Daylight Time
#Embedded file name: otp\speedchat\SCGMTextTerminal.py
from SCTerminal import SCTerminal
from otp.speedchat import SpeedChatGMHandler
SCGMTextMsgEvent = 'SCGMTextMsg'

class SCGMTextTerminal(SCTerminal):

    def __init__(self, textId):
        SCTerminal.__init__(self)
        gmHandler = SpeedChatGMHandler.SpeedChatGMHandler()
        self.textId = textId
        self.text = gmHandler.getPhrase(textId)

    def handleSelect(self):
        SCTerminal.handleSelect(self)
        messenger.send(self.getEventName(SCGMTextMsgEvent), [self.textId])
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\speedchat\SCGMTextTerminal.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:21 Central Daylight Time
