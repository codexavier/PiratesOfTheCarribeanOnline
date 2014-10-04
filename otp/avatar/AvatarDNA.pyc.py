# 2014.05.21 01:51:34 Central Daylight Time
#Embedded file name: otp\avatar\AvatarDNA.py
from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
import random
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
notify = directNotify.newCategory('AvatarDNA')

class AvatarDNA:

    def __str__(self):
        return 'avatar parent class: type undefined'

    def makeNetString(self):
        notify.error('called makeNetString on avatarDNA parent class')

    def printNetString(self):
        string = self.makeNetString()
        dg = PyDatagram(string)
        dg.dumpHex(ostream)

    def makeFromNetString(self, string):
        notify.error('called makeFromNetString on avatarDNA parent class')

    def getType(self):
        notify.error('Invalid DNA type: ', self.type)
        return type
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\avatar\AvatarDNA.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:34 Central Daylight Time
