# 2014.05.21 01:51:40 Central Daylight Time
#Embedded file name: otp\avatar\PlayerBase.py


class PlayerBase:

    def __init__(self):
        self.gmState = False

    def atLocation(self, locationId):
        return True

    def getLocation(self):
        return []

    def setAsGM(self, state):
        self.gmState = state

    def isGM(self):
        return self.gmState
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\avatar\PlayerBase.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:40 Central Daylight Time
