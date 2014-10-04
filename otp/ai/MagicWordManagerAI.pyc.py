# 2014.05.21 01:51:32 Central Daylight Time
#Embedded file name: otp\ai\MagicWordManagerAI.py
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from otp.ai.MagicWordGlobal import *
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.MsgTypes import *

class MagicWordManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('MagicWordManagerAI')

    def sendMagicWord(self, word, targetId):
        invokerId = self.air.getAvatarIdFromSender()
        invoker = self.air.doId2do.get(invokerId)
        if not invoker:
            self.sendUpdateToAvatarId(invokerId, 'sendMagicWordResponse', ['missing invoker'])
            return
        if invoker.getAdminAccess() < MINIMUM_MAGICWORD_ACCESS:
            self.air.writeServerEvent('suspicious', invokerId, 'Attempted to issue magic word: %s' % word)
            dg = PyDatagram()
            dg.addServerHeader(self.GetPuppetConnectionChannel(invokerId), self.air.ourChannel, CLIENTAGENT_EJECT)
            dg.addUint16(126)
            dg.addString('Magic Words are reserved for administrators only!')
            self.air.send(dg)
            return
        target = self.air.doId2do.get(targetId)
        if not target:
            self.sendUpdateToAvatarId(invokerId, 'sendMagicWordResponse', ['missing target'])
            return
        response = spellbook.process(invoker, target, word)
        if response:
            self.sendUpdateToAvatarId(invokerId, 'sendMagicWordResponse', [response])
        self.air.writeServerEvent('magic-word', invokerId, invoker.getAdminAccess(), targetId, target.getAdminAccess(), word, response)
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\ai\MagicWordManagerAI.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:32 Central Daylight Time
