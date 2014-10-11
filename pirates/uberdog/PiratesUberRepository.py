from pirates.distributed.PiratesInternalRepository import PiratesInternalRepository
from direct.distributed.PyDatagram import *
from otp.distributed.DistributedDirectoryAI import DistributedDirectoryAI
from otp.distributed.OtpDoGlobals import *

class PiratesUberRepository(PiratesInternalRepository):
    def __init__(self, baseChannel, serverId):
        PiratesInternalRepository.__init__(self, baseChannel, serverId, dcSuffix='UD')

        self.notify.setInfo(True)

    def handleConnected(self):
        rootObj = DistributedDirectoryAI(self)
        rootObj.generateWithRequiredAndId(self.getGameDoId(), 0, 0)

        self.createGlobals()
        self.notify.info('Done.')

    def createGlobals(self):
        self.csm = simbase.air.generateGlobalObject(OTP_DO_ID_CLIENT_SERVICES_MANAGER,
                                                    'ClientServicesManager')