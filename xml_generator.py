import sys
import os
import errno

import res_rc

from datetime import datetime, date, time, timedelta
from PyQt5.QtCore import pyqtSignal, Qt, QDate, QDateTime, QTimer
from PyQt5.QtWidgets import QMainWindow, QWidget, QFileDialog, QToolTip, QPushButton, QApplication, QMessageBox
from PyQt5.QtGui import *
import MainWindow_poverki  #модуль главного окна PyQt
from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QPalette

class main_window(QMainWindow, MainWindow_poverki.Ui_MainWindow):

    def __init__(self, parent = None):
        super(main_window, self).__init__()
        self.setupUi(self)

        self.menuBar.setVisible(False)
        self.setWindowTitle("  ")
        self.logoTimer()

        self.progressBar.setVisible(False)
        self.dateEdit.setDateTime(QDateTime.currentDateTime())
        self.line_3.setVisible(False)
        self.line_3.setStyleSheet('color: red;')
        self.line_4.setVisible(False)
        self.line_4.setStyleSheet('color: red;')
        self.line_5.setVisible(False)
        self.line_5.setStyleSheet('color: red;')
        self.label_9.setVisible(False)
        self.label_9.setStyleSheet('color: red;')
        self.label_10.setVisible(False)
        self.label_10.setStyleSheet('color: red;')
        self.label_19.setVisible(False)
        self.label_19.setStyleSheet('color: red;')
        self.label_20.setVisible(False)
        self.label_20.setStyleSheet('color: red;')
        self.calendarWidget.setVisible(False)
        self.pushButton_3.setVisible(False)

        self.pushButton.clicked.connect(self.create)            #Запуск
        self.pushButton_2.clicked.connect(self.open_calend)
        self.pushButton_3.clicked.connect(self.close_calend)
        self.action.triggered.connect(self.info_page)
        self.action_3.triggered.connect(self.close)

    def info_page(self):
        msg = QMessageBox()
        msg.setWindowTitle("Информация")
        msg.setText("Программное обеспечение: Генератор файлов в формате XML для партий СИ")
        msg.setInformativeText(f"Разработчик: ФГУП \"ВНИИМС\"\nРаспространяется на безвозмездной основе\nВерсия программы: 1.2")
        #msg.setDetailedText(f"Распространяется на безвозмездной основе\nВерсия программы: 1.0")
        okButton = msg.addButton('Закрыть', QMessageBox.AcceptRole)
        #msg.addButton('Отмена', QMessageBox.RejectRole)
        
        msg.exec()

    def logoTimer(self):
        self.timer = QTimer()
        self.timer.start(5000)
        self.timer.timeout.connect(self.label_image)
        self.timer.setSingleShot(True)

    def label_image(self):
        self.label_23.setVisible(False)
        self.label_24.setVisible(False)
        self.label_25.setVisible(False)
        self.menuBar.setVisible(True)
        self.setWindowTitle("Генератор заявок")

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

    def valid_date(self):
        self.close_calend()
        self.lineEdit_6.setText(self.calendarWidget.selectedDate().toString("yyyy-MM-dd"))


    def complete_fields(self):
        #Тип СИ (№ Гос. реестра)
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
        self.tail_zav_number = self.lineEdit_5.text()

        #Номер свидетельства на СИ
        self.prefix_applic_number = self.lineEdit_8.text()
        self.counter_applic_number = self.lineEdit_9.text()
        self.tail_applic_number = self.lineEdit_10.text()

        #Условный шифр знака поверки
        signCipher = self.lineEdit_7.text()
        self.signCipher = signCipher.upper()

        #Дата поверки (формат гггг-мм-дд)
        self.vrfDate = self.dateEdit.text()

        #Дата действия поверки (формат гггг-мм-дд), можно оставить пустое значение ''
        self.validDate = self.lineEdit_6.text()

        #Методика поверки
        self.method = self.lineEdit_11.text()

        #Ф.И.О. поверителя
        self.metrologist = self.lineEdit_20.text()

        #Знак поверки в паспорте (true/false)
        signPass = f'{self.checkBox.isChecked()}'
        self.signPass = signPass.lower()

        #Знак поверки на СИ (true/false)
        signMi = f'{self.checkBox_2.isChecked()}'
        self.signMi = signMi.lower()

        #ГПЭ
        self.npe_number = self.lineEdit_12.text()

        #Эталоны
        self.uve_number = self.lineEdit_13.text()

        #Стандартные образцы
        self.ses_number = self.lineEdit_14.text()             # Тип СО

        self.ses_manufactureYear = int(self.spinBox_4.text()) # Год производства

        self.ses_manufactureNum = self.lineEdit_15.text()     # Заводской номер

        #СИ, применяемые в качестве эталонов
        self.mieta_number = self.lineEdit_16.text()

        #СИ, применяемые при поверке
        self.mis_number = self.lineEdit_17.text()             # Тип СИ (№ Гос. реестра)
        self.mis_manufactureNum = self.lineEdit_18.text()     # Заводской номер

        #Вещества (материалы)
        self.reagent_number = self.lineEdit_19.text()

        #Прочие сведения
        self.additional_info = self.textEdit_23.toPlainText()
        self.ranges = self.textEdit_19.toPlainText()
        self.values = self.textEdit_20.toPlainText()
        self.channels = self.textEdit_21.toPlainText()
        self.blocks = self.textEdit_22.toPlainText()

        fields = [self.mitypeNumber, self.modification, self.manufactureYear, self.prefix_zav_number, self.counter_zav_number, self.tail_zav_number, self.prefix_applic_number,
        self.counter_applic_number, self.tail_applic_number, self.signCipher, self.vrfDate, self.validDate, self.method, self.metrologist, self.signPass, self.signMi, self.npe_number,
        self.uve_number, self.ses_number, self.ses_manufactureYear, self.ses_manufactureNum, self.mieta_number, self.mis_number, self.mis_manufactureNum, self.reagent_number,
        self.additional_info, self.ranges, self.values, self.channels, self.blocks]

        return fields

    def applic_constructor(self, filepath, result, part, counter_zav, counter_applic):

        #Название файла
        name_of_file = r'заявка_' + self.mitypeNumber + '_часть_' + str(part) + '_записей_' + str(result) + '_шифр_' + self.signCipher + '.xml'

        #Путь сохранения файла
        FileFullPath = os.path.join(filepath, name_of_file)

        with open (FileFullPath, 'w', encoding='utf-8') as sample:

            header_1 = f'<?xml version="1.0" encoding="utf-8" ?>\n'
            header_2 = f'<gost:application xmlns:gost="urn://fgis-arshin.gost.ru/module-verifications/import/2020-04-14">\n'
            header = header_1 + header_2
            sample.write(header)

        for n in range(result):

            manufactureNum = self.prefix_zav_number + str(counter_zav).zfill(self.zav_len) + self.tail_zav_number
            certNum = self.prefix_applic_number + str(counter_applic).zfill(self.applic_len) + self.tail_applic_number

            with open (FileFullPath, 'a', encoding='utf-8') as sample_body:

                result_start = f'<gost:result>\n'
                miInfo_start = f'<gost:miInfo>\n'
                singleMI_start = f'<gost:singleMI>\n'
                mitypeNumber_str = f'<gost:mitypeNumber>{self.mitypeNumber}</gost:mitypeNumber>\n'
                manufactureNum_str = f'<gost:manufactureNum>{manufactureNum}</gost:manufactureNum>\n'
                manufactureYear_str = f'<gost:manufactureYear>{self.manufactureYear}</gost:manufactureYear>\n'
                modification_str = f'<gost:modification>{self.modification}</gost:modification>\n'
                singleMI_close = f'</gost:singleMI>\n'
                miInfo_close = f'</gost:miInfo>\n'

                if self.manufactureYear == '':
                    miInfo = miInfo_start + singleMI_start + mitypeNumber_str + manufactureNum_str + modification_str + singleMI_close + miInfo_close
                else:
                    miInfo = miInfo_start + singleMI_start + mitypeNumber_str + manufactureNum_str + manufactureYear_str + modification_str + singleMI_close + miInfo_close

                signCipher_str = f'<gost:signCipher>{self.signCipher}</gost:signCipher>\n'
                vrfDate_str = f'<gost:vrfDate>{self.vrfDate}+03:00</gost:vrfDate>\n'
                if self.validDate == '':
                    valid = signCipher_str + vrfDate_str
                else:
                    validDate_str = f'<gost:validDate>{self.validDate}+03:00</gost:validDate>\n'
                    valid = signCipher_str + vrfDate_str + validDate_str

                applicable_start = f'<gost:applicable>\n'
                certNum_str = f'<gost:certNum>{certNum}</gost:certNum>\n'
                signPass_str = f'<gost:signPass>{self.signPass}</gost:signPass>\n'
                signMi_str = f'<gost:signMi>{self.signMi}</gost:signMi>\n'
                applicable_close = f'</gost:applicable>\n'
                verification_res = applicable_start + certNum_str + signPass_str + signMi_str + applicable_close

                docTitle = f'<gost:docTitle>{self.method}</gost:docTitle>\n'

                if self.metrologist != '':
                    poveritel = f'<gost:metrologist>{self.metrologist}</gost:metrologist>\n'
                else:
                    poveritel = ''

                means_start = f'<gost:means>\n'

                npe = ''
                uve = ''
                ses = ''
                mieta = ''
                mis = ''
                reagent = ''

                if self.npe_number != '':
                    npe_start = f'<gost:npe>\n'
                    npe_number_str = f'<gost:number>{self.npe_number}</gost:number>\n'
                    npe_close = f'</gost:npe>\n'
                    npe = npe_start + npe_number_str + npe_close

                if self.uve_number != '':
                    uve_start = f'<gost:uve>\n'
                    uve_number_str = f'<gost:number>{self.uve_number}</gost:number>\n'
                    uve_close = f'</gost:uve>\n'
                    uve = uve_start + uve_number_str + uve_close

                if self.ses_number != '':
                    ses_start = f'<gost:ses>\n'
                    se_start = f'<gost:se>\n'
                    ses_number_str = f'<gost:typeNum>{self.ses_number}</gost:typeNum>\n'
                    ses_manufactureYear_str = f'<gost:manufactureYear>{self.ses_manufactureYear}</gost:manufactureYear>\n'
                    ses_manufactureNum_str = f'<gost:manufactureNum>{self.ses_manufactureNum}</gost:manufactureNum>\n'
                    se_close = f'</gost:se>\n'
                    ses_close = f'</gost:ses>\n'
                    ses = ses_start + se_start + ses_number_str + ses_manufactureYear_str + ses_manufactureNum_str + se_close + ses_close

                if self.mieta_number != '':
                    mieta_start = f'<gost:mieta>\n'
                    mieta_number_str = f'<gost:number>{self.mieta_number}</gost:number>\n'
                    mieta_close = f'</gost:mieta>\n'
                    mieta = mieta_start + mieta_number_str + mieta_close

                if self.mis_number != '':
                    mis_start =	f'<gost:mis>\n'
                    mi_start = f'<gost:mi>\n'
                    mis_number_str = f'<gost:typeNum>{self.mis_number}</gost:typeNum>\n'
                    mis_manufactureNum_str = f'<gost:manufactureNum>{self.mis_manufactureNum}</gost:manufactureNum>\n'
                    mi_close = f'</gost:mi>\n'
                    mis_close =	f'</gost:mis>\n'
                    mis = mis_start + mi_start + mis_number_str + mis_manufactureNum_str + mi_close + mis_close

                if self.reagent_number != '':
                    reagent_start =	f'<gost:reagent>\n'
                    reagent_number_str = f'<gost:number>{self.reagent_number}</gost:number>\n'
                    reagent_close =	f'</gost:reagent>\n'
                    reagent = reagent_start + reagent_number_str + reagent_close

                means_close = f'</gost:means>\n'

                additional_info_str = ''
                ranges_str = ''
                values_str = ''
                channels_str = ''
                blocks_str = ''

                if self.additional_info != '':
                    additional_info_str = f'<gost:additional_info>{self.additional_info}</gost:additional_info>\n'

                if self.ranges != '':
                    ranges_str = f'<gost:ranges>{self.ranges}</gost:ranges>\n'

                if self.values != '':
                    values_str = f'<gost:values>{self.values}</gost:values>\n'

                if self.channels != '':
                    channels_str = f'<gost:channels>{self.channels}</gost:channels>\n'

                if self.blocks != '':
                    blocks_str = f'<gost:blocks>{self.blocks}</gost:blocks>\n'

                result_close = f'</gost:result>\n'

                body = result_start + miInfo + valid + verification_res + docTitle + poveritel + means_start + npe + uve + ses + mieta + mis + reagent + means_close + additional_info_str + ranges_str + values_str + channels_str + blocks_str + result_close
                sample_body.write(body)

                counter_zav += 1
                counter_applic += 1


        with open (FileFullPath, 'a', encoding='utf-8') as sample:
            footer = f'</gost:application>\n'
            sample.write(footer)

        return counter_zav, counter_applic

    def check_zav_number_is_int(self):
        self.changeable_zav_number = self.lineEdit_4.text()
        self.zav_len = len(self.changeable_zav_number)
        self.counter_zav_number = int(self.changeable_zav_number)
        if type(self.counter_zav_number) == int:
            self.label_9.setVisible(False)
            return True
        else:
            return False

    def check_applic_number_is_int(self):
        self.changeable_applic_number = self.lineEdit_9.text()
        self.applic_len = len(self.changeable_applic_number)
        self.counter_applic_number = int(self.changeable_applic_number)
        if type(self.counter_applic_number) == int:
            self.label_10.setVisible(False)
            return True
        else:
            return False

    def check_fields(self):

        self.complete_fields()

        red_warning = "border-color: red; border-style: solid; border-width: 2px; font-weight: normal;"

        field_tab_1 = {'self.mitypeNumber': [self.mitypeNumber, self.lineEdit, self.line_3],
                       'self.modification': [self.modification, self.lineEdit_2, self.line_3],
                       'self.counter_zav_number': [self.counter_zav_number, self.lineEdit_4, self.line_3]}

        field_tab_2 = {'self.method': [self.method, self.lineEdit_11, self.line_4],
                       'self.signCipher': [self.signCipher, self.lineEdit_7, self.line_4],
                       'self.counter_applic_number': [self.counter_applic_number, self.lineEdit_9, self.line_4]}

        field_tab_3 = {'self.npe_number': [self.npe_number, self.lineEdit_12, self.line_5],
                       'self.uve_number': [self.uve_number, self.lineEdit_13, self.line_5],
                       'self.ses_number': [self.ses_number, self.lineEdit_14, self.line_5],
                       'self.mieta_number': [self.mieta_number, self.lineEdit_16, self.line_5],
                       'self.mis_number': [self.mis_number, self.lineEdit_17, self.line_5],
                       'self.reagent_number': [self.reagent_number, self.lineEdit_19, self.line_5]}

        ch_fields = [field_tab_1, field_tab_2, field_tab_3]

        count = 0

        for i in range(len(ch_fields)):
            count_1 = 0
            count_2 = 0
            count_3 = 0

            test = ch_fields[i]

            for k in test.keys():
                required_field = test[k][1]
                alert_field = test[k][2]
                #Проход циклом по всем полям, выявление незаполненных обязательных полей
                if test[k][0] == '' or test[k][0].isspace():
                    required_field.setFrame(False)
                    required_field.setStyleSheet(red_warning)
                    alert_field.setVisible(True)
                    self.pushButton.setText("Проверить обязательные поля")
                    #Для вкладки Средства поверки (если хотя бы одно поле заполнено, то для остальных полей убирается красная рамка и флаг над табом)
                    if test == field_tab_3 and (self.npe_number != '' or self.uve_number != '' or self.ses_number != '' or self.mieta_number != '' or self.mis_number != '' or self.reagent_number != ''):
                        self.line_5.setVisible(False)
                        for p in test.keys():
                            test[p][1].setFrame(True)
                            test[p][1].setStyleSheet("")
                        #Проверка: Если заполнено поле СИ, применяемые при поверке, то обязательно нужно ввести Зав номер СИ.
                        if self.mis_number != '' and self.mis_manufactureNum == '':
                            self.lineEdit_18.setFrame(False)
                            self.lineEdit_18.setStyleSheet(red_warning)
                            self.line_5.setVisible(True)
                            self.toolBox.setCurrentIndex(4)
                            count_3 = 0
                        else:
                            self.lineEdit_18.setFrame(True)
                            self.lineEdit_18.setStyleSheet("")

                else:
                    required_field.setFrame(True)
                    required_field.setStyleSheet("")
                    if self.mitypeNumber != '' and self.modification != '' and type(self.counter_zav_number) == int:
                        self.line_3.setVisible(False)
                        count_1 = 1
                    elif type(self.counter_zav_number) != int and 'self.counter_zav_number' in test:
                        try:
                            self.check_zav_number_is_int()
                        except ValueError:
                            self.label_9.setVisible(True)
                            self.lineEdit_4.setFrame(False)
                            self.lineEdit_4.setStyleSheet(red_warning)
                            alert_field.setVisible(True)
                            self.pushButton.setText("Проверить обязательные поля")
                            count_1 = 0
                    if self.method != '' and self.signCipher != '' and type(self.counter_applic_number) == int:
                        self.line_4.setVisible(False)
                        count_2 = 1
                    elif type(self.counter_applic_number) != int and 'self.counter_applic_number' in test:
                        try:
                            self.check_applic_number_is_int()
                        except ValueError:
                            self.label_10.setVisible(True)
                            self.lineEdit_9.setFrame(False)
                            self.lineEdit_9.setStyleSheet(red_warning)
                            alert_field.setVisible(True)
                            self.pushButton.setText("Проверить обязательные поля")
                            count_2 = 0
                    if self.npe_number != '' or self.uve_number != '' or self.ses_number != '' or self.mieta_number != '' or self.mis_number != '' or self.reagent_number != '':
                        self.line_5.setVisible(False)
                        count_3 = 1
                    if self.mis_number != '' and self.mis_manufactureNum == '':
                        count_3 = 0

                if self.validDate != '' and self.vrfDate == self.validDate:
                    self.label_20.setVisible(False)
                    self.label_19.setVisible(True)
                    self.line_4.setVisible(True)
                    count_2 = 0
                elif self.validDate != '' and self.vrfDate > self.validDate:
                    self.label_19.setVisible(False)
                    self.label_20.setVisible(True)
                    self.line_4.setVisible(True)
                    count_2 = 0
                else:
                    self.label_19.setVisible(False)
                    self.label_20.setVisible(False)
                    count_2 = 1

                    count = count_1 + count_2 + count_3

        if count == len(ch_fields):
            self.pushButton.setText("Создать заявки")
            return True
        else:
            return False

    def create(self):

        result = self.check_fields()

        if result == True:

            #Общее количество записей о поверках СИ
            TOTAL_RESULTS = int(self.spinBox.text())

            #Количество записей о поверках СИ в одной заявке (не более 5000 записей)
            RESULTS_IN_APP = int(self.spinBox_2.text())


            filepath = QFileDialog.getExistingDirectory(self, "Каталог сохранения заявок")
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
                #Номер свидетельства СИ
                counter_applic_number = self.counter_applic_number

                for j in range(parts):
                    if TOTAL_RESULTS <= RESULTS_IN_APP:
                        zav, applic = self.applic_constructor(filepath, TOTAL_RESULTS, j + 1, counter_zav_number, counter_applic_number)
                    elif TOTAL_RESULTS > RESULTS_IN_APP:
                        zav, applic = self.applic_constructor(filepath, RESULTS_IN_APP, j + 1, counter_zav_number, counter_applic_number)
                        TOTAL_RESULTS -= RESULTS_IN_APP
                    counter_zav_number = zav
                    counter_applic_number = applic

                    set_progress += progress_value
                    if set_progress > 100:
                        set_progress = 100
                    self.progressBar.setValue(round(set_progress))

                self.statusBar().showMessage('Формирование файлов завершено!')
                self.pushButton.setVisible(True)
                self.progressBar.setVisible(False)
                self.statusTimer()

    def statusTimer(self):
        self.timer = QTimer()
        self.timer.start(2500)
        self.timer.timeout.connect(self.clearStatusBar)
        self.timer.setSingleShot(True)                     #Таймер выполняется один раз

    def clearStatusBar(self):
        self.statusBar().clearMessage()

    def closeEvent(self, event):                           #Запрос на закрытие программы
        reply = QMessageBox.question(self, 'Предупреждение',
            "Закрыть приложение?", QMessageBox.No |
            QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):                            #Выход из программы по Esc
        if e.key() == Qt.Key_Escape:
            self.close()

        if e.key() in [Qt.Key_Enter, Qt.Key_Return]:
            self.create()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main_window()
    ex.show()
    app.exec()