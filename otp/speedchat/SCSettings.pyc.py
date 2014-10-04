# 2014.05.21 01:52:22 Central Daylight Time
#Embedded file name: otp\speedchat\SCSettings.py
from SCColorScheme import SCColorScheme
from otp.otpbase import OTPLocalizer

class SCSettings:

    def __init__(self, eventPrefix, whisperMode = 0, colorScheme = None, submenuOverlap = OTPLocalizer.SCOsubmenuOverlap, topLevelOverlap = None):
        self.eventPrefix = eventPrefix
        self.whisperMode = whisperMode
        if colorScheme is None:
            colorScheme = SCColorScheme()
        self.colorScheme = colorScheme
        self.submenuOverlap = submenuOverlap
        self.topLevelOverlap = topLevelOverlap
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\speedchat\SCSettings.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:22 Central Daylight Time
