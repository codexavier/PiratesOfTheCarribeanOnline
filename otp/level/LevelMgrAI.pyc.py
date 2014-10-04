# 2014.05.21 01:52:04 Central Daylight Time
#Embedded file name: otp\level\LevelMgrAI.py
from direct.showbase.PythonUtil import Functor
import LevelMgrBase

class LevelMgrAI(LevelMgrBase.LevelMgrBase):

    def __init__(self, level, entId):
        LevelMgrBase.LevelMgrBase.__init__(self, level, entId)
        self.level.zoneNum2zoneId = {}
        self.level.zoneIds = []
        self.accept(self.level.getEntityOfTypeCreateEvent('zone'), self.handleZoneCreated)

    def destroy(self):
        del self.level.zoneIds
        del self.level.zoneNum2zoneId
        LevelMgrBase.LevelMgrBase.destroy(self)

    def handleZoneCreated(self, entId):
        zoneEnt = self.level.getEntity(entId)
        self.level.zoneNum2zoneId[zoneEnt.entId] = zoneEnt.getZoneId()
        self.privCreateSortedZoneIdList()
        self.accept(self.level.getEntityDestroyEvent(entId), Functor(self.handleZoneDestroy, entId))

    def handleZoneDestroy(self, entId):
        zoneEnt = self.level.getEntity(entId)
        del self.level.zoneNum2zoneId[zoneEnt.entId]
        self.privCreateSortedZoneIdList()

    def privCreateSortedZoneIdList(self):
        zoneNums = self.level.zoneNum2zoneId.keys()
        zoneNums.sort()
        self.level.zoneIds = []
        for zoneNum in zoneNums:
            self.level.zoneIds.append(self.level.zoneNum2zoneId[zoneNum])
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\level\LevelMgrAI.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:04 Central Daylight Time
