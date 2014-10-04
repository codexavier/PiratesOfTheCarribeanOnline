# 2014.05.21 01:52:10 Central Daylight Time
#Embedded file name: otp\margins\MarginManager.py
from pandac.PandaModules import *
from MarginCell import MarginCell
import random

class MarginManager(PandaNode):

    def __init__(self):
        PandaNode.__init__(self, 'margins')
        self.cells = set()
        self.visiblePopups = set()

    def addGridCell(self, x, y, left, right, bottom, top):
        padding = 0.125
        scale = 0.2
        xStart = left + scale / 2.0 + padding
        yStart = bottom + scale / 2.0 + padding
        xEnd = right - scale / 2.0 - padding
        yEnd = top - scale / 2.0 - padding
        xInc = (xEnd - xStart) / 5.0
        yInc = (yEnd - yStart) / 3.5
        cell = MarginCell(self)
        cell.reparentTo(NodePath.anyPath(self))
        cell.setScale(scale)
        cell.setPos(xStart + xInc * x, 0, yStart + yInc * y)
        cell.setAvailable(True)
        cell.setPythonTag('MarginCell', cell)
        self.cells.add(cell)
        self.reorganize()
        return cell

    def setCellAvailable(self, cell, available):
        cell = cell.getPythonTag('MarginCell')
        cell.setAvailable(available)
        self.reorganize()

    def addVisiblePopup(self, popup):
        self.visiblePopups.add(popup)
        self.reorganize()

    def removeVisiblePopup(self, popup):
        if popup not in self.visiblePopups:
            return
        self.visiblePopups.remove(popup)
        self.reorganize()

    def reorganize(self):
        activeCells = [ cell for cell in self.cells if cell.isAvailable() ]
        popups = list(self.visiblePopups)
        popups.sort(key=lambda x: -x.getPriority())
        popups = popups[:len(activeCells)]
        freeCells = []
        for cell in activeCells:
            if not cell.hasContent():
                freeCells.append(cell)
            elif cell.getContent() in popups:
                popups.remove(cell.getContent())
            else:
                cell.setContent(None)
                freeCells.append(cell)

        assert len(freeCells) >= len(popups)
        for popup in popups:
            if popup._lastCell in freeCells and popup._lastCell.isFree():
                popup._lastCell.setContent(popup)
                freeCells.remove(popup._lastCell)
            else:
                cell = random.choice(freeCells)
                cell.setContent(popup)
                freeCells.remove(cell)
+++ okay decompyling C:\Users\dalma_000\Dropbox\TT Stuff\TTSC(new)\TTSC(new)\toontown\toontown2\otp\margins\MarginManager.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2014.05.21 01:52:10 Central Daylight Time
