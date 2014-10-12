from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.PyDatagram import *


class ClientServicesManagerUD(DistributedObjectGlobalUD):
    notify = directNotify.newCategory('ClientServicesManagerUD')

    def login(self, cookie):
        self.target = self.air.getMsgSender()

        datagram = PyDatagram()
        datagram.addServerHeader(
            self.target,
            self.air.ourChannel,
            CLIENTAGENT_SET_STATE)
        datagram.addUint16(2)
        self.air.send(datagram)

        self.sendUpdateToChannel(self.target, 'acceptLogin', [])