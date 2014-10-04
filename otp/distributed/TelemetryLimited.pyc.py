# 2014.05.21 01:51:50 Central Daylight Time
#Embedded file name: otp\distributed\TelemetryLimited.py


class TelemetryLimited:
    Sng = SerialNumGen()

    def __init__(self):
        self._telemetryLimiterId = self.Sng.next()
        self._limits = set()

    def getTelemetryLimiterId(self):
        return self._telemetryLimiterId

    def addTelemetryLimit(self, limit):
        self._limits.add(limit)

    def removeTelemetryLimit(self, limit):
        if limit in self._limits:
            self._limits.remove(limit)

    def enforceTelemetryLimits(self):
        for limit in self._limits:
            limit(self)
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\distributed\TelemetryLimited.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:50 Central Daylight Time
