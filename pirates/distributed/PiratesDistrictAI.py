from otp.distributed.DistributedDistrictAI import DistributedDistrictAI
from pirates.piratesbase import PiratesGlobals


class PiratesDistrictAI(DistributedDistrictAI):
    parentingRules = ('', '')
    avatarCount = 0
    newAvatarCount = 0
    mainWorld = 'AnvilIsland'
    shardType = PiratesGlobals.SHARD_MAIN
    populationLimits = (1, 50)

    def setParentingRules(self, rule1, rule2):
        self.parentingRules = (rule1, rule2)

    def d_setParentingRules(self, rule1, rule2):
        self.sendUpdate('setParentingRules', [rule1, rule2])

    def b_setParentingRules(self, rule1, rule2):
        self.setParentingRules(rule1, rule2)
        self.d_setParentingRules(rule1, rule2)

    def getParentingRules(self):
        return self.parentingRules

    def setAvatarCount(self, avCount):
        self.avatarCount = avCount

    def d_setAvatarCount(self, avCount):
        self.sendUpdate('setAvatarCount', [avCount])

    def b_setAvatarCount(self, avCount):
        self.setAvatarCount(avCount)
        self.d_setAvatarCount(avCount)

    def getAvatarCount(self):
        return self.avatarCount

    def setNewAvatarCount(self, avCount):
        self.avatarCount = avCount

    def d_setNewAvatarCount(self, avCount):
        self.sendUpdate('setNewAvatarCount', [avCount])

    def b_setNewAvatarCount(self, avCount):
        self.setNewAvatarCount(avCount)
        self.d_setNewAvatarCount(avCount)

    def getNewAvatarCount(self):
        return self.newAvatarCount

    def setMainWorld(self, mainWorld):
        self.mainWorld = mainWorld

    def d_setMainWorld(self, mainWorld):
        self.sendUpdate('setMainWorld', [mainWorld])

    def b_setMainWorld(self, mainWorld):
        self.setMainWorld(mainWorld)
        self.d_setMainWorld(mainWorld)

    def getMainWorld(self):
        return self.mainWorld

    def setShardType(self, shardType):
        self.shardType = shardType

    def d_setShardType(self, shardType):
        self.sendUpdate('setShardType', [shardType])

    def b_setShardType(self, shardType):
        self.setShardType(shardType)
        self.b_setShardType(shardType)

    def getShardType(self):
        return self.shardType

    def setPopulationLimits(self, med, high):
        self.populationLimits = (med, high)

    def d_setPopulationLimits(self, med, high):
        self.sendUpdate('setPopulationLimits', [med, high])

    def b_setPopulationLimits(self, med, high):
        self.setPopulationLimits(med, high)
        self.d_setPopulationLimits(med, high)

    def getPopulationLimits(self):
        return self.populationLimits
