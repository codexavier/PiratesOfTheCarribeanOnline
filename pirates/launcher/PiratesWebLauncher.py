# File: P (Python 2.4)

from otp.launcher.WebLauncherBase import WebLauncherBase
from pirates.piratesbase import PLocalizer

class PiratesWebLauncher(WebLauncherBase):
    GameName = 'Pirates'
    LauncherPhases = [
        (2, 'potco_2'),
        (3, 'potco_3'),
        (4, 'potco_4'),
        (5, 'potco_5')]
    Localizer = PLocalizer
    
    def __init__(self, appRunner):
        WebLauncherBase.__init__(self, appRunner)
        self.startDownload()
        PiratesStart = PiratesStart
        import pirates.piratesbase

    
    def getAccountServer(self):
        pass

    
    def getNeedPwForSecretKey(self):
        return 0

    
    def getParentPasswordSet(self):
        return 0

    
    def canLeaveFirstIsland(self):
        return self.getPhaseComplete(4)


