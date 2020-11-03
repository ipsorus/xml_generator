# import xmlschema
# schema_xsd = open('D:/load_testing/log/import.2020-04-14.xsd', encoding='utf-8').read()
# schema = xmlschema.XMLSchema(schema_xsd)

# result = schema.is_valid('D:/load_testing/single_test/5000/17-07_load_single_5000_1_signCipher_М.xml')
# res = schema.validate('D:/load_testing/single_test/5000/17-07_load_single_5000_1_signCipher_М.xml')

# print(result, res)

# #print(schema, schema_xsd)
# =====================

# import random

# list = ['82', '81', '80', '79', '78', '77', '76', '75', '74', '73', '72', '71']
# print(list)

# random.shuffle(list)

# print(list)

#================================
# from PyQt5.QtWidgets import *
# import sys

# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)

#         radiobutton = QRadioButton("Australia")
#         radiobutton.setChecked(True)
#         radiobutton.country = "Australia"
#         radiobutton.toggled.connect(self.onClicked)
#         layout.addWidget(radiobutton, 0, 0)

#         radiobutton = QRadioButton("China")
#         radiobutton.country = "China"
#         radiobutton.toggled.connect(self.onClicked)
#         layout.addWidget(radiobutton, 0, 1)

#         radiobutton = QRadioButton("Japan")
#         radiobutton.country = "Japan"
#         radiobutton.toggled.connect(self.onClicked)
#         layout.addWidget(radiobutton, 0, 2)

#     def onClicked(self):
#         radioButton = self.sender()
#         if radioButton.isChecked():
#             print("Country is %s" % (radioButton.country))

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#======================
# from PyQt5 import QtCore, QtGui, QtWidgets
# import sys

# class mainForm(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.runUi()

#     def runUi(self):
#         self.resize(250, 150)
#         self.move(300, 300)
#         self.setWindowTitle('Let\ Rock!')
#         self.setWindowIcon(QtGui.QIcon('icon.png'))
#         self.setMaximumSize(QtCore.QSize(560, 522))
#         self.setMinimumSize(QtCore.QSize(560, 522))

#         layout = QtWidgets.QVBoxLayout(self)

#         groupBoxGD = QtWidgets.QGroupBox('Соединение с ГД', self)

#         layout2 = QtWidgets.QVBoxLayout(groupBoxGD)

#         hrLWGDLink = QtWidgets.QWidget(groupBoxGD)
#         hrLGD = QtWidgets.QVBoxLayout(hrLWGDLink)
#         hrLGD.setContentsMargins(0, 0, 0, 0)
#         btnAddTab = QtWidgets.QPushButton(hrLWGDLink)
#         btnAddTab.setText('Add tab')

#         hrLGD.addWidget(btnAddTab)
#         self.tabWidget = QtWidgets.QTabWidget(hrLWGDLink)
#         hrLGD.addWidget(self.tabWidget)
#         layout2.addWidget(hrLWGDLink)
#         layout.addWidget(groupBoxGD)
#         btnAddTab.clicked.connect(self.addProjectTab)

#     def addProjectTab(self):
#         tab = QtWidgets.QWidget()
#         self.tabWidget.addTab(tab, "tab")

# app = QtWidgets.QApplication(sys.argv)
# w = mainForm()
# w.show()
# sys.exit(app.exec_())

#========================
# import sys
# import os

# from PyQt5 import (QtCore, QtWidgets, QtGui)
# from PyQt5.QtGui import (QIcon)
# from PyQt5.QtWidgets import (QMainWindow, QPushButton, QLabel, QLineEdit, QTextEdit)
# from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QGridLayout)
# from PyQt5.QtWidgets import (QFormLayout, QSizePolicy, QAction, QToolBar)
# from PyQt5.QtCore import (QSize, QProcess)

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('tabs mgmnt test')
#         self.setGeometry(50, 50, 600, 600)

