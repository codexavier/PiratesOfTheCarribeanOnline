from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.PyDatagram import *


class ClientServicesManagerUD(DistributedObjectGlobalUD):
    notify = directNotify.newCategory('ClientServicesManagerUD')

    def login(self, cookie):
        target = self.air.getMsgSender()

        datagram = PyDatagram()
        datagram.addServerHeader(
            target,
            self.air.ourChannel,
            CLIENTAGENT_SET_STATE)
        datagram.addUint16(2)
        self.air.send(datagram)

        self.sendUpdateToChannel(target, 'acceptLogin', [])

    def requestAvatars(self):
        target = self.air.getMsgSender()
        avs = []
        self.sendUpdateToChannel(target, 'setAvatars', [avs])

    def createAvatar(self, avDNA, index):
        target = self.air.getMsgSender()
        self.sendUpdateToChannel(target, 'createAvatarResp', [69])

    def chooseAvatar(self, avId):
        target = self.air.getMsgSender()
        self.sendUpdateToChannel(target, 'avatarResponse', [avId, ''])