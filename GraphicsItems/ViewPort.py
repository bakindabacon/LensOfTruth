import pyqtgraph as pg
import PySide6.QtGui as qtg
import PySide6.QtWidgets as qtw
import PySide6.QtCore as qtc

class Display():
    def __init__(self, plotWidget):
        super().__init__()
        self.plotWidget = plotWidget
        self.items=[]
        self.x = 0
        self.y = 0
        self.width = 1000
        self.height = 500
        #x_range = [0,300]
        #y_range= [0,1000]
        #self.y_range = y_range
        geo = qtc.QRect(self.x,self.y,self.width,self.height)
        self.plotWidget.setGeometry(geo)
        #self.plotWidget.setXRange(*x_range)
        #self.plotWidget.setYRange(*y_range)

    def addPlotItem(self,item):
        self.items.append(item)
        self.plotWidget.plotItem.addItem(item)


    def update(self,plotWidget):
        pass
