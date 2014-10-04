# 2014.05.21 01:51:41 Central Daylight Time
#Embedded file name: otp\chat\ChatAgent.py
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from pandac.PandaModules import *
from otp.otpbase import OTPGlobals

class ChatAgent(DistributedObjectGlobal):

    def __init__(self, cr):
        DistributedObjectGlobal.__init__(self, cr)

    def delete(self):
        self.ignoreAll()
        self.cr.chatManager = None
        DistributedObjectGlobal.delete(self)

    def adminChat(self, aboutId, message):
        self.notify.warning('Admin Chat(%s): %s' % (aboutId, message))
        messenger.send('adminChat', [aboutId, message])

    def sendChatMessage(self, message):
        self.sendUpdate('chatMessage', [message])
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\chat\ChatAgent.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:41 Central Daylight Time
