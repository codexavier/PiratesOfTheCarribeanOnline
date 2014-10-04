# 2014.05.21 01:51:45 Central Daylight Time
#Embedded file name: otp\distributed\AccountUD.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class AccountUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('AccountUD')
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\distributed\AccountUD.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:45 Central Daylight Time
