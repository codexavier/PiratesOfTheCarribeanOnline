# 2014.05.21 01:52:11 Central Daylight Time
#Embedded file name: otp\margins\MarginPopup.py
from pandac.PandaModules import *

class MarginPopup:

    def __init__(self):
        self.__manager = None
        self.__visible = False
        self.__priority = 0
        self._assignedCell = None
        self._lastCell = None

    def setVisible(self, visibility):
        visibility = bool(visibility)
        if self.__visible == visibility:
            return
        self.__visible = visibility
        if self.__manager is not None:
            if visibility:
                self.__manager.addVisiblePopup(self)
            else:
                self.__manager.removeVisiblePopup(self)

    def getPriority(self):
        return self.__priority

    def setPriority(self, priority):
        self.__priority = priority
        if self.__manager is not None:
            self.__manager.reorganize()

    def isDisplayed(self):
        return self._assignedCell is not None

    def marginVisibilityChanged(self):
        pass

    def manage(self, manager):
        self.unmanage(self.__manager)
        self.__manager = manager
        if self.__visible:
            manager.addVisiblePopup(self)

    def unmanage(self, manager):
        if self.__manager is not None:
            if self.__visible:
                self.__manager.removeVisiblePopup(self)
            self.__manager = None
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\margins\MarginPopup.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:11 Central Daylight Time
