# 2014.05.21 01:52:22 Central Daylight Time
#Embedded file name: otp\speedchat\SCStaticTextTerminal.py
from SCTerminal import SCTerminal
from otp.otpbase.OTPLocalizer import SpeedChatStaticText
SCStaticTextMsgEvent = 'SCStaticTextMsg'

def decodeSCStaticTextMsg(textId):
    return SpeedChatStaticText.get(textId, None)


class SCStaticTextTerminal(SCTerminal):

    def __init__(self, textId):
        SCTerminal.__init__(self)
        self.textId = textId
        self.text = SpeedChatStaticText[self.textId]

    def handleSelect(self):
        SCTerminal.handleSelect(self)
        messenger.send(self.getEventName(SCStaticTextMsgEvent), [self.textId])
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\speedchat\SCStaticTextTerminal.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:23 Central Daylight Time