#         self.toolbar = QToolBar('My Main Tool Bar')
#         self.addToolBar(self.toolbar)
#         newTabAct = QAction('New Tab', self)
#         self.toolbar.addAction(newTabAct)
#         newTabAct.triggered.connect(self.newTabHandler)

#     # ----------------------- newTabHandler() ------------------------
#     def newTabHandler(self):
#         tab_widget = self.parentWidget().parentWidget()
#         #              QStackedLayout    QStackedWidget
#         # or
#         # tab_widget = self.window()
#         print(tab_widget)
#         count = tab_widget.count()
#         win = MainWindow()
#         tab_widget.addTab(win, "Tab-{}".format(count + 1))

# # ================================= main() ==========================
# if (__name__ == "__main__"):
#     app = QtWidgets.QApplication(sys.argv)
#     tabs = QtWidgets.QTabWidget()
#     win = MainWindow()
#     tabs.addTab(win, "Tab-1" )
#     tabs.show()
#     sys.exit ( app.exec_() )

#==================================
# import sys
# from PyQt5 import QtCore, QtWidgets, QtGui
# from PyQt5.QtWidgets import (QLineEdit, QLabel, QSpinBox, QWidget, QProgressBar, QPushButton, QApplication)
# from PyQt5.QtCore import QRect
# from PyQt5.QtGui import QFont

# class TabPage(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         self.initUI()

#     def initUI(self):

#         font_8 = QFont()
#         font_8.setFamily("MS Shell Dlg 2")
#         font_8.setPointSize(8)
#         font_8.setBold(False)
#         font_8.setWeight(50)

#         font_12 = QFont()
#         font_12.setFamily("Calibri")
#         font_12.setPointSize(12)
#         font_12.setBold(False)
#         font_12.setWeight(50)

#         self.label = QLabel("№ типа", self)
#         self.label.setGeometry(QRect(10, 10, 141, 16))
#         self.label.setFont(font_8)
#         self.lineEdit = QLineEdit(self)
#         self.lineEdit.setGeometry(QRect(10, 30, 191, 31))
#         self.lineEdit.setFont(font_12)
#         self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
#         self.lineEdit.setClearButtonEnabled(True)

#         self.spinBox = QSpinBox(self)
#         self.spinBox.setGeometry(QRect(240, 30, 191, 31))

#         self.spinBox.setFont(font_12)
#         self.spinBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
#         self.spinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
#         self.spinBox.setWhatsThis("")
#         self.spinBox.setAccessibleName("")
#         self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
#         self.spinBox.setMinimum(1917)
#         self.spinBox.setMaximum(2060)
#         self.spinBox.setProperty("value", 2020)
#         self.label = QLabel("Год выпуска *", self)
#         self.label.setGeometry(QRect(240, 10, 141, 16))
#         self.label.setFont(font_8)

#         self.label = QLabel("Зав №", self)
#         self.label.setGeometry(QRect(470, 10, 141, 16))
#         self.label.setFont(font_8)

#         self.lineEdit = QLineEdit(self)
#         self.lineEdit.setGeometry(QRect(470, 30, 191, 31))
#         self.lineEdit.setFont(font_12)
#         self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
#         self.lineEdit.setClearButtonEnabled(True)

#         self.lineEdit = QLineEdit(self)
#         self.lineEdit.setGeometry(QRect(10, 90, 651, 31))
#         self.lineEdit.setFont(font_12)
#         self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
#         self.lineEdit.setClearButtonEnabled(True)

#         self.label = QLabel("Характеристики СО", self)
#         self.label.setGeometry(QRect(10, 70, 211, 16))
#         self.label.setFont(font_8)

#         self.btn = QPushButton('Печать в консоль', self)
#         self.btn.move(40, 150)
#         self.btn.clicked.connect(self.doAction)

#         self.show()


#     def doAction(self):
#         print(self.lineEdit.text())


# class Window(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.tabs = QtWidgets.QTabWidget()
#         layout = QtWidgets.QVBoxLayout(self)
#         layout.addWidget(self.tabs)
#         button = QtWidgets.QToolButton()
#         button.setToolTip('Add New Tab')
#         button.clicked.connect(self.addNewTab)
#         button.setIcon(self.style().standardIcon(
#             QtWidgets.QStyle.SP_DialogYesButton))
#         self.tabs.setCornerWidget(button, QtCore.Qt.TopRightCorner)
#         self.addNewTab()

#     def addNewTab(self):
#         text = 'Tab %d' % (self.tabs.count() + 1)
#         self.tabs.addTab(TabPage(self.tabs), text)

# if __name__ == '__main__':

#     app = QtWidgets.QApplication(sys.argv)
#     window = Window()
#     window.setGeometry(700, 300, 700, 300)
#     window.show()
#     sys.exit(app.exec_())

#===============================

import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.Qt import *


# class TabPage_SO(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         self.labelType = QLabel("№ типа", self)
#         self.lineEditType = QLineEdit(self)
#         self.lineEditType.setClearButtonEnabled(True)

#         self.labelYearOfIssue = QLabel("Год выпуска *", self)
#         self.spinBox = QSpinBox(self)
#         self.spinBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
#         self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
#         self.spinBox.setMinimum(1917)
#         self.spinBox.setMaximum(2060)
#         self.spinBox.setProperty("value", 2020)

#         self.labelSerialNumber = QLabel("Заводской №", self)
#         self.lineEditSerialNumber = QLineEdit(self)
#         self.lineEditSerialNumber.setClearButtonEnabled(True)

#         self.labelSpecifications = QLabel("Характеристики", self)
#         self.lineEditSpecifications = QLineEdit(self)
#         self.lineEditSpecifications.setClearButtonEnabled(True)

#         grid = QGridLayout(self) 
#         grid.addWidget(self.labelType, 0, 0)
#         grid.addWidget(self.labelYearOfIssue, 0, 1)
#         grid.addWidget(self.labelSerialNumber, 0, 2)
#         grid.addWidget(self.lineEditType, 1, 0)
#         grid.addWidget(self.spinBox, 1, 1)
#         grid.addWidget(self.lineEditSerialNumber, 1, 2)
#         grid.addWidget(self.labelSpecifications, 2, 0)
#         grid.addWidget(self.lineEditSpecifications, 3, 0, 1, 3)
#         grid.setRowStretch(4, 1)


# class TabWidget(QTabWidget):
#     def __init__(self):
#         super().__init__()
#         self.addTab(TabPage_SO(self), "Tab Zero") 
#         count = self.count()
#         nb = QToolButton(text="Добавить", autoRaise=True)     
#         nb.clicked.connect(self.new_tab)
#         self.insertTab(count, QWidget(), "")
#         self.tabBar().setTabButton(count, QTabBar.RightSide, nb)

#     def new_tab(self):
#         index = self.count() - 1
#         self.insertTab(index, TabPage_SO(self), "Tab %d" % index)
#         self.setCurrentIndex(index)


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.centralWidget = QWidget()
#         self.setCentralWidget(self.centralWidget)
        
#         self.tabWidget = TabWidget()
#         self.tableWidget = QTableWidget(0, 4)
#         self.tableWidget.setHorizontalHeaderLabels(
#             ["№ типа", "Год выпуска *", "Заводской №", "Характеристики"])
#         self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
#         self.tableWidget.setSortingEnabled(True)
#         self.tableWidget.setAlternatingRowColors(True)

#         self.buttonAdd = QPushButton('Добавить из текущей вкладки в таблицу')
#         self.buttonAdd.clicked.connect(self.addRowTable)
#         self.buttonDel = QPushButton('Удалить выбранную строку в таблице')
#         self.buttonDel.clicked.connect(self.delRowTable)

