# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTabWidget,
    QTableView, QTableWidgetItem, QWidget)
from GraphicsItems.ViewPort import Display
import config.resource
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        MainWindow.resize(750, 610)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/main_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 750, 571))
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.GraphWidget = pg.PlotWidget(self.tab_1, axisItems={'bottom': pg.DateAxisItem()})
        self.GraphWidget.setObjectName(u"GraphWidget")
        self.GraphWidget.setGeometry(QRect(20, 10, 671, 331))
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableView = QTableView(self.tab_2)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(475, 0, 255, 521))
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 711, 33))
        self.menuQuit = QMenu(self.menubar)
        self.menuQuit.setObjectName(u"menuQuit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuQuit.menuAction())
        self.menuQuit.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lens Of Truth", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Price Chart", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Marketplace", None))
        self.menuQuit.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

