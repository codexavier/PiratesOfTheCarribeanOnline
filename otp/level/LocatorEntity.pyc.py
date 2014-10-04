# 2014.05.21 01:52:05 Central Daylight Time
#Embedded file name: otp\level\LocatorEntity.py
import Entity, BasicEntities
from pandac.PandaModules import NodePath
from direct.directnotify import DirectNotifyGlobal

class LocatorEntity(Entity.Entity, NodePath):
    notify = DirectNotifyGlobal.directNotify.newCategory('LocatorEntity')

    def __init__(self, level, entId):
        node = hidden.attachNewNode('LocatorEntity-%s' % entId)
        NodePath.__init__(self, node)
        Entity.Entity.__init__(self, level, entId)
        self.doReparent()

    def destroy(self):
        Entity.Entity.destroy(self)
        self.removeNode()

    def getNodePath(self):
        return self

    def doReparent(self):
        if self.searchPath != '':
            parent = self.level.geom.find(self.searchPath)
            if parent.isEmpty():
                LocatorEntity.notify.warning("could not find '%s'" % self.searchPath)
                self.reparentTo(hidden)
            else:
                self.reparentTo(parent)

    if __dev__:

        def attribChanged(self, attrib, value):
            self.doReparent()
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\level\LocatorEntity.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:05 Central Daylight Time
