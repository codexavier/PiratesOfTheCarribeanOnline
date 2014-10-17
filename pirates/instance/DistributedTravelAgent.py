from direct.distributed.DistributedObject import DistributedObject


class DistributedTravelAgent(DistributedObject):
    notify = directNotify.newCategory('DistributedTravelAgent')