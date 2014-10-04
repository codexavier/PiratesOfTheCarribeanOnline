# 2014.05.21 01:51:45 Central Daylight Time
#Embedded file name: otp\chat\WhiteList.py
from bisect import bisect_left
import string
import sys
import os

class WhiteList:

    def __init__(self, wordlist):
        self.words = []
        for line in wordlist:
            self.words.append(line.strip('\n\r').lower())

        self.words.sort()
        self.numWords = len(self.words)

    def cleanText(self, text):
        text = text.strip('.,?!')
        text = text.lower()
        return text

    def isWord(self, text):
        text = self.cleanText(text)
        i = bisect_left(self.words, text)
        if i == self.numWords:
            return False
        return self.words[i] == text

    def isPrefix(self, text):
        text = self.cleanText(text)
        i = bisect_left(self.words, text)
        if i == self.numWords:
            return False
        return self.words[i].startswith(text)

    def prefixCount(self, text):
        text = self.cleanText(text)
        i = bisect_left(self.words, text)
        j = i
        while j < self.numWords and self.words[j].startswith(text):
            j += 1

        return j - i

    def prefixList(self, text):
        text = self.cleanText(text)
        i = bisect_left(self.words, text)
        j = i
        while j < self.numWords and self.words[j].startswith(text):
            j += 1

        return self.words[i:j]
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\chat\WhiteList.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:51:45 Central Daylight Time
