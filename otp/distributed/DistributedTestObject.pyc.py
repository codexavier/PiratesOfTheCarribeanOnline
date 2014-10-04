# 2014.05.21 01:51:47 Central Daylight Time
#Embedded file name: otp\distributed\DistributedTestObject.py
from direct.distributed import DistributedObject

class DistributedTestObject(DistributedObject.DistributedObject):

    def setRequiredField(self, r):
        self.requiredField = r

    def setB(self, B):
        self.B = B

    def setBA(self, BA):
        self.BA = BA

    def setBO(self, BO):
        self.BO = BO

    def setBR(self, BR):
        self.BR = BR

    def setBRA(self, BRA):
        self.BRA = BRA

    def setBRO(self, BRO):
        self.BRO = BRO

    def setBROA(self, BROA):
        self.BROA = BROA

    def gotNonReqThatWasntSet(self):
        for field in ('B', 'BA', 'BO', 'BR', 'BRA', 'BRO', 'BROA'):
            if hasattr(self, field):
                return True

        return False
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\distributed\DistributedTestObject.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:47 Central Daylight Time
