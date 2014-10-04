# 2014.05.21 01:38:05 Central Daylight Time
#Embedded file name: otp\login\AccountServerConstants.py
from pandac.PandaModules import *
from RemoteValueSet import *
from direct.directnotify import DirectNotifyGlobal
import TTAccount
import HTTPUtil

class AccountServerConstants(RemoteValueSet):
    notify = DirectNotifyGlobal.directNotify.newCategory('AccountServerConstants')

    def __init__(self, cr):
        noquery = 1
        if cr.productName == 'DisneyOnline-US':
            if base.config.GetBool('tt-specific-login', 0):
                pass
            else:
                noquery = 0
        if cr.accountOldAuth or base.config.GetBool('default-server-constants', noquery):
            self.notify.debug('setting defaults, not using account server constants')
            self.dict = {}
            for constantName in self.defaults:
                pass

    def getBool(self, name):
        pass

    def getInt(self, name):
        pass

    def getFloat(self, name):
        pass

    def getString(self, name):
        pass

    def __getConstant(self, constantName, accessor):
        pass

    @staticmethod
    def getServer():
        pass

    @staticmethod
    def getServerURL():
        pass
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\otp\login\AccountServerConstants.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:38:06 Central Daylight Time
