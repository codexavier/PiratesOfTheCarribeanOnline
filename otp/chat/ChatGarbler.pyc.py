# 2014.05.21 01:51:41 Central Daylight Time
#Embedded file name: otp\chat\ChatGarbler.py
import string
import random
from otp.otpbase import OTPLocalizer

class ChatGarbler:

    def garble(self, avatar, message):
        newMessage = ''
        numWords = random.randint(1, 7)
        wordlist = OTPLocalizer.ChatGarblerDefault
        for i in range(1, numWords + 1):
            wordIndex = random.randint(0, len(wordlist) - 1)
            newMessage = newMessage + wordlist[wordIndex]
            if i < numWords:
                newMessage = newMessage + ' '

        return newMessage

    def garbleSingle(self, avatar, message):
        newMessage = ''
        numWords = 1
        wordlist = OTPLocalizer.ChatGarblerDefault
        for i in range(1, numWords + 1):
            wordIndex = random.randint(0, len(wordlist) - 1)
            newMessage = newMessage + wordlist[wordIndex]
            if i < numWords:
                newMessage = newMessage + ' '

        return newMessage
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\chat\ChatGarbler.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:41 Central Daylight Time
