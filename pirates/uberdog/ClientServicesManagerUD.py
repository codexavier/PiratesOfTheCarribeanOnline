from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.PyDatagram import *


class ClientServicesManagerUD(DistributedObjectGlobalUD):
    notify = directNotify.newCategory('ClientServicesManagerUD')

    def login(self, cookie):
        print 'Got a login!'
        print cookie

        pdg = PyDatagram()
        pdg.addServerHeader(self.air.getMsgSender(), self.air.ourChannel, 3110)
        pdg.addUint16(2)
        self.air.send(pdg)

        self.sendUpdateToChannel(self.air.getMsgSender(), 'acceptLogin', [])