# 2014.05.21 01:52:07 Central Daylight Time
#Embedded file name: otp\level\ZoneEntityBase.py
import Entity
import LevelConstants

class ZoneEntityBase(Entity.Entity):

    def __init__(self, level, entId):
        Entity.Entity.__init__(self, level, entId)
        self.zoneId = None

    def destroy(self):
        del self.zoneId
        Entity.Entity.destroy(self)

    def isUberZone(self):
        return self.entId == LevelConstants.UberZoneEntId

    def setZoneId(self, zoneId):
        self.zoneId = zoneId

    def getZoneId(self):
        return self.zoneId

    def getZoneNum(self):
        return self.entId
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\level\ZoneEntityBase.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:07 Central Daylight Time
