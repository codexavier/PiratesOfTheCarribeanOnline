# 2014.05.21 01:52:20 Central Daylight Time
#Embedded file name: otp\speedchat\SCCustomTerminal.py
from SCTerminal import SCTerminal
from otp.otpbase.OTPLocalizer import CustomSCStrings
SCCustomMsgEvent = 'SCCustomMsg'

def decodeSCCustomMsg(textId):
    return CustomSCStrings.get(textId, None)


class SCCustomTerminal(SCTerminal):

    def __init__(self, textId):
        SCTerminal.__init__(self)
        self.textId = textId
        self.text = CustomSCStrings[self.textId]

    def handleSelect(self):
        SCTerminal.handleSelect(self)
        messenger.send(self.getEventName(SCCustomMsgEvent), [self.textId])
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\speedchat\SCCustomTerminal.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:20 Central Daylight Time