#         vbox = QGridLayout(self.centralWidget)
#         vbox.addWidget(self.tabWidget, 0, 0, 1, 2)
#         vbox.addWidget(self.tableWidget, 1, 0, 1, 2)
#         vbox.addWidget(self.buttonAdd, 2, 0)
#         vbox.addWidget(self.buttonDel, 2, 1)
        
        
#     def addRowTable(self):
#         editType = self.tabWidget.currentWidget().lineEditType.text() 
#         spinYearOfIssue = str(self.tabWidget.currentWidget().spinBox.value())
#         editSerialNumber = self.tabWidget.currentWidget().lineEditSerialNumber.text()
#         editSpecifications = self.tabWidget.currentWidget().lineEditSpecifications.text()
        
#         if not editType or not editSerialNumber or not editSpecifications:
#             msg = QMessageBox.information(self, 'Внимание', 'Заполните все поля!')
#             return
#         self.tableWidget.setSortingEnabled(False)
#         rows = self.tableWidget.rowCount()
#         self.tableWidget.insertRow(rows)
#         self.tableWidget.setItem(rows, 0, QTableWidgetItem(editType)) 
#         self.tableWidget.setItem(rows, 1, QTableWidgetItem(spinYearOfIssue))  
#         self.tableWidget.setItem(rows, 2, QTableWidgetItem(editSerialNumber)) 
#         self.tableWidget.setItem(rows, 3, QTableWidgetItem(editSpecifications))          
#         self.tableWidget.setSortingEnabled(True)
#         #print(editType, spinYearOfIssue, editSerialNumber, editSpecifications)    

#     def delRowTable(self):
#         row = self.tableWidget.currentRow()
#         if row == -1:
#             msg = QMessageBox.information(self, 'Внимание', 'Выберите строку для удаления')
#             return
#         self.tableWidget.removeRow(row)    
       

# qss = """
# QLabel {
#     font: 8pt "MS Shell Dlg 2";
# }
# QLineEdit {
#     font: 12pt "Calibri";
# }
# QSpinBox {
#     font: 12pt "Calibri";
# }
# """ 


# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     app.setStyleSheet(qss)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

#======================
# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.Qt import *
# import time as timer

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.centralWidget = QWidget()
#         self.setCentralWidget(self.centralWidget)

#         self.textEdit = QTextEdit()

#         self.buttonAdd = QPushButton('Старт')
#         self.buttonAdd.clicked.connect(self.add_text)

#         vbox = QGridLayout(self.centralWidget)
#         vbox.addWidget(self.textEdit, 0, 0, 1, 2)
#         vbox.addWidget(self.buttonAdd, 2, 1)

#     def add_text(self):
        
#         for i in range(5):
#             timer.sleep(2)
#             self.insert_text(i)
#             QApplication.processEvents()

#     def insert_text(self, i):
#         self.textEdit.append(str(i))


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


#======================
# from PyQt5.QtWidgets import *
# import sys

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.red_warning = "border-color: red; border-style: solid; border-width: 2px; font-weight: normal;"

#         self.centralWidget = QWidget()
#         self.setCentralWidget(self.centralWidget)

#         # Add toolbar and items
#         self.toolbox = QToolBox()

#         self.lineEdit_1 = QLineEdit()
#         self.toolbox.addItem(self.lineEdit_1, "Вкладка 1")
#         self.lineEdit_2 = QLineEdit()
#         self.toolbox.addItem(self.lineEdit_2, "Вкладка 2")
#         self.lineEdit_3 = QLineEdit()
#         self.toolbox.addItem(self.lineEdit_3, "Вкладка 3")

#         self.buttonAdd = QPushButton('Проверить')
#         self.buttonAdd.clicked.connect(self.check)

#         vbox = QGridLayout(self.centralWidget)
#         vbox.addWidget(self.toolbox, 0, 0, 1, 2)
#         vbox.addWidget(self.buttonAdd, 2, 1)

