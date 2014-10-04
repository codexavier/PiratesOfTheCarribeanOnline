# 2014.05.21 01:51:37 Central Daylight Time
#Embedded file name: otp\avatar\Emote.py
from otp.otpbase import OTPLocalizer
import types

class Emote:
    EmoteClear = -1
    EmoteEnableStateChanged = 'EmoteEnableStateChanged'

    def __init__(self):
        self.emoteFunc = None

    def isEnabled(self, index):
        if isinstance(index, types.StringType):
            index = OTPLocalizer.EmoteFuncDict[index]
        if self.emoteFunc == None:
            return 0
        if self.emoteFunc[index][1] == 0:
            return 1
        return 0


globalEmote = None
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\avatar\Emote.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:37 Central Daylight Time
