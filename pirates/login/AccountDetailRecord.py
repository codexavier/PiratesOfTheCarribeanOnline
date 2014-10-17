from pirates.piratesbase import PiratesGlobals


class SubDetails:
    def __init__(self):
        self.subAccess = PiratesGlobals.AccessFull
        self.subName = 'developer'


class AccountDetailRecord:
    def __init__(self):
        self.WLChatEnabled = False
        self.playerAccountId = PiratesGlobals.PiratesSubId
        self.playerName = 'developer'
        self.subDetails = {self.playerAccountId: SubDetails()}

    def canOpenChatAndNotGetBooted(self):
        return True