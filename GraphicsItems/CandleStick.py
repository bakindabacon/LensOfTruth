from PySide6 import QtGui as qtg
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
import pyqtgraph as pg

class CandleStick(pg.GraphicsObject):
    def __init__(self,x,open,high,low,close):
        self.x=x
        #self.y=y
        self.width = 30
        self.open=open
        self.high=high
        self.low=low
        self.close=close
        super().__init__()
        self.loadCandle()

    def loadCandle(self):
        self.picture = qtg.QPicture()
        p = qtg.QPainter(self.picture)

        if self.open >= self.close:
            p.setPen(pg.mkPen('r'))
            p.drawLine(qtc.QLine(self.x+self.width/2,self.high,self.x+self.width/2,self.low))
            p.setBrush(pg.mkBrush('r'))
            p.drawRect(qtc.QRect(self.x, self.open, self.width, self.close - self.open))
        else:
            p.setPen(pg.mkPen('g'))
            p.drawLine(qtc.QLine(self.x + self.width / 2, self.high, self.x + self.width / 2, self.low))
            p.setBrush(pg.mkBrush('g'))
            p.drawRect(qtc.QRect(self.x, self.open, self.width, self.close - self.open))

        p.end()
    def paint(self,p,*args):
        p.drawPicture(0,0,self.picture)

    def boundingRect(self):
        return qtc.QRectF(self.picture.boundingRect())