# File: S (Python 2.4)

global launcher
from pirates.launcher.PiratesWebLauncher import PiratesWebLauncher
from otp.launcher.ExploreDirectory import exploreDirectory
launcher = None

def main(appRunner = None):
    global launcher
    if not appRunner:
        print 'Not running in a web environment; using dummyAppRunner.'
        dummyAppRunner = dummyAppRunner
        import direct.p3d.AppRunner
        PandaSystem = PandaSystem
        import pandac.PandaModules
        appRunner = dummyAppRunner()
        version = PandaSystem.getPackageVersionString()
        hostUrl = PandaSystem.getPackageHostUrl()
        appRunner.addPackageInfo('potco_WL', None, None, hostUrl)
        appRunner.addPackageInfo('potco_2', None, None, hostUrl)
    
    if int(appRunner.tokenDict.get('download', '0')):
        print 'Download token set; not running launcher.'
        import sys as sys
        sys.exit(0)
    
    exploreDirectory(appRunner)
    launcher = PiratesWebLauncher(appRunner)
    print 'Reached end of StartPiratesWebLauncher.py.'

