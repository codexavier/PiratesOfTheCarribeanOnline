# 2014.05.21 01:52:27 Central Daylight Time
#Embedded file name: otp\web\SettingsMgrAI.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class SettingsMgrAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('SettingsMgrAI')

    def requestAllChangedSettings(self):
        pass

    def settingChange(self, todo0, todo1):
        pass
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\web\SettingsMgrAI.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:27 Central Daylight Time
