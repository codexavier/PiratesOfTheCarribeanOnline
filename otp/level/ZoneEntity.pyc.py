# 2014.05.21 01:52:06 Central Daylight Time
#Embedded file name: otp\level\ZoneEntity.py
import ZoneEntityBase
import BasicEntities

class ZoneEntity(ZoneEntityBase.ZoneEntityBase, BasicEntities.NodePathAttribs):

    def __init__(self, level, entId):
        ZoneEntityBase.ZoneEntityBase.__init__(self, level, entId)
        self.nodePath = self.level.getZoneNode(self.entId)
        if self.nodePath is None:
            if __dev__:
                self.level.reportModelSpecSyncError('unknown zoneNum %s; zone was removed from model?' % self.entId)
            else:
                self.notify.error('zone %s not found in level model' % self.entId)
        BasicEntities.NodePathAttribs.initNodePathAttribs(self, doReparent=0)
        self.visibleZoneNums = {}
        self.incrementRefCounts(self.visibility)

    def destroy(self):
        BasicEntities.NodePathAttribs.destroy(self)
        ZoneEntityBase.ZoneEntityBase.destroy(self)

    def getNodePath(self):
        return self.nodePath

    def getVisibleZoneNums(self):
        return self.visibleZoneNums.keys()

    def incrementRefCounts(self, zoneNumList):
        for zoneNum in zoneNumList:
            self.visibleZoneNums.setdefault(zoneNum, 0)
            self.visibleZoneNums[zoneNum] += 1

    def decrementRefCounts(self, zoneNumList):
        for zoneNum in zoneNumList:
            self.visibleZoneNums[zoneNum] -= 1
            if self.visibleZoneNums[zoneNum] == 0:
                del self.visibleZoneNums[zoneNum]

    if __dev__:

        def setVisibility(self, visibility):
            self.decrementRefCounts(self.visibility)
            self.visibility = visibility
            self.incrementRefCounts(self.visibility)
            self.level.handleVisChange()
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\level\ZoneEntity.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:07 Central Daylight Time
