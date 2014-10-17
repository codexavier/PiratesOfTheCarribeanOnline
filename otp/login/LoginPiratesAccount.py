from pandac.PandaModules import *
from direct.distributed.MsgTypes import *
from direct.directnotify.DirectNotifyGlobal import directNotify
from LoginBase import LoginBase


class LoginPiratesAccount(LoginBase):
    notify = directNotify.newCategory('LoginPiratesAccount')

    def __init__(self, cr):
        LoginBase.__init__(self, cr)

    def supportsRelogin(self):
        if __debug__:
            return 1
        return 0

    def authorize(self, username, password):
        return 0 # No error!

    def sendLoginMsg(self):
        cr = self.cr
        # TODO

    def resendLoginCookie(self):
        self.notify.error('Cannot resend login cookie!')

    def getErrorCode(self):
        return 0

    def needToSetParentPassword(self):
        return 0

    def authenticateParentPassword(self, loginName, password, parentPassword):
        self.notify.error('authenticateParentPassword called')

    def authenticateDelete(self, loginName, password):
        return 1
