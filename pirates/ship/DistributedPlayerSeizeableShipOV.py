# File: D (Python 2.4)

from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectOV

class DistributedPlayerSeizeableShipOV(DistributedObjectOV.DistributedObjectOV):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPlayerSeizeableShipOV')
    
    def __init__(self, cr):
        DistributedObjectOV.DistributedObjectOV.__init__(self, cr)


