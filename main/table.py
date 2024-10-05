
from PySide6 import QtGui as qtg
from PySide6.QtWidgets import QWidget, QTabWidget
from PySide6.QtCore import QRect, QAbstractTableModel, Qt
import pyqtgraph as pg

class TableModel(QAbstractTableModel):
    def __init__(self,data):
        super().__init__()
        self._data=data
    def rowCount(self,index):
        return self._data.shape[0]

    def columnCount(self,index):
        return self._data.shape[1]
    def data(self,index,role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            print('Display Role:', index.row(),index.column())
            return str(self._data.iloc[index.row(),index.column()])
    def headerData(self,section,orientation,role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])




