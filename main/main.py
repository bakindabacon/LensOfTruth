from main_window import Ui_MainWindow
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
import pyqtgraph as pg
import GraphicsItems.ViewPort as vp
import sys
from GraphicsItems.CandleStick import CandleStick
from GraphicsItems.BulkDraw import BulkDraw
import pandas as pd
from Exchange.ccxt_phemex_class import TradeSession
#import Exchange.dontshare_config as ds
from table import TableModel
class mainWindow(qtw.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionQuit.triggered.connect(self.close)




if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = mainWindow()
    window.show()
    GraphDisplay = vp.Display(window.GraphWidget)
    t = TradeSession()
    d = t.get_bidask(symbol='BTC/USD:BTC',size=100)
    df = pd.DataFrame(d[0], columns=['price', 'quantity'])
    print(df)
    data = t.get_bars('1m').drop(columns=['volume'])
    model = TableModel(df)
    window.tableView.setModel(model)
    BulkDraw(GraphDisplay,data)
    sys.exit(app.exec())