# 2014.05.21 01:52:06 Central Daylight Time
#Embedded file name: otp\level\VisibilityExtender.py
import Entity

class VisibilityExtender(Entity.Entity):

    def __init__(self, level, entId):
        Entity.Entity.__init__(self, level, entId)
        self.initVisExt()

    def initVisExt(self):
        self.extended = 0
        self.zoneEntId = self.getZoneEntId()
        self.eventName = None
        if self.event is not None:
            self.eventName = self.getOutputEventName(self.event)
            self.accept(self.eventName, self.handleEvent)

    def destroyVisExt(self):
        if self.eventName is not None:
            self.ignore(self.eventName)
        if self.extended:
            self.retract()

    def handleEvent(self, doExtend):
        if doExtend:
            if not self.extended:
                self.extend()
        elif self.extended:
            self.retract()

    def extend(self):
        zoneEnt = self.level.getEntity(self.getZoneEntId())
        zoneEnt.incrementRefCounts(self.newZones)
        self.extended = 1
        self.level.handleVisChange()

    def retract(self):
        zoneEnt = self.level.getEntity(self.getZoneEntId())
        zoneEnt.decrementRefCounts(self.newZones)
        self.extended = 0
        self.level.handleVisChange()

    def destroy(self):
        self.destroyVisExt()
        Entity.Entity.destroy(self)

    if __dev__:

        def setNewZones(self, newZones):
            extended = self.extended
            self.destroyVisExt()
            self.newZones = newZones
            self.initVisExt()
            if extended:
                self.extend()

        def attribChanged(self, *args):
            extended = self.extended
            self.destroyVisExt()
            self.initVisExt()
            if extended:
                self.extend()
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\level\VisibilityExtender.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:06 Central Daylight Time
