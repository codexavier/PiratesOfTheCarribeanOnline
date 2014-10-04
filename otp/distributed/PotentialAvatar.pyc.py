# 2014.05.21 01:51:50 Central Daylight Time
#Embedded file name: otp\distributed\PotentialAvatar.py


class PotentialAvatar:

    def __init__(self, id, names, dna, position, allowedName, creator = 1, shared = 1, online = 0, wishState = 'CLOSED', wishName = '', defaultShard = 0, lastLogout = 0):
        self.id = id
        self.name = names[0]
        self.dna = dna
        self.avatarType = None
        self.position = position
        self.wantName = names[1]
        self.approvedName = names[2]
        self.rejectedName = names[3]
        self.allowedName = allowedName
        self.wishState = wishState
        self.wishName = wishName
        self.creator = creator
        self.shared = shared
        self.online = online
        self.defaultShard = defaultShard
        self.lastLogout = lastLogout
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\distributed\PotentialAvatar.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:50 Central Daylight Time
