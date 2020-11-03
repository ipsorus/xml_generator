# Владелец интеллектуальной собственности и разработчик данного программного обеспечения: Лошкарев Вадим Игоревич

import sys
import os
import errno

import res_rc
import MainWindow_poverki_2020  #модуль главного окна PyQt

from datetime import datetime, date, time, timedelta
from PyQt5.QtCore import pyqtSignal, Qt, QDate, QDateTime, QTimer, QBasicTimer, QRect
from PyQt5.QtWidgets import QMainWindow, QWidget, QFileDialog, QToolTip, QPushButton, QApplication, QMessageBox, QLineEdit, QLabel, QSpinBox, QProgressBar
from PyQt5.QtGui import *

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QColor, QPalette, QFont

from PyQt5 import QtCore
from PyQt5 import QtGui

from PyQt5.Qt import *


class TestFunc(object):
    def __init__(self, parent=None):
        super().__init__()

        self.mitypeNumber = lineEdit.text()

        print('test', MainWindow_poverki_2020.lineEdit.text())

    def test_func(self, MainWindow):
        '''
        Сборка записи о поверке и сохранение данных в файл
        '''
        print('pechat', MainWindow_poverki_2020.lineEdit.text())