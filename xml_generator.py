# Владелец интеллектуальной собственности и разработчик данного программного обеспечения: Лошкарев Вадим Игоревич

import sys
import os
import errno

import res_rc #файл ресурсов (иконки, стрелки)
import MainWindow_poverki_2020  #модуль главного окна PyQt

from datetime import datetime, date, time
#from PyQt5.QtCore import Qt, QDate, QDateTime, QTimer, QRect
#from PyQt5.QtWidgets import QMainWindow, QWidget, QFileDialog, QToolTip, QPushButton, QApplication, QMessageBox, QLineEdit, QLabel, QProgressBar, QSpinBox, QTabBar, QTextEdit, QToolButton
#from PyQt5.QtGui import *

#from PyQt5.QtGui import QFont

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.Qt import *

class TabPage_SO(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.labelType = QtWidgets.QLabel("№ типа СО по реестру *", self)
        self.labelType.setGeometry(QtCore.QRect(10, 10, 191, 16))
        self.lineEditType = QtWidgets.QLineEdit(self)
        self.lineEditType.setGeometry(QtCore.QRect(10, 30, 191, 31))
        self.lineEditType.setClearButtonEnabled(True)

        self.labelYearOfIssue = QtWidgets.QLabel("Год выпуска *", self)
        self.labelYearOfIssue.setGeometry(QtCore.QRect(240, 10, 191, 16))
        self.spinBoxManufYear = QtWidgets.QSpinBox(self)
        self.spinBoxManufYear.setGeometry(QtCore.QRect(240, 30, 191, 31))
        self.spinBoxManufYear.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.spinBoxManufYear.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxManufYear.setMinimum(1917)
        self.spinBoxManufYear.setMaximum(2060)
        current_date = date.today()
        self.spinBoxManufYear.setProperty("value", current_date.year)

        self.labelSerialNumber = QtWidgets.QLabel("Заводской №/№ партии", self)
        self.labelSerialNumber.setGeometry(QtCore.QRect(470, 10, 191, 16))
        self.lineEditSerialNumber = QtWidgets.QLineEdit(self)
        self.lineEditSerialNumber.setGeometry(QtCore.QRect(470, 30, 191, 31))
        self.lineEditSerialNumber.setClearButtonEnabled(True)

        self.labelSpecifications = QtWidgets.QLabel("Метрологические характеристики СО", self)
        self.labelSpecifications.setGeometry(QtCore.QRect(10, 70, 261, 16))
        self.lineEditSpecifications = QtWidgets.QLineEdit(self)
        self.lineEditSpecifications.setGeometry(QtCore.QRect(10, 90, 651, 31))
        self.lineEditSpecifications.setClearButtonEnabled(True)

class TabPage_SI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.labelTypeSI = QtWidgets.QLabel("Регистрационный № типа СИ *", self)
        self.labelTypeSI.setGeometry(QtCore.QRect(10, 5, 200, 21))
        self.lineEditTypeSI = QtWidgets.QLineEdit(self)
        self.lineEditTypeSI.setGeometry(QtCore.QRect(10, 30, 191, 31))
        self.lineEditTypeSI.setClearButtonEnabled(True)

        self.labelZavNumber = QtWidgets.QLabel("Заводской номер *", self)
        self.labelZavNumber.setGeometry(QtCore.QRect(10, 70, 151, 16))
        self.lineEditZavNumber = QtWidgets.QLineEdit(self)
        self.lineEditZavNumber.setGeometry(QtCore.QRect(10, 90, 191, 31))
        self.lineEditZavNumber.setClearButtonEnabled(True)

        self.labelInventory = QtWidgets.QLabel("Буквенно-цифровое обозначение *", self)
        self.labelInventory.setGeometry(QtCore.QRect(250, 70, 240, 16))
        self.lineEditInventory = QtWidgets.QLineEdit(self)
        self.lineEditInventory.setGeometry(QtCore.QRect(250, 90, 191, 31))
        self.lineEditInventory.setClearButtonEnabled(True)

class main_window(QtWidgets.QMainWindow, MainWindow_poverki_2020.Ui_MainWindow):

    def __init__(self, parent = None):
        super(main_window, self).__init__()
        self.setupUi(self)

        self.menuBar.setVisible(False)
        self.setWindowTitle("")
        self.logoTimer()

        self.font_tab3 = QtGui.QFont()
        self.font_tab3.setFamily("Calibri")
        self.font_tab3.setPointSize(12)
        self.font_tab3.setBold(False)
        self.font_tab3.setWeight(50)

        self.red_warning = "border-color: red; border-style: solid; border-width: 2px; font-weight: normal;"

        self.label_29.setVisible(False)
        self.progressBar.setVisible(False)
        self.listWidget.setVisible(False)
        self.pushButton_4.setVisible(False)
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.line_3.setVisible(False)
        self.line_3.setStyleSheet('color: red;')
        self.line_4.setVisible(False)
        self.line_4.setStyleSheet('color: red;')
        self.line_5.setVisible(False)
        self.line_5.setStyleSheet('color: red;')
        self.line_6.setVisible(False)
        self.line_6.setStyleSheet('color: red;')
        self.label_9.setVisible(False)
        self.label_9.setStyleSheet('color: red;')
        self.label_19.setVisible(False)
        self.label_19.setStyleSheet('color: red;')
        self.label_20.setVisible(False)
        self.label_20.setStyleSheet('color: red;')
        self.label_30.setVisible(False)
        self.label_30.setStyleSheet('color: red;')
        self.calendarWidget.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.pushButton.setEnabled(False)

        self.pushButton.clicked.connect(self.create)            #Запуск
        self.pushButton_2.clicked.connect(self.open_calend)
        self.pushButton_3.clicked.connect(self.close_calend)
        self.pushButton_4.clicked.connect(self.instruction_page_close)
        self.action.triggered.connect(self.info_page)
        self.action_2.triggered.connect(self.instruction_page_open)
        self.action_3.triggered.connect(self.close)

        self.radioButton_3.toggled.connect(self.onClicked_applic_inapplic)
        self.radioButton_7.toggled.connect(self.onClicked_type_SI)
        self.radioButton_8.toggled.connect(self.onClicked_type_SI)
        self.radioButton_9.toggled.connect(self.onClicked_type_SI)

        self.checkBox_4.toggled.connect(self.onClicked_checkBox_4)

        self.comboBox.activated.connect(self.onClicked_comboBox)
        self.tabWidget.currentChanged.connect(self.test_filled_tabs)
        self.toolBox.currentChanged.connect(self.create_first_tabs)

        self.tabWidget_2.tabCloseRequested.connect(self.closeTab_SO)
        self.tabWidget_3.tabCloseRequested.connect(self.closeTab_SI)

        self.tabWidget_2.currentChanged.connect(self.print_tab)

        self.tabCurrIndex = self.tabWidget.currentIndex()

        #Проверка на-лету вкладка 1
        self.lineEdit.textChanged.connect(self.check_tab_1)
        self.lineEdit_2.textChanged.connect(self.check_tab_1)
        self.lineEdit_4.textChanged.connect(self.check_tab_1)
        #Проверка на-лету вкладка 2
        self.lineEdit_7.textChanged.connect(self.check_tab_2)
        self.lineEdit_9.textChanged.connect(self.check_tab_2)
        self.lineEdit_10.textChanged.connect(self.check_tab_2)
        self.lineEdit_11.textChanged.connect(self.check_tab_2)
        #Проверка на-лету вкладка 3
        self.lineEdit_12.textChanged.connect(self.check_tab_3)
        self.lineEdit_13.textChanged.connect(self.check_tab_3)
        self.lineEdit_16.textChanged.connect(self.check_tab_3)
        self.lineEdit_19.textChanged.connect(self.check_tab_3)
        #Проверка на-лету вкладка 4
        self.lineEdit_21.textChanged.connect(self.check_tab_4)
        self.lineEdit_22.textChanged.connect(self.check_tab_4)
        self.lineEdit_23.textChanged.connect(self.check_tab_4)
        self.textEdit_27.textChanged.connect(self.check_tab_4)

        self.indicator_1 = False
        self.indicator_2 = False
        self.indicator_3 = False
        self.indicator_4 = False

        self.count_1 = 0
        self.count_2 = 0
        self.count_3 = 0
        self.count_4 = 0

        self.indexes_SO = {}

    def print_tab(self):
        print('currentWidget', self.tabWidget_2.currentIndex())
    
    #Служебные функции
    def instruction_page_open(self):
        self.listWidget.setVisible(True)
        self.label_29.setVisible(True)
        self.pushButton_4.setVisible(True)

    def instruction_page_close(self):
        self.listWidget.setVisible(False)
        self.label_29.setVisible(False)
        self.pushButton_4.setVisible(False)

    def info_page(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Информация")
        msg.setText("Программное обеспечение: Генератор файлов в формате XML для партий СИ")
        msg.setInformativeText(f"Разработчик: ФГУП \"ВНИИМС\"\nРаспространяется на безвозмездной основе\nВерсия программы: 2.0")
        #msg.setDetailedText(f"Распространяется на безвозмездной основе\nВерсия программы: 2.0")
        okButton = msg.addButton('Закрыть', QtWidgets.QMessageBox.AcceptRole)
        #msg.addButton('Отмена', QMessageBox.RejectRole)
        msg.exec()

    def logoTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.start(5000)
        self.timer.timeout.connect(self.label_image)
        self.timer.setSingleShot(True)

    def label_image(self):
        self.label_23.setVisible(False)
        self.label_24.setVisible(False)
        self.label_25.setVisible(False)
        self.label_26.setVisible(False)
        self.label_27.setVisible(False)
        self.menuBar.setVisible(True)
        self.setWindowTitle("Генератор заявок для партий СИ")
    #=========================

    #Создание и удаление табов
    def create_first_tabs(self):
        if self.toolBox.currentIndex() == 2 and self.tabWidget_2.count() == 0:
            self.comboBox.setEnabled(False)
            count = self.tabWidget_2.count()
            self.nb_SO = QtWidgets.QToolButton(text="Добавить СО", autoRaise=True)
            self.nb_SO.clicked.connect(self.add_tab_SO)
            self.tabWidget_2.insertTab(count, QtWidgets.QWidget(), "")
            self.tabWidget_2.tabBar().setTabButton(count, QtWidgets.QTabBar.RightSide, self.nb_SO)
            self.toolBox.setItemText(2, '> Стандартные образцы, применяемые при поверке')
            self.add_tab_SO()

        elif self.toolBox.currentIndex() == 4 and self.tabWidget_3.count() == 0:
            self.comboBox.setEnabled(False)
            count_SI = self.tabWidget_3.count()
            self.nb_SI = QtWidgets.QToolButton(text="Добавить СИ", autoRaise=True)
            self.nb_SI.clicked.connect(self.add_tab_SI)
            self.tabWidget_3.insertTab(count_SI, QtWidgets.QWidget(), "")
            self.tabWidget_3.tabBar().setTabButton(count_SI, QtWidgets.QTabBar.RightSide, self.nb_SI)
            self.toolBox.setItemText(4, '> СИ, применяемые при поверке')
            self.add_tab_SI()

    def add_tab_SO(self):
        self.indexes_SO[str(self.tabWidget_2.currentIndex())] = 0
        print('self.indexes_SO_create tab', self.indexes_SO)
        self.nb_SO.setEnabled(False)
        self.count_3 = 0
        self.start_to_create_application()
        text = f'Образец'
        index = self.tabWidget_2.count() - 1
        self.tabWidget_2.insertTab(index, TabPage_SO(self), text)
        self.tabWidget_2.setCurrentIndex(self.tabWidget_2.count() - 2)
        self.tabWidget_2.currentWidget().lineEditType.textChanged.connect(self.check_tab_3)

    # def check_tab_test(self):
    #     print('1', self.tabWidget_2(1).lineEditType.text())
    #     print('2', self.tabWidget_2(2).lineEditType.text())

    def add_tab_SI(self):
        self.nb_SI.setEnabled(False)
        self.count_3 = 0
        self.start_to_create_application()
        text = f'СИ'
        index = self.tabWidget_3.count() - 1
        self.tabWidget_3.insertTab(index, TabPage_SI(self), text)
        self.tabWidget_3.setCurrentIndex(self.tabWidget_3.count() - 2)
        self.tabWidget_3.currentWidget().lineEditTypeSI.textChanged.connect(self.check_tab_3)
        self.tabWidget_3.currentWidget().lineEditZavNumber.textChanged.connect(self.check_tab_3)
        self.tabWidget_3.currentWidget().lineEditInventory.textChanged.connect(self.check_tab_3)

    def closeTab_SO (self, currentIndex):
        self.tabWidget_2.removeTab(currentIndex)
        deleted_tab = self.indexes_SO.pop(str(currentIndex), None)
        #del self.indexes_SO[str(self.tabWidget_2.count() - 1)]
        print('self.indexes_SO_del tab', self.indexes_SO)
        print('currentIndex', currentIndex)
        print('deleted_tab', deleted_tab)
        self.tabWidget_2.setCurrentIndex(self.tabWidget_2.count() - 2)
        if self.tabWidget_2.count() == 1:
            self.tabWidget_2.removeTab(currentIndex)
            self.toolBox.setItemText(2, 'Стандартные образцы, применяемые при поверке')
            self.toolBox.setCurrentIndex(0)
            self.label_30.setText("Необходимо заполнить хотя бы одно поле")
            self.comboBox.setEnabled(True)
            self.check_tab_3()
        self.check_tab_3()

    def closeTab_SI (self, currentIndex):
        self.tabWidget_3.removeTab(currentIndex)
        self.tabWidget_3.setCurrentIndex(self.tabWidget_3.count() - 2)
        if self.tabWidget_3.count() == 1:
            self.tabWidget_3.removeTab(currentIndex)
            self.toolBox.setItemText(4, 'СИ, применяемые при поверке')
            self.toolBox.setCurrentIndex(0)
            self.label_30.setText("Необходимо заполнить хотя бы одно поле")
            self.comboBox.setEnabled(True)
            self.check_tab_3()
        self.check_tab_3()
    #==========================

    #Тестирование табов на заполнение полей
    def test_filled_tabs(self):
        if self.tabCurrIndex == 0:
            self.indicator_1 = True
            self.check_tab_1()
        elif self.tabCurrIndex == 1:
            self.indicator_2 = True
            self.check_tab_2()
        elif self.tabCurrIndex == 2:
            self.indicator_3 = True
            self.check_tab_3()
        elif self.tabCurrIndex == 3:
            self.indicator_4 = True
            self.check_tab_4()
        self.tabCurrIndex = self.tabWidget.currentIndex()
    #=========================

    #Действия по нажатию на радиобаттоны, чекбоксы и комбобоксы
    def onClicked_type_SI(self):
        if self.radioButton_7.isChecked():
            self.label_4.setText("Тип СИ*")
        elif self.radioButton_8.isChecked():
            self.label_4.setText("Метрологическая аттестация*")
        elif self.radioButton_9.isChecked():
            self.label_4.setText("СИ ВН или СН*")

    def onClicked_applic_inapplic(self):
        if self.radioButton_3.isChecked():
            self.label_17.setEnabled(True)
            self.lineEdit_8.setEnabled(True)
            self.checkBox.setEnabled(True)
            self.checkBox_2.setEnabled(True)
            self.lineEdit_9.setEnabled(False)
            self.lineEdit_9.setStyleSheet("")
            self.label_18.setEnabled(False)
            self.check_tab_2()
            print('self.indicator_2', self.indicator_2)
            print('test_check')
        else:
            self.check_tab_2()
            self.label_18.setEnabled(True)
            self.lineEdit_9.setEnabled(True)
            self.label_17.setEnabled(False)
            self.lineEdit_8.setEnabled(False)
            self.checkBox.setEnabled(False)
            self.checkBox_2.setEnabled(False)

    def onClicked_comboBox(self):
        if self.comboBox.currentIndex() > 0:
            self.toolBox.setEnabled(False)
            self.label_30.setVisible(False)
            self.line_5.setVisible(False)
        else:
            self.toolBox.setEnabled(True)
            self.check_tab_3()

    def onClicked_checkBox_4(self):
        if self.checkBox_4.isChecked():
            self.label_44.setEnabled(True)
            self.textEdit_27.setEnabled(True)
            self.check_tab_4()
        else:
            self.textEdit_27.setStyleSheet("")
            self.label_44.setEnabled(False)
            self.textEdit_27.setEnabled(False)
            self.textEdit_27.clear()
    #=============================

    #Открытие и закрытие календаря для поля Действительна до
    def open_calend(self):
        self.label_19.setVisible(False)
        self.label_20.setVisible(False)
        self.pushButton_3.setVisible(True)
        self.calendarWidget.setVisible(True)
        self.pushButton_2.setVisible(False)
        self.calendarWidget.clicked.connect(self.valid_date)

    def close_calend(self):
        self.pushButton_2.setVisible(True)
        self.calendarWidget.setVisible(False)
        self.pushButton_3.setVisible(False)
    #=============================

    #Установка даты в формате "yyyy-MM-dd" в поле Действительна до
    def valid_date(self):
        self.close_calend()
        self.lineEdit_6.setText(self.calendarWidget.selectedDate().toString("yyyy-MM-dd"))
    #=============================

    def applic_constructor(self, filepath, result, part, counter_zav):
        '''
        Сборка записи о поверке и сохранение данных в файл
        '''

        date_stamp = datetime.now().strftime("%Y-%m-%d")

        #Название файла
        name_of_file = r'заявка_xml_' + date_stamp + '_' + self.mitypeNumber.strip(" ") + '_часть_' + str(part) + '_записей_' + str(result) + '_шифр_' + self.signCipher.strip(" ") + '.xml'

        #Путь сохранения файла
        FileFullPath = os.path.join(filepath, name_of_file)

        with open (FileFullPath, 'w', encoding='utf-8') as sample:

            header_1 = f'<?xml version="1.0" encoding="utf-8" ?>\n'
            header_comment_1 = f'<!--\n'
            header_comment_2 = f'Данный xml-файл создан при помощи ПО "Генератор заявок для партий СИ"\n'
            header_comment_3 = f'Версия ПО 2.0\n'
            header_comment_4 = f'-->\n'
            header_2 = f'<gost:application xmlns:gost="urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19">\n'
            header = header_1 + header_comment_1 + header_comment_2 + header_comment_3 + header_comment_4 + header_2
            sample.write(header)

        for n in range(result):
            #Основное тело записи о поверке
            body = ''

            manufactureNum = self.prefix_zav_number.lstrip(" ") + str(counter_zav).zfill(self.zav_len) + self.tail_zav_number.rstrip(" ")

            with open (FileFullPath, 'a', encoding='utf-8') as sample_body:

                body = f'<gost:result>\n'+ f'<gost:miInfo>\n' + f'<gost:singleMI>\n'

                if self.radioButton_7.isChecked():
                    body += f'<gost:mitypeNumber>{self.mitypeNumber.strip(" ")}</gost:mitypeNumber>\n'
                elif self.radioButton_8.isChecked():
                    body += f'<gost:crtmitypeTitle>{self.mitypeNumber.strip(" ")}</gost:crtmitypeTitle>\n'
                elif self.radioButton_9.isChecked():
                    body += f'<gost:milmitypeTitle>{self.mitypeNumber.strip(" ")}</gost:milmitypeTitle>\n'

                if self.radioButton_5.isChecked():
                    body += f'<gost:manufactureNum>{manufactureNum}</gost:manufactureNum>\n'
                else:
                    body += f'<gost:inventoryNum>{manufactureNum}</gost:inventoryNum>\n'

                if self.manufactureYear != '':
                    body += f'<gost:manufactureYear>{self.manufactureYear}</gost:manufactureYear>\n'

                body += f'<gost:modification>{self.modification.strip(" ")}</gost:modification>\n'

                body += f'</gost:singleMI>\n'
                body += f'</gost:miInfo>\n'
                body += f'<gost:signCipher>{self.signCipher.strip(" ")}</gost:signCipher>\n'
                body += f'<gost:miOwner>{self.miOwner.strip(" ")}</gost:miOwner>\n'

                body += f'<gost:vrfDate>{self.vrfDate}</gost:vrfDate>\n'

                if self.validDate != '':
                    body += f'<gost:validDate>{self.validDate}</gost:validDate>\n'

                if self.radioButton.isChecked():
                    body += f'<gost:type>1</gost:type>\n'
                else:
                    body += f'<gost:type>2</gost:type>\n'

                body += f'<gost:calibration>{self.calibration}</gost:calibration>\n'
                if self.radioButton_3.isChecked():
                    body += f'<gost:applicable>\n'
                    if self.stickerNum != '':
                        body += f'<gost:stickerNum>{self.stickerNum.strip(" ")}</gost:stickerNum>\n'
                    body += f'<gost:signPass>{self.signPass}</gost:signPass>\n'
                    body += f'<gost:signMi>{self.signMi}</gost:signMi>\n'
                    body += f'</gost:applicable>\n'
                else:
                    body += f'<gost:inapplicable>\n'
                    body += f'<gost:reasons>{self.reasons.strip(" ")}</gost:reasons>\n'
                    body += f'</gost:inapplicable>\n'

                body += f'<gost:docTitle>{self.method.strip(" ")}</gost:docTitle>\n'

                if self.metrologist != '':
                    body += f'<gost:metrologist>{self.metrologist.strip(" ")}</gost:metrologist>\n'

                body += f'<gost:means>\n'

                if self.comboBox.currentIndex() == 0:
                    if self.npe_number != '':
                        text = self.npe_number.strip(' ')
                        text = text.split(';')
                        body += f'<gost:npe>\n'
                        for t in text:
                            if t != '' and not t.isspace():
                                body += f'<gost:number>{t.strip(" ")}</gost:number>\n'
                        body += f'</gost:npe>\n'

                    if self.uve_number != '':
                        text = self.uve_number.strip(' ')
                        text = text.split(';')
                        body += f'<gost:uve>\n'
                        for t in text:
                            if t != '' and not t.isspace():
                                body += f'<gost:number>{t.strip(" ")}</gost:number>\n'
                        body += f'</gost:uve>\n'

                    if self.tabWidget_2.count() > 1:
                        body += f'<gost:ses>\n'
                        for i in range(self.tabWidget_2.count() - 1):
                            self.tabWidget_2.setCurrentIndex(i)
                            body += F'<gost:se>\n'
                            body += f'<gost:typeNum>{self.tabWidget_2.currentWidget().lineEditType.text().strip(" ")}</gost:typeNum>\n'
                            body += f'<gost:manufactureYear>{self.tabWidget_2.currentWidget().spinBoxManufYear.value()}</gost:manufactureYear>\n'
                            if self.tabWidget_2.currentWidget().lineEditSerialNumber.text() != '' and not self.tabWidget_2.currentWidget().lineEditSerialNumber.text().isspace():
                                body += f'<gost:manufactureNum>{self.tabWidget_2.currentWidget().lineEditSerialNumber.text().strip(" ")}</gost:manufactureNum>\n'
                            if self.tabWidget_2.currentWidget().lineEditSpecifications.text() != '' and not self.tabWidget_2.currentWidget().lineEditSpecifications.text().isspace():
                                body += f'<gost:metroChars>{self.tabWidget_2.currentWidget().lineEditSpecifications.text().strip(" ")}</gost:metroChars>\n'
                            body += F'</gost:se>\n'
                        body += f'</gost:ses>\n'

                    if self.mieta_number != '':
                        text = self.mieta_number.strip(' ')
                        text = text.split(';')
                        body += f'<gost:mieta>\n'
                        for t in text:
                            if t != '' and not t.isspace():
                                body += f'<gost:number>{t.strip(" ")}</gost:number>\n'
                        body += f'</gost:mieta>\n'

                    if self.tabWidget_3.count() > 1:
                        body += f'<gost:mis>\n'
                        for i in range(self.tabWidget_3.count() - 1):
                            self.tabWidget_3.setCurrentIndex(i)
                            body += F'<gost:mi>\n'
                            body += f'<gost:typeNum>{self.tabWidget_3.currentWidget().lineEditTypeSI.text().strip(" ")}</gost:typeNum>\n'
                            if self.tabWidget_3.currentWidget().lineEditZavNumber.text() != '':
                                body += f'<gost:manufactureNum>{self.tabWidget_3.currentWidget().lineEditZavNumber.text().strip(" ")}</gost:manufactureNum>\n'
                            elif self.tabWidget_3.currentWidget().lineEditInventory.text() != '':
                                body += f'<gost:inventoryNum>{self.tabWidget_3.currentWidget().lineEditInventory.text().strip(" ")}</gost:inventoryNum>\n'
                            body += F'</gost:mi>\n'
                        body += f'</gost:mis>\n'

                    if self.reagent_number != '':
                        text = self.reagent_number.strip(' ')
                        text = text.split(';')
                        body += f'<gost:reagent>\n'
                        for t in text:
                            if t != '' and not t.isspace():
                                body += f'<gost:number>{t.strip(" ")}</gost:number>\n'
                        body += f'</gost:reagent>\n'

                else:
                    body += f'<gost:oMethod>{self.oMethod}</gost:oMethod>\n'

                body += f'</gost:means>\n'

                body += f'<gost:conditions>\n'
                body += f'<gost:temperature>{self.temperature.strip(" ")}</gost:temperature>\n'
                body += f'<gost:pressure>{self.pressure.strip(" ")}</gost:pressure>\n'
                body += f'<gost:hymidity>{self.hymidity.strip(" ")}</gost:hymidity>\n'
                if self.other != '':
                    body += f'<gost:other>{self.other.strip(" ")}</gost:other>\n'
                body += f'</gost:conditions>\n'

                if self.structure != '':
                    body += f'<gost:structure>{self.structure.strip(" ")}</gost:structure>\n'

                if self.checkBox_4.isChecked():
                    body += f'<gost:brief_procedure>\n'
                    body += f'<gost:characteristics>{self.characteristics.strip(" ")}</gost:characteristics>\n'
                    body += f'</gost:brief_procedure>\n'

                if self.additional_info != '':
                    body += f'<gost:additional_info>{self.additional_info.strip(" ")}</gost:additional_info>\n'

                body += f'</gost:result>\n'
                sample_body.write(body)

                counter_zav += 1

        with open (FileFullPath, 'a', encoding='utf-8') as sample:
            footer = f'</gost:application>\n'
            sample.write(footer)

        return counter_zav

    #Проверка что введенное значение в поле Заводской номер является числом
    def check_zav_number_is_int(self):
        try:
            self.counter_zav_number = int(self.counter_zav_number)
            self.label_9.setVisible(False)
        except ValueError:
            pass
            #self.label_9.setVisible(True)
            #self.lineEdit_4.setStyleSheet(self.red_warning)
            #self.line_3.setVisible(True)
            #self.pushButton.setText("Необходимо заполнить обязательные поля")

    #Проверка таб 1
    def check_tab_1(self):
        #Тип СИ
        self.mitypeNumber = self.lineEdit.text()
        #Модификация СИ
        self.modification = self.lineEdit_2.text()
        #Дата производства СИ
        self.manufactureYear = self.spinBox_3.text()
        if self.manufactureYear == '-':
            self.manufactureYear = ''
        else:
            self.manufactureYear = int(self.spinBox_3.text())
        #Заводской номер СИ
        self.prefix_zav_number = self.lineEdit_3.text()
        self.counter_zav_number = self.lineEdit_4.text()
        self.zav_len = len(self.counter_zav_number.strip(' '))
        if self.counter_zav_number != '':
            self.check_zav_number_is_int()
        self.tail_zav_number = self.lineEdit_5.text()

        if self.indicator_1 == False:
            self.universal_fields_checker_with_sender()
            if self.mitypeNumber != '' and self.modification != '' and type(self.counter_zav_number) is int:
                self.count_1 = 1
            else:
                self.count_1 = 0

        else:
            field_tab_1 = {'self.mitypeNumber': [self.mitypeNumber, self.lineEdit, self.line_3],
                        'self.modification': [self.modification, self.lineEdit_2, self.line_3],
                        'self.counter_zav_number': [str(self.counter_zav_number), self.lineEdit_4, self.line_3]}

            self.check_zav_number_is_int()
            if not type(self.counter_zav_number) is int:
                self.label_9.setVisible(True)

            self.universal_fields_checker(field_tab_1)

            # for field in field_tab_1.keys():
            #     required_field = field_tab_1[field][1]
            #     alert_field = field_tab_1[field][2]
            #     #Проход циклом по всем полям, выявление незаполненных обязательных полей
            #     if field_tab_1[field][0] == '' or field_tab_1[field][0].isspace():
            #         required_field.setStyleSheet(self.red_warning)
            #         alert_field.setVisible(True)
            #         self.pushButton.setText("Необходимо проверить вкладку Сведения о СИ")
            #         self.pushButton.setEnabled(False)
            #     else:
            #         required_field.setStyleSheet("")
            #         self.pushButton.setText("Создать заявку")

            if self.mitypeNumber != '' and self.modification != '' and type(self.counter_zav_number) is int:
                self.line_3.setVisible(False)
                #self.pushButton.setText("Создать заявку")
                self.count_1 = 1
            else:
                self.line_3.setVisible(True)
                #self.pushButton.setText("Необходимо проверить вкладку Сведения о СИ")
                #self.pushButton.setEnabled(False)
                self.count_1 = 0

        # if self.count_1 == 1:
        #     return self.count_1
        self.start_to_create_application()
        print('self.count_1', self.count_1)
        return self.count_1

    #Проверка таб 2
    def check_tab_2(self):
        #Условный шифр знака поверки
        signCipher = self.lineEdit_7.text()
        self.signCipher = signCipher.upper()
        #Владелец СИ
        self.miOwner = self.lineEdit_10.text()
        #Дата поверки (формат гггг-мм-дд)
        self.vrfDate = self.dateEdit.text()
        #Дата действия поверки (формат гггг-мм-дд)
        self.validDate = self.lineEdit_6.text()
        #Методика поверки
        self.method = self.lineEdit_11.text()
        #Ф.И.О. поверителя
        self.metrologist = self.lineEdit_20.text()
        #Результаты калибровки (true/false)
        calibration = f'{self.checkBox_3.isChecked()}'
        self.calibration = calibration.lower()
        #Номер наклейки
        self.stickerNum = self.lineEdit_8.text()
        #Знак поверки в паспорте (true/false)
        signPass = f'{self.checkBox.isChecked()}'
        self.signPass = signPass.lower()
        #Знак поверки на СИ (true/false)
        signMi = f'{self.checkBox_2.isChecked()}'
        self.signMi = signMi.lower()
        #Причина непригодности
        self.reasons = self.lineEdit_9.text()

        if self.indicator_2 == False:
            self.universal_fields_checker_with_sender()

            if self.radioButton_3.isChecked() and self.method != '' and self.signCipher != '' and self.miOwner != '':
                self.count_2 = 1
            elif self.radioButton_4.isChecked() and self.reasons != '' and self.method != '' and self.signCipher != '' and self.miOwner != '':
                self.count_2 = 1
            else:
                #self.pushButton.setEnabled(False)
                self.count_2 = 0

        else:
            field_tab_2 = {'self.method': [self.method, self.lineEdit_11, self.line_4],
                        'self.signCipher': [self.signCipher, self.lineEdit_7, self.line_4],
                        'self.miOwner': [self.miOwner, self.lineEdit_10, self.line_4],
                        'self.reasons': [self.reasons, self.lineEdit_9, self.line_4]}

            self.universal_fields_checker(field_tab_2)
            # for field in field_tab_2.keys():
            #     required_field = field_tab_2[field][1]
            #     alert_field = field_tab_2[field][2]
            #     #Проход циклом по всем полям, выявление незаполненных обязательных полей
            #     if (field == 'self.reasons' and self.radioButton_4.isChecked()) and (field_tab_2[field][0] == '' or field_tab_2[field][0].isspace()):
            #         required_field.setStyleSheet(self.red_warning)
            #         alert_field.setVisible(True)
            #         self.pushButton.setText("Необходимо проверить вкладку Сведения о поверке")
            #         self.count_2 = 0
            #     elif field != 'self.reasons' and field_tab_2[field][0] == '' or field_tab_2[field][0].isspace():
            #         required_field.setStyleSheet(self.red_warning)
            #         alert_field.setVisible(True)
            #         self.pushButton.setText("Необходимо проверить вкладку Сведения о поверке")
            #         self.count_2 = 0
            #     else:
            #         alert_field.setVisible(False)
            #         required_field.setStyleSheet("")
            #         self.pushButton.setText("Создать заявку")
            #         self.count_2 = 1

            if self.radioButton_3.isChecked() and self.method != '' and self.signCipher != '' and self.miOwner != '' or (self.radioButton_4.isChecked() and self.reasons != '' and self.method != '' and self.signCipher != '' and self.miOwner != ''):
                self.line_4.setVisible(False)
                self.count_2 = 1
                if self.validDate != '' and self.vrfDate == self.validDate:
                    self.label_20.setVisible(False)
                    self.label_19.setVisible(True)
                    self.line_4.setVisible(True)
                    #self.pushButton.setText("Необходимо заполнить обязательные поля")
                    self.count_2 = 0
                elif self.validDate != '' and self.vrfDate > self.validDate:
                    self.label_19.setVisible(False)
                    self.label_20.setVisible(True)
                    self.line_4.setVisible(True)
                    #self.pushButton.setText("Необходимо заполнить обязательные поля")
                    self.count_2 = 0
                else:
                    #self.pushButton.setText("Создать заявку")
                    self.label_19.setVisible(False)
                    self.label_20.setVisible(False)
                    self.count_2 = 1
            else:
                self.line_4.setVisible(True)
                #self.pushButton.setText("Необходимо заполнить обязательные поля")
                self.count_2 = 0

        # if self.count_2 == 1:
        #     return self.count_2
        self.start_to_create_application()
        print('self.count_2', self.count_2)
        return self.count_2

    #Проверка таб 3
    def check_tab_3(self):
        self.full_count = self.tabWidget_2.count() - 1
        print('self.full_count_начало функции', self.full_count)

        #ГПЭ
        self.npe_number = self.lineEdit_12.text()
        #Эталоны
        self.uve_number = self.lineEdit_13.text()
        #СИ, применяемые в качестве эталонов
        self.mieta_number = self.lineEdit_16.text()
        #Вещества (материалы)
        self.reagent_number = self.lineEdit_19.text()
        #Методы поверки без применения средств поверки
        self.oMethod = self.comboBox.currentIndex()

        if self.comboBox.currentIndex() == 0:
            if self.npe_number != '' or self.uve_number != '' or self.tabWidget_2.count() > 0 or self.mieta_number != '' or self.tabWidget_3.count() > 0 or self.reagent_number != '':
                self.line_5.setVisible(False)
                self.label_30.setVisible(False)
                self.comboBox.setEnabled(False)
                #self.pushButton.setText("Создать заявку")
                self.count_3 = 1
            else:
                self.comboBox.setEnabled(True)
                self.line_5.setVisible(True)
                self.label_30.setVisible(True)
                self.comboBox.setEnabled(True)
                #self.pushButton.setText("Необходимо проверить вкладку Средства поверки")
                self.count_3 = 0

            # #Проверка: Если создана вкладка СО, применяемые при поверке.
            if self.tabWidget_2.count() > 0:
                for i in range(self.tabWidget_2.count() - 1):
                    if self.tabWidget_2.widget(i).lineEditType.text() == '' or self.tabWidget_2.widget(i).lineEditType.text().isspace():
                        self.tabWidget_2.widget(i).lineEditType.setStyleSheet(self.red_warning)
                        self.nb_SO.setEnabled(False)
                        self.line_5.setVisible(True)
                        self.label_30.setText("Необходимо проверить вкладку Стандартные образцы, применяемые при поверке")
                        #self.pushButton.setText("Необходимо проверить вкладку Стандартные образцы, применяемые при поверке")
                        self.count_3 = 0
                        self.start_to_create_application()
                        return
                    else:
                        self.tabWidget_2.widget(i).lineEditType.setStyleSheet('')
                        self.tabWidget_2.widget(i).lineEditType.setFont(self.font_tab3)
                        #self.tabWidget_2.setTabText(self.tabWidget_2.currentIndex(), 'Образец')
                        self.nb_SO.setEnabled(True)
                        self.line_5.setVisible(False)
                        self.label_30.setVisible(False)
                        #self.pushButton.setText("Создать заявку")
                        self.count_3 = 1
                        self.start_to_create_application()

            #Проверка: Если создана вкладка СИ, применяемые при поверке.
            if self.tabWidget_3.count() > 0:
                for i in range(self.tabWidget_3.count() - 1):
                    if self.tabWidget_3.widget(i).lineEditTypeSI.text() == '' or self.tabWidget_3.widget(i).lineEditTypeSI.text().isspace():
                        self.tabWidget_3.widget(i).lineEditTypeSI.setStyleSheet(self.red_warning)
                        self.line_5.setVisible(True)
                        self.label_30.setVisible(True)
                        self.label_30.setText("Необходимо проверить вкладку СИ, применяемые при поверке")
                        self.nb_SI.setEnabled(False)
                        #self.pushButton.setText("Необходимо проверить вкладку СИ, применяемые при поверке")
                        self.count_3 = 0
                        self.start_to_create_application()
                        return
                    else:
                        self.tabWidget_3.widget(i).lineEditZavNumber.setStyleSheet('')
                        self.tabWidget_3.widget(i).lineEditZavNumber.setFont(self.font_tab3)
                        self.tabWidget_3.widget(i).lineEditInventory.setStyleSheet('')
                        self.tabWidget_3.widget(i).lineEditInventory.setFont(self.font_tab3)
                        self.tabWidget_3.widget(i).lineEditTypeSI.setStyleSheet('')
                        self.tabWidget_3.widget(i).lineEditTypeSI.setFont(self.font_tab3)
                        self.line_5.setVisible(False)
                        self.label_30.setVisible(False)
                        #self.pushButton.setText("Создать заявку")
                        self.nb_SI.setEnabled(True)
                        self.count_3 = 1
                        self.start_to_create_application()
                        #Если заполнено поле Тип СИ, то проверка заполнения зав. № или буквенно-цифрового обозначения
                        if self.tabWidget_3.widget(i).lineEditTypeSI.text() != '' and (self.tabWidget_3.widget(i).lineEditZavNumber.text() == '' and self.tabWidget_3.widget(i).lineEditInventory.text() == ''):
                            self.tabWidget_3.widget(i).lineEditZavNumber.setStyleSheet(self.red_warning)
                            self.tabWidget_3.widget(i).lineEditInventory.setStyleSheet(self.red_warning)
                            self.line_5.setVisible(True)
                            self.label_30.setVisible(True)
                            self.label_30.setText("Необходимо заполнить либо буквенно-цифровое обозначение, либо заводской номер")
                            #self.pushButton.setText("Необходимо проверить вкладку СИ, применяемые при поверке")
                            self.nb_SI.setEnabled(False)
                            self.count_3 = 0
                            self.start_to_create_application()
                            return

        else:
            self.line_5.setVisible(False)
            self.label_30.setVisible(False)
            #self.pushButton.setText("Создать заявку")
            self.count_3 = 1

        # if self.count_3 == 1:
        #     return self.count_3
        self.start_to_create_application()
        print('self.count_3', self.count_3)
        return self.count_3

    #Проверка таб 3 Стандартные образцы
    def check_tab_3_SO(self):

        #Проверка: Если заполнено поле СО, применяемые при поверке.
        #self.tabWidget_2.setCurrentIndex(self.tabWidget_2.currentIndex())
        if self.tabWidget_2.currentWidget().lineEditType.text() == '' or self.tabWidget_2.currentWidget().lineEditType.text().isspace():
            self.tabWidget_2.currentWidget().lineEditType.setStyleSheet(self.red_warning)
            self.line_5.setVisible(True)
            self.label_30.setVisible(True)
            self.label_30.setText("Необходимо проверить вкладку Стандартные образцы, применяемые при поверке")
            #self.pushButton.setText("Необходимо проверить вкладку Стандартные образцы, применяемые при поверке")
            self.count_3 = 0
            self.start_to_create_application()
            print('self.count_3', self.count_3)
            return
        else:
            self.tabWidget_2.currentWidget().lineEditType.setStyleSheet('')
            self.tabWidget_2.currentWidget().lineEditType.setFont(self.font_tab3)
            self.line_5.setVisible(False)
            self.label_30.setVisible(False)
            #self.pushButton.setText("Создать заявку")
            self.count_3 = 1

        # if self.count_3 == 1:
        #     self.start_to_create_check(self.count_3)
        #     return self.count_3
        self.start_to_create_application()
        print('self.count_3', self.count_3)
        return self.count_3

    #Проверка таб 3 Средства измерений
    def check_tab_3_SI(self):

        #self.tabWidget_3.setCurrentIndex(self.tabWidget_3.currentIndex())
        if self.tabWidget_3.currentWidget().lineEditTypeSI.text() == '' or self.tabWidget_3.currentWidget().lineEditTypeSI.text().isspace():
            self.tabWidget_3.currentWidget().lineEditTypeSI.setStyleSheet(self.red_warning)
            self.line_5.setVisible(True)
            self.label_30.setVisible(True)
            self.label_30.setText("Необходимо проверить вкладку СИ, применяемые при поверке")
            #self.pushButton.setText("Необходимо проверить вкладку СИ, применяемые при поверке")
            print('self.count_3', self.count_3)
            self.start_to_create_application()
            self.count_3 = 0
            return
        else:
            self.tabWidget_3.currentWidget().lineEditZavNumber.setStyleSheet('')
            self.tabWidget_3.currentWidget().lineEditInventory.setStyleSheet('')
            self.tabWidget_3.currentWidget().lineEditTypeSI.setStyleSheet('')
            self.tabWidget_3.currentWidget().lineEditZavNumber.setFont(self.font_tab3)
            self.tabWidget_3.currentWidget().lineEditInventory.setFont(self.font_tab3)
            self.tabWidget_3.currentWidget().lineEditTypeSI.setFont(self.font_tab3)
            self.line_5.setVisible(False)
            self.label_30.setVisible(False)
            #self.pushButton.setText("Создать заявку")
            self.count_3 = 1
            if self.tabWidget_3.currentWidget().lineEditTypeSI.text() != '' and ((self.tabWidget_3.currentWidget().lineEditZavNumber.text() == '' or self.tabWidget_3.currentWidget().lineEditZavNumber.text().isspace()) and (self.tabWidget_3.currentWidget().lineEditInventory.text() == '' or self.tabWidget_3.currentWidget().lineEditInventory.text().isspace())):
                self.tabWidget_3.currentWidget().lineEditZavNumber.setStyleSheet(self.red_warning)
                self.tabWidget_3.currentWidget().lineEditInventory.setStyleSheet(self.red_warning)
                self.line_5.setVisible(True)
                self.label_30.setVisible(True)
                self.label_30.setText("Необходимо заполнить либо буквенно-цифровое обозначение, либо заводской номер")
                #self.pushButton.setText("Необходимо проверить вкладку СИ, применяемые при поверке")
                self.count_3 = 0
                self.start_to_create_application()
                return

        # if self.count_3 == 1:
        #     self.start_to_create_check(self.count_3)
        #     return self.count_3
        # self.start_to_create_check(self.count_3)
        self.start_to_create_application()
        print('self.count_3', self.count_3)
        return self.count_3

    #Проверка таб 4
    def check_tab_4(self):
        #Условия проведения поверки
        self.temperature = self.lineEdit_21.text()
        self.pressure = self.lineEdit_22.text()
        self.hymidity = self.lineEdit_23.text()
        #Другие факторы
        self.other = self.textEdit_24.toPlainText()
        #Состав СИ, представленного на поверку
        self.structure = self.textEdit_25.toPlainText()
        #Краткая характеристика объема поверки
        self.characteristics = self.textEdit_27.toPlainText()
        #Прочие сведения
        self.additional_info = self.textEdit_26.toPlainText()

        if self.indicator_4 == False:
            self.universal_fields_checker_with_sender()
            if self.checkBox_4.checkState() == 0 and self.temperature != '' and self.pressure != '' and self.hymidity != '':
                self.count_4 = 1
            elif self.checkBox_4.isChecked() and self.characteristics != '' and self.temperature != '' and self.pressure != '' and self.hymidity != '':
                self.count_4 = 1
            else:
                #self.pushButton.setEnabled(False)
                self.count_4 = 0
        else:
            field_tab_4 = {'self.temperature': [self.temperature, self.lineEdit_21, self.line_6],
                        'self.pressure': [self.pressure, self.lineEdit_22, self.line_6],
                        'self.hymidity': [self.hymidity, self.lineEdit_23, self.line_6],
                        'self.characteristics': [self.characteristics, self.textEdit_27, self.line_6]}

            self.universal_fields_checker(field_tab_4)
            print('func_4', self.count_4)
            # for field in field_tab_4.keys():
            #     required_field = field_tab_4[field][1]
            #     alert_field = field_tab_4[field][2]
            #     #Проход циклом по всем полям, выявление незаполненных обязательных полей
            #     if (field == 'self.characteristics' and self.checkBox_4.isChecked()) and (field_tab_4[field][0] == '' or field_tab_4[field][0].isspace()):
            #         required_field.setStyleSheet(self.red_warning)
            #         alert_field.setVisible(True)
            #         self.pushButton.setText("Необходимо проверить вкладку Прочие сведения")
            #         self.pushButton.setEnabled(False)
            #         self.count_4 = 0

            #     elif field != 'self.characteristics' and field_tab_4[field][0] == '' or field_tab_4[field][0].isspace():
            #         required_field.setStyleSheet(self.red_warning)
            #         alert_field.setVisible(True)
            #         self.pushButton.setText("Необходимо проверить вкладку Прочие сведения")
            #         self.pushButton.setEnabled(False)
            #         self.count_4 = 0

            #     else:
            #         self.pushButton.setText("Создать заявку")
            #         self.pushButton.setEnabled(True)
            #         required_field.setStyleSheet("")
            #         self.count_4 = 1

            if self.checkBox_4.checkState() == 0 and self.temperature != '' and self.pressure != '' and self.hymidity != '':
                self.line_6.setVisible(False)
                #self.pushButton.setText("Создать заявку")
                #self.pushButton.setEnabled(True)
                self.count_4 = 1
            elif self.checkBox_4.isChecked() and self.characteristics != '' and self.temperature != '' and self.pressure != '' and self.hymidity != '':
                self.line_6.setVisible(False)
                #self.pushButton.setText("Создать заявку")
                self.count_4 = 1
            else:
                self.line_6.setVisible(True)
                #self.pushButton.setText("Необходимо заполнить обязательные поля")
                #self.pushButton.setEnabled(False)
                self.count_4 = 0

        self.start_to_create_application()
        print('self.count_4', self.count_4)
        return self.count_4

    def universal_fields_checker(self, field_tab):
        for field in field_tab.keys():
            required_field = field_tab[field][1]
            alert_field = field_tab[field][2]
            #Проход циклом по всем обязательным полям, выявление незаполненных обязательных полей
            if (field != 'self.reasons' and field != 'self.characteristics') and field_tab[field][0] == '' or field_tab[field][0].isspace():
                required_field.setStyleSheet(self.red_warning)
                alert_field.setVisible(True)
            elif (field == 'self.reasons' and self.radioButton_4.isChecked()) and (field_tab[field][0] == '' or field_tab[field][0].isspace()):
                required_field.setStyleSheet(self.red_warning)
                alert_field.setVisible(True)
            elif (field == 'self.characteristics' and self.checkBox_4.isChecked()) and (field_tab[field][0] == '' or field_tab[field][0].isspace()):
                required_field.setStyleSheet(self.red_warning)
                alert_field.setVisible(True)
                #self.pushButton.setText("Необходимо заполнить обязательные поля")
                #self.pushButton.setEnabled(False)
                #self.count = 0
                #self.pushButton.setText("Необходимо заполнить обязательные поля")
                #self.pushButton.setEnabled(False)
                #self.count = 0
                #self.pushButton.setText("Необходимо проверить вкладку Сведения о поверке")
                #self.count_2 = 0
            # elif field != 'self.reasons' and field_tab[field][0] == '' or field_tab[field][0].isspace():
            #     required_field.setStyleSheet(self.red_warning)
            #     alert_field.setVisible(True)
            #     #self.pushButton.setText("Необходимо проверить вкладку Сведения о поверке")
            #     #self.count_2 = 0

            else:
                #self.pushButton.setText("Создать заявку")
                required_field.setStyleSheet("")
                alert_field.setVisible(False)
                #self.count = 1
        #return self.count

    def universal_fields_checker_with_sender(self):
        sender = self.sender()
        print('sender', id(sender))
        print('self.counter_zav_number_2', type(self.counter_zav_number))
        if sender == self.lineEdit_4 and not type(self.counter_zav_number) is int:
            self.check_zav_number_is_int()
            self.label_9.setVisible(True)
            print('self.lineEdit_4')
        elif sender == self.lineEdit_4 and type(self.counter_zav_number) is int:
            self.label_9.setVisible(False)
        else:
            print('not self.lineEdit_4')
        is_lineEdit = isinstance(sender, QtWidgets.QLineEdit)
        is_textEdit = isinstance(sender, QtWidgets.QTextEdit)
        print('is_textEdit', is_textEdit)
        if is_lineEdit and (sender.text() == '' or sender.text().isspace()):
            sender.setStyleSheet(self.red_warning)
            #self.pushButton.setText("Необходимо заполнить обязательные поля")
            #self.pushButton.setEnabled(False)
        elif (is_textEdit and self.checkBox_4.isChecked()) and (sender.toPlainText() == '' or sender.toPlainText().isspace()):
            sender.setStyleSheet(self.red_warning)
            #self.pushButton.setText("Необходимо заполнить обязательные поля")
            #self.pushButton.setEnabled(False)
        else:
            sender.setStyleSheet("")
            #self.pushButton.setText("Создать заявку")

    def start_to_create_application(self):
        self.result = 0
        self.result = self.count_1 + self.count_2 + self.count_3 + self.count_4

        if self.result == 4:
            self.pushButton.setText("Создать заявку")
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setText("Необходимо заполнить обязательные поля")
            self.pushButton.setEnabled(False)


        print('self.result', self.result)

    def create(self):
        #Общее количество записей о поверках СИ
        TOTAL_RESULTS = int(self.spinBox.text())

        #Количество записей о поверках СИ в одной заявке (не более 4000 записей)
        RESULTS_IN_APP = int(self.spinBox_2.text())

        filepath = QtWidgets.QFileDialog.getExistingDirectory(self, "Каталог сохранения заявок")
        if filepath != '':

            self.pushButton.setVisible(False)
            self.progressBar.setVisible(True)

            parts = TOTAL_RESULTS // RESULTS_IN_APP # Вычисление количества заявок (Общее количество заявок делится без остатка на желаемое количество в одной заявке)
            if TOTAL_RESULTS % RESULTS_IN_APP != 0: # Если остаток от деления заявок на части не равен 0, то количество заявок увеличивается на 1.
                parts += 1

            set_progress = 0
            progress_value = 100 / (TOTAL_RESULTS / RESULTS_IN_APP)

            #Заводской номер СИ
            counter_zav_number = self.counter_zav_number

            for j in range(parts):
                if TOTAL_RESULTS <= RESULTS_IN_APP:
                    zav = self.applic_constructor(filepath, TOTAL_RESULTS, j + 1, counter_zav_number)
                elif TOTAL_RESULTS > RESULTS_IN_APP:
                    zav = self.applic_constructor(filepath, RESULTS_IN_APP, j + 1, counter_zav_number)
                    TOTAL_RESULTS -= RESULTS_IN_APP
                counter_zav_number = zav

                set_progress += progress_value
                if set_progress > 100:
                    set_progress = 100
                self.progressBar.setValue(round(set_progress))

            self.statusBar().showMessage('Формирование файлов завершено!')
            self.pushButton.setVisible(True)
            self.progressBar.setVisible(False)
            self.statusTimer()

    def statusTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.start(2500)
        self.timer.timeout.connect(self.clearStatusBar)
        self.timer.setSingleShot(True)                     #Таймер выполняется один раз

    def clearStatusBar(self):
        self.statusBar().clearMessage()

    # def closeEvent(self, event):                           #Запрос на закрытие программы
    #     reply = QMessageBox.question(self, 'Предупреждение',
    #         "Закрыть приложение?", QMessageBox.No |
    #         QMessageBox.No, QMessageBox.Yes)

    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()

    def keyPressEvent(self, e):                            #Выход из программы по Esc
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

        if e.key() in [QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return]:
            #self.create()
            self.start_to_create_application()


# StyleSheet
StyleSheet = """

Window{background: #b8cdee;}

QLineEdit {
    border: 2px solid gray;
    border-radius: 3px;
    padding: 0 8px;
    background: #ffffff;
    selection-background-color: darkgray;
}
QToolBox::tab {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
    border-radius: 5px;
    color: darkgray;
}

QToolBox::tab:selected { /* italicize selected tabs */
    font: italic;
    color: white;
}

QComboBox {
    border: 1px solid gray;
    border-radius: 3px;
    padding: 1px 18px 1px 3px;
    min-width: 6em;
    background: white;
}

QComboBox:editable {
    background: white;
}

QComboBox:!editable, QComboBox::drop-down:editable {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
}

/* QComboBox gets the "on" state when the popup is open */
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
}

QComboBox:on { /* shift the text when the popup opens */
    padding-top: 3px;
    padding-left: 4px;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;

    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid; /* just a single line */
    border-top-right-radius: 3px; /* same radius as the QComboBox */
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow {
    image: url(:/icons/strelka.ico);
}

QComboBox::down-arrow:on { /* shift the arrow when popup is open */
    top: 1px;
    left: 1px;
}

QComboBox QAbstractItemView {
    border: 2px solid darkgray;
    selection-background-color: lightgray;
}

QProgressBar {
    border: 2px solid grey;
    border-radius: 5px;
}

QProgressBar::chunk {
    background-color: #05B8CC;
    width: 20px;
}

QPushButton {
    border: 2px solid #8f8f91;
    border-radius: 6px;
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #f6f7fa, stop: 1 #dadbde);
    min-width: 80px;
}

QPushButton:pressed {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #dadbde, stop: 1 #f6f7fa);
}

QPushButton:flat {
    border: none; /* no border for a flat push button */
}

QPushButton:default {
    border-color: navy; /* make the default button prominent */
}

"""

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyleSheet(StyleSheet)
    window = main_window()
    window.show()
    sys.exit(app.exec_())