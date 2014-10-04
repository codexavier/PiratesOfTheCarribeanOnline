# 2014.05.21 01:52:26 Central Daylight Time
#Embedded file name: otp\web\SettingsMgr.py
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.directnotify.DirectNotifyGlobal import directNotify
from otp.web.SettingsMgrBase import SettingsMgrBase

class SettingsMgr(DistributedObjectGlobal, SettingsMgrBase):
    notify = directNotify.newCategory('SettingsMgr')

    def announceGenerate(self):
        DistributedObjectGlobal.announceGenerate(self)
        SettingsMgrBase.announceGenerate(self)
        if not self.cr.isLive():
            self._sracs = None
            if self.cr.isConnected():
                self._scheduleChangedSettingRequest()
            self._crConnectEvent = self.cr.getConnectedEvent()
            self.accept(self._crConnectEvent, self._handleConnected)

    def _handleConnected(self):
        self._scheduleChangedSettingRequest()

    def _scheduleChangedSettingRequest(self):
        if self._sracs:
            self._sracs.destroy()
        self._sracs = FrameDelayedCall('requestAllChangedSettings', self.sendRequestAllChangedSettings)

    def delete(self):
        self.ignore(self._crConnectEvent)
        if self._sracs:
            self._sracs.destroy()
        SettingsMgrBase.delete(self)
        DistributedObjectGlobal.delete(self)

    def sendRequestAllChangedSettings(self):
        self.sendUpdate('requestAllChangedSettings', [])

    def settingChange(self, settingName, valueStr):
        if valueStr == self._getCurrentValueRepr(settingName):
            return
        self.notify.info('got setting change: %s -> %s' % (settingName, valueStr))
        self._changeSetting(settingName, valueStr)
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\web\SettingsMgr.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:26 Central Daylight Time
