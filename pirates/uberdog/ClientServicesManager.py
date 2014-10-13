from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.directnotify.DirectNotifyGlobal import directNotify
from otp.distributed.PotentialAvatar import PotentialAvatar
from pirates.piratesbase import PiratesGlobals


class ClientServicesManager(DistributedObjectGlobal):
    notify = directNotify.newCategory('ClientServicesManager')

    def performLogin(self, doneEvent):
        self.doneEvent = doneEvent

        cookie = self.cr.playToken or 'dev'

        self.sendUpdate('login', [cookie])

    def acceptLogin(self):
        messenger.send(self.doneEvent, [{'mode': 'success'}])

    def requestAvatars(self):
        self.sendUpdate('requestAvatars')

    def setAvatars(self, avatars):  # TODO
        avList = {PiratesGlobals.PiratesSubId: [PiratesGlobals.AvatarSlotAvailable,
                                                PiratesGlobals.AvatarSlotAvailable,
                                                PiratesGlobals.AvatarSlotAvailable,
                                                PiratesGlobals.AvatarSlotAvailable]}
        self.cr.handleAvatarsList(avList)