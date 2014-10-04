# 2014.05.21 01:52:06 Central Daylight Time
#Embedded file name: otp\level\VisibilityBlocker.py
import Entity

class VisibilityBlocker:

    def __init__(self):
        self.__nextSetZoneDoneEvent = None

    def destroy(self):
        self.cancelUnblockVis()

    def requestUnblockVis(self):
        if self.__nextSetZoneDoneEvent is None:
            self.__nextSetZoneDoneEvent = self.level.cr.getNextSetZoneDoneEvent()
            self.acceptOnce(self.__nextSetZoneDoneEvent, self.okToUnblockVis)
            self.level.forceSetZoneThisFrame()

    def cancelUnblockVis(self):
        if self.__nextSetZoneDoneEvent is not None:
            self.ignore(self.__nextSetZoneDoneEvent)
            self.__nextSetZoneDoneEvent = None

    def isWaitingForUnblockVis(self):
        return self.__nextSetZoneDoneEvent is not None

    def okToUnblockVis(self):
        self.cancelUnblockVis()
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\level\VisibilityBlocker.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:06 Central Daylight Time