#     def check(self):
#         fields = [self.lineEdit_1, self.lineEdit_2, self.lineEdit_3]
#         for field in fields:
#             if field.text() != '' and field.text().isspace():
#                 field.setStyleSheet(self.red_warning)
#             elif field.text() == '':
#                 field.setStyleSheet(self.red_warning)
#             else:
#                 field.setStyleSheet('')

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec_())

#====================
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import *


class MyToolBoxWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)
        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setSpacing(0)
        self.pages = []
        self.tabs = []

        self._first_v_spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

    def addItem(self, page, name, color=None):
        tab_button = QtWidgets.QPushButton(name)
        font = QtGui.QFont()
        font.setBold(True)
        tab_button.setFont(font)
        page.setSizePolicy(QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        page.hide()
        self.pages.append(page)
        self.tabs.append(tab_button)
        self.vertical_layout.addWidget(tab_button)
        self.vertical_layout.addWidget(page)
        tab_button.clicked.connect(self._button_clicked)

        if color:
            self.setColor( (len(self.pages) - 1), color  )

    def setColor(self, index, color):
        palette = self.get_palette(color)
        self.pages[index].setPalette(palette)
        self.tabs[index].setPalette(palette)
        self.pages[index].setAutoFillBackground(True)

    def check_if_all_pages_are_hidden(self):
        areHidden = True
        for page in self.pages:
            if not page.isHidden():
                areHidden = False
                break
        if areHidden:
            self.vertical_layout.addItem(self._first_v_spacerItem)
        else:
            self.vertical_layout.removeItem(self._first_v_spacerItem)

    def _button_clicked(self):
        i = self.tabs.index(self.sender())
        if self.pages[i].isHidden():
            self.pages[i].show()
        else:
            self.pages[i].hide()
        self.check_if_all_pages_are_hidden()

    def get_palette(self, color):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)

        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)

        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)

        brush = QtGui.QBrush(QtGui.QColor(42, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)

        brush = QtGui.QBrush(QtGui.QColor(42, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)

        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)

        brush = QtGui.QBrush(QtGui.QColor(42, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)

        brush = QtGui.QBrush(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)

        return palette
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)        

        self.my_tool_box = MyToolBoxWidget()

        page1 = QtWidgets.QLineEdit()
        self.my_tool_box.addItem(page=page1, name="Вкладка 1", color="#4ade00")
        page2 = QtWidgets.QLineEdit()
        self.my_tool_box.addItem(page=page2, name="Вкладка 2", color="#009deb")
        page3 = QtWidgets.QLineEdit()
        self.my_tool_box.addItem(page=page3, name="Вкладка 3", color="#f95300")
        page4 = QtWidgets.QLineEdit()
        self.my_tool_box.addItem(page=page4, name="Вкладка 4", color="#ccc")

        # Добавить проставку в конце
        self.my_tool_box.check_if_all_pages_are_hidden()
        
        self.buttonAdd = QPushButton('Проверить')
        self.buttonAdd.clicked.connect(self.check)

        vbox = QGridLayout(self.centralWidget)
        vbox.addWidget(self.my_tool_box, 0, 0, 1, 2)
        vbox.addWidget(self.buttonAdd, 2, 1)
        
        self.red_warning = """
                border-color: red; 
                border-style: solid; 
                border-width: 2px; 
                font-weight: normal;
        """
        self.fields = [page1, page2, page3, page4]

    def check(self):
#        fields = [page1, page2, page3, page4]
#        for field in self.fields:
        for index, field in enumerate(self.fields):
            if field.text() == '' or (field.text() != '' and field.text().isspace()):
                field.setStyleSheet(self.red_warning)
                self.my_tool_box.setColor(index, 'red')
#            elif field.text() == '':
#                field.setStyleSheet(self.red_warning)
            else:
                field.setStyleSheet('')
                self.my_tool_box.setColor(index, '#00FF00')

 
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.setStyle('Fusion')                        # !!! Важно !!!
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())