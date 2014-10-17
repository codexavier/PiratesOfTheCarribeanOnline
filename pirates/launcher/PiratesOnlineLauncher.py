from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import directNotify
from otp.launcher.LauncherBase import LauncherBase
import os


class PiratesOnlineLauncher(LauncherBase):
    notify = directNotify.newCategory('PiratesOnlineLauncher')

    def __init__(self):
        self.http = HTTPClient()
        # TODO: Logging

    def setPandaErrorCode(self, errorCode):
        pass

    def getLoginCookie(self):
        return self.getValue('LOGIN_COOKIE')

    def getGameServer(self):
        return self.getValue('GAME_SERVER')

    def getValue(self, key, default = None):
        return os.environ.get(key, default)

    def setValue(self, key, value):
        os.environ[key] = str(value)

    def getNeedPwForSecretKey(self):
        return False

    def getParentPasswordSet(self):
        return True

    def getPhaseComplete(self, phase):
        return True