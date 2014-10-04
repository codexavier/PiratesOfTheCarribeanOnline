# File: D (Python 2.4)

from pirates.audio import SoundGlobals
from pirates.piratesbase import PiratesGlobals
from pirates.ship import ShipGlobals
from pirates.ship.DistributedSimpleShip import DistributedSimpleShip

class DistributedTutorialSimpleShip(DistributedSimpleShip):
    
    def __init__(self, cr):
        DistributedSimpleShip.__init__(self, cr)
        self.interactTube = None

    
    def announceGenerate(self):
        DistributedSimpleShip.announceGenerate(self)
        self.setupBoardingSphere(bitmask = PiratesGlobals.WallBitmask | PiratesGlobals.SelectBitmask | PiratesGlobals.RadarShipBitmask)
        self.addDeckInterest()

    
    def disable(self):
        self.removeBoardingSphere()
        DistributedSimpleShip.disable(self)

    
    def setupBoardingSphere(self, bitmask = PiratesGlobals.RadarShipBitmask):
        self.removeBoardingSphere()
        tubeName = self.uniqueName('proximityCollision')
        result = self.createShipTube(tubeName, bitmask)
        self.interactTube = result[2]
        self.interactTube.setTag('objType', str(PiratesGlobals.COLL_AV))
        self.interactTube.setTag('avId', str(self.doId))
        sphereScale = ShipGlobals.getBoardingSphereScale(self.modelClass)
        spherePosH = ShipGlobals.getBoardingSpherePosH(self.modelClass)
        self.interactTube.setY(spherePosH[0][1])
        self.proximityCollisionEnterEvent = 'enter' + tubeName

    
    def removeBoardingSphere(self):
        if self.interactTube:
            self.interactTube.removeNode()
        

    
    def handleChildArrive(self, child, zoneId):
        DistributedSimpleShip.handleChildArrive(self, child, zoneId)
        if child.isLocal():
            self.gameFSM.stopCurrentMusic()
            self.gameFSM.startCurrentMusic(SoundGlobals.MUSIC_CUBA_COMBAT)
        

    
    def localAvatarExitShip(self, boardingFlagship = 0):
        DistributedSimpleShip.localAvatarExitShip(self, boardingFlagship)
        self.gameFSM.stopCurrentMusic()


