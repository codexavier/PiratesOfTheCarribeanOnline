# 2014.05.21 01:52:19 Central Daylight Time
#Embedded file name: otp\speedchat\SCCustomMenu.py
from SCMenu import SCMenu
from SCCustomTerminal import SCCustomTerminal
from otp.otpbase.OTPLocalizer import CustomSCStrings

class SCCustomMenu(SCMenu):

    def __init__(self):
        SCMenu.__init__(self)
        self.accept('customMessagesChanged', self.__customMessagesChanged)
        self.__customMessagesChanged()

    def destroy(self):
        SCMenu.destroy(self)

    def __customMessagesChanged(self):
        self.clearMenu()
        try:
            lt = base.localAvatar
        except:
            return

        for msgIndex in lt.customMessages:
            if CustomSCStrings.has_key(msgIndex):
                self.append(SCCustomTerminal(msgIndex))
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\speedchat\SCCustomMenu.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:19 Central Daylight Time
