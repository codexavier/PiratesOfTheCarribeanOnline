# 2014.05.21 01:52:02 Central Daylight Time
#Embedded file name: otp\level\EntityCreatorAI.py
import EntityCreatorBase
import LogicGate
import EditMgrAI
import LevelMgrAI
import ZoneEntityAI
from direct.showbase.PythonUtil import Functor

def createDistributedEntity(AIclass, level, entId, zoneId):
    ent = AIclass(level, entId)
    ent.generateWithRequired(zoneId)
    return ent


def createLocalEntity(AIclass, level, entId, zoneId):
    ent = AIclass(level, entId)
    return ent


def nothing(*args):
    return 'nothing'


class EntityCreatorAI(EntityCreatorBase.EntityCreatorBase):

    def __init__(self, level):
        EntityCreatorBase.EntityCreatorBase.__init__(self, level)
        cLE = createLocalEntity
        self.privRegisterTypes({'attribModifier': nothing,
         'ambientSound': nothing,
         'collisionSolid': nothing,
         'cutScene': nothing,
         'editMgr': Functor(cLE, EditMgrAI.EditMgrAI),
         'entityGroup': nothing,
         'entrancePoint': nothing,
         'levelMgr': Functor(cLE, LevelMgrAI.LevelMgrAI),
         'locator': nothing,
         'logicGate': Functor(cLE, LogicGate.LogicGate),
         'model': nothing,
         'nodepath': nothing,
         'path': nothing,
         'propSpinner': nothing,
         'visibilityExtender': nothing,
         'zone': Functor(cLE, ZoneEntityAI.ZoneEntityAI)})

    def doCreateEntity(self, ctor, entId):
        zoneId = self.level.getEntityZoneId(entId)
        self.notify.debug('creating entity %s in zone %s' % (entId, zoneId))
        return ctor(self.level, entId, zoneId)
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\level\EntityCreatorAI.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:02 Central Daylight Time
