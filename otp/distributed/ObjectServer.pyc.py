# 2014.05.21 01:51:47 Central Daylight Time
#Embedded file name: otp\distributed\ObjectServer.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject

class ObjectServer(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('ObjectServer')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    def setName(self, name):
        self.name = name
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\distributed\ObjectServer.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:47 Central Daylight Time
