# 2014.05.21 01:52:04 Central Daylight Time
#Embedded file name: otp\level\LevelMgrBase.py
import Entity

class LevelMgrBase(Entity.Entity):

    def __init__(self, level, entId):
        Entity.Entity.__init__(self, level, entId)

    def destroy(self):
        Entity.Entity.destroy(self)
        self.ignoreAll()
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\level\LevelMgrBase.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:04 Central Daylight Time
