# 2014.05.21 01:52:10 Central Daylight Time
#Embedded file name: otp\login\SecretFriendsInfoPanel.py
from pandac.PandaModules import *
from otp.otpbase.OTPGlobals import *
from direct.gui.DirectGui import *
from MultiPageTextFrame import *
from otp.otpbase import OTPLocalizer
from otp.otpgui import OTPDialog

class SecretFriendsInfoPanel(getGlobalDialogClass()):

    def __init__(self, doneEvent, hidePageNum = 0, pageChangeCallback = None):
        dialogClass = getGlobalDialogClass()
        dialogClass.__init__(self, parent=aspect2d, dialogName='secretFriendsInfoDialog', doneEvent=doneEvent, okButtonText=OTPLocalizer.SecretFriendsInfoPanelClose, style=OTPDialog.Acknowledge, text='', topPad=1.5, sidePad=1.2, pos=(0, 0, 0.1), scale=0.9)
        self.textPanel = MultiPageTextFrame(parent=self, textList=OTPLocalizer.SecretFriendsInfoPanelText, hidePageNum=hidePageNum, pageChangeCallback=pageChangeCallback)
        self['image'] = self['image']
        self['image_pos'] = (0, 0, -0.1)
        self['image_scale'] = (2, 1, 1.3)
        closeButton = self.getChild(0)
        closeButton.setZ(-0.56)
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\login\SecretFriendsInfoPanel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:10 Central Daylight Time
