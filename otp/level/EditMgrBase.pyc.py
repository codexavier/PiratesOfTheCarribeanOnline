# 2014.05.21 01:52:01 Central Daylight Time
#Embedded file name: otp\level\EditMgrBase.py
import Entity
from direct.directnotify import DirectNotifyGlobal

class EditMgrBase(Entity.Entity):
    notify = DirectNotifyGlobal.directNotify.newCategory('EditMgr')

    def __init__(self, level, entId):
        Entity.Entity.__init__(self, level, entId)

    def destroy(self):
        Entity.Entity.destroy(self)
        self.ignoreAll()

    if __dev__:

        def setInsertEntity(self, data):
            self.level.setEntityCreatorUsername(data['entId'], data['username'])
            self.level.levelSpec.insertEntity(data['entId'], data['entType'], data['parentEntId'])
            self.level.levelSpec.doSetAttrib(self.entId, 'insertEntity', None)

        def setRemoveEntity(self, data):
            self.level.levelSpec.removeEntity(data['entId'])
            self.level.levelSpec.doSetAttrib(self.entId, 'removeEntity', None)
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\level\EditMgrBase.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:01 Central Daylight Time
