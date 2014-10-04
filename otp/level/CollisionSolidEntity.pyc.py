# 2014.05.21 01:51:58 Central Daylight Time
#Embedded file name: otp\level\CollisionSolidEntity.py
from pandac.PandaModules import *
from otp.otpbase import OTPGlobals
from direct.directnotify import DirectNotifyGlobal
import BasicEntities

class CollisionSolidEntity(BasicEntities.NodePathEntity):
    notify = DirectNotifyGlobal.directNotify.newCategory('CollisionSolidEntity')

    def __init__(self, level, entId):
        self.collNodePath = None
        BasicEntities.NodePathEntity.__init__(self, level, entId)
        self.initSolid()

    def destroy(self):
        self.destroySolid()
        BasicEntities.NodePathEntity.destroy(self)

    def initSolid(self):
        self.destroySolid()
        if self.solidType == 'sphere':
            solid = CollisionSphere(0, 0, 0, self.radius)
        else:
            solid = CollisionTube(0, 0, 0, 0, 0, self.length, self.radius)
        node = CollisionNode(self.getUniqueName(self.__class__.__name__))
        node.addSolid(solid)
        node.setCollideMask(OTPGlobals.WallBitmask)
        self.collNodePath = self.attachNewNode(node)
        if __dev__:
            if self.showSolid:
                self.showCS()
            else:
                self.hideCS()

    def destroySolid(self):
        if self.collNodePath is not None:
            self.collNodePath.removeNode()
            self.collNodePath = None

    if __dev__:

        def attribChanged(self, attrib, value):
            print 'attribChanged'
            self.initSolid()
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\level\CollisionSolidEntity.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:58 Central Daylight Time
