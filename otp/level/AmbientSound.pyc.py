# 2014.05.21 01:51:57 Central Daylight Time
#Embedded file name: otp\level\AmbientSound.py
from direct.interval.IntervalGlobal import *
import BasicEntities
import random

class AmbientSound(BasicEntities.NodePathEntity):

    def __init__(self, level, entId):
        BasicEntities.NodePathEntity.__init__(self, level, entId)
        self.initSound()

    def destroy(self):
        self.destroySound()
        BasicEntities.NodePathEntity.destroy(self)

    def initSound(self):
        if not self.enabled:
            return
        if self.soundPath == '':
            return
        self.sound = base.loadSfx(self.soundPath)
        if self.sound is None:
            return
        self.soundIval = SoundInterval(self.sound, node=self, volume=self.volume)
        self.soundIval.loop()
        self.soundIval.setT(random.random() * self.sound.length())

    def destroySound(self):
        if hasattr(self, 'soundIval'):
            self.soundIval.pause()
            del self.soundIval
        if hasattr(self, 'sound'):
            del self.sound

    if __dev__:

        def attribChanged(self, *args):
            self.destroySound()
            self.initSound()
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\level\AmbientSound.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:58 Central Daylight Time
