# 2014.05.21 01:52:07 Central Daylight Time
#Embedded file name: otp\level\ZoneEntityAI.py
import ZoneEntityBase

class ZoneEntityAI(ZoneEntityBase.ZoneEntityBase):

    def __init__(self, level, entId):
        ZoneEntityBase.ZoneEntityBase.__init__(self, level, entId)
        self.setZoneId(self.level.air.allocateZone())

    def destroy(self):
        if not self.isUberZone():
            self.level.air.deallocateZone(self.getZoneId())
        ZoneEntityBase.ZoneEntityBase.destroy(self)
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\level\ZoneEntityAI.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:07 Central Daylight Time
