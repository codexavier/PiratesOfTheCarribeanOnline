# 2014.05.21 01:52:20 Central Daylight Time
#Embedded file name: otp\speedchat\SCEmoteMenu.py
from SCMenu import SCMenu
from SCEmoteTerminal import SCEmoteTerminal

class SCEmoteMenu(SCMenu):

    def __init__(self):
        SCMenu.__init__(self)
        self.accept('emotesChanged', self.__emoteAccessChanged)
        self.__emoteAccessChanged()

    def destroy(self):
        SCMenu.destroy(self)

    def __emoteAccessChanged(self):
        self.clearMenu()
        try:
            lt = base.localAvatar
        except:
            return

        for i in range(len(lt.emoteAccess)):
            if lt.emoteAccess[i]:
                self.append(SCEmoteTerminal(i))
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\speedchat\SCEmoteMenu.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:20 Central Daylight Time
