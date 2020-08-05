# Владелец интеллектуальной собственности и разработчик данного программного обеспечения: Лошкарев Вадим Игоревич

import csv
from datetime import datetime, date, time, timedelta
import random
import os
import errno
import res_rc
import sys

import csv_to_xml  #модуль главного окна PyQt

from PyQt5.QtCore import pyqtSignal, Qt, QDate, QDateTime, QTimer
from PyQt5.QtWidgets import QMainWindow, QWidget, QFileDialog, QToolTip, QPushButton, QApplication, QMessageBox, QAction
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QPalette

class main_window(QMainWindow, csv_to_xml.Ui_MainWindow):

    data = []
    dict = {}

    def __init__(self, parent = None):
        super(main_window, self).__init__()
        self.setupUi(self)

        self.menuBar.setVisible(False)
        self.setWindowTitle("  ")
        self.statusTimer()
        self.lineEdit.setPlaceholderText('Выберите CSV-файл')

        self.lineEdit_2.setPlaceholderText((f"Путь сохранения по-умолчанию: {os.getcwd()}"))
        self.folder = os.getcwd()
        self.folder_xml = os.getcwd()
        self.pushButton_3.setEnabled(False)

        self.progressBar.setVisible(False)
        self.pushButton.clicked.connect(self.choose_file)            #Выбор файла

        self.pushButton_2.clicked.connect(self.choose_folder)
        self.pushButton_3.clicked.connect(self.do_convert)
        self.action.triggered.connect(self.info_page)
        self.action_3.triggered.connect(self.close)

    def info_page(self):
        msg = QMessageBox()
        msg.setWindowTitle("Информация")
        msg.setText("Программное обеспечение: Конвертер файлов из формата CSV в формат XML")
        msg.setInformativeText(f"Разработчик: ФГУП \"ВНИИМС\"\nРаспространяется на безвозмездной основе\nВерсия программы: 1.0")
        #msg.setDetailedText(f"Распространяется на безвозмездной основе\nВерсия программы: 1.0")
        okButton = msg.addButton('Закрыть', QMessageBox.AcceptRole)
        #msg.addButton('Отмена', QMessageBox.RejectRole)
        
        msg.exec()


    def statusTimer(self):
        self.timer = QTimer()
        self.timer.start(5000)
        self.timer.timeout.connect(self.label_image)
        self.timer.setSingleShot(True)

    def label_image(self):
        self.label.setVisible(False)
        self.label_2.setVisible(False)
        self.label_6.setVisible(False)
        self.menuBar.setVisible(True)
        self.setWindowTitle("Конвертер CSV в XML")

    def csv_reader(self, file_obj):
        """
        Read a csv file
        """

        reader = csv.reader(file_obj)
        for row in reader:
            row_1 = (" ".join(row))
            self.data.append(row_1.split(';'))

        return self.data


    def create_dict(self, csv_list):
        for n in range(len(csv_list[0])):
            self.dict[csv_list[0][n]] = csv_list[1][n]

        return self.dict

    def do_convert(self):
        self.pushButton.setVisible(False)
        csv_path = self.file
        file_name = os.path.splitext(self.filename_csv)[0]

        try:
            with open(csv_path, "r", encoding='utf-8') as f_obj:
                csv_list = self.csv_reader(f_obj)
                TOTAL_RESULTS = len(csv_list)-1

        except UnicodeDecodeError:
            with open(csv_path, "r") as f_obj:
                csv_list = self.csv_reader(f_obj)
                TOTAL_RESULTS = len(csv_list)-1


        #Количество записей о поверках СИ в одной заявке (не более 5000 записей)
        RESULTS_IN_APP = int(self.spinBox.text())

        parts = TOTAL_RESULTS // RESULTS_IN_APP # Вычисление количества заявок (Общее количество заявок делится без остатка на желаемое количество в одной заявке)
        if TOTAL_RESULTS % RESULTS_IN_APP != 0: # Если остаток от деления заявок на части не равен 0, то количество заявок увеличивается на 1.
            parts += 1

        set_progress = 0
        progress_value = 100 / (TOTAL_RESULTS / RESULTS_IN_APP)
        self.progressBar.setVisible(True)

        for j in range(parts):
            error = ''
            if TOTAL_RESULTS <= RESULTS_IN_APP:
                try:
                    self.converter(csv_list, file_name, TOTAL_RESULTS, j + 1)
                except (KeyError, PermissionError):
                    self.statusBar().showMessage('Ошибка, неверный формат данных в CSV')
                    error = 'True'
            elif TOTAL_RESULTS > RESULTS_IN_APP:
                try:
                    self.converter(csv_list, file_name, RESULTS_IN_APP, j + 1)
                    TOTAL_RESULTS -= RESULTS_IN_APP
                except (KeyError, PermissionError):
                    self.statusBar().showMessage('Ошибка, неверный формат данных в CSV')
                    error = 'True'

            set_progress += progress_value
            if set_progress > 100:
                set_progress = 100
            self.progressBar.setValue(round(set_progress))

        if error != 'True':
            self.statusBar().showMessage('Конвертирование файла завершено')
            self.spinBox.setValue(1)

        self.pushButton.setVisible(True)
        self.progressBar.setVisible(False)

        self.lineEdit.setText('')
        self.lineEdit.setPlaceholderText('Выберите CSV-файл')
        self.file = ''
        self.pushButton_3.setEnabled(False)
        self.data = []
        self.dict = {}


    def choose_file(self):
        self.file = QFileDialog.getOpenFileName(self, "Выбрать CSV-файл", '*.csv')[0]
        if self.file != '':
            self.pushButton_3.setEnabled(True)
            self.statusBar().clearMessage()
        self.filename_csv = os.path.basename(self.file)
        self.lineEdit.setText(self.filename_csv)

        return self.filename_csv, self.file

    def choose_folder(self):
        self.folder_xml = QFileDialog.getExistingDirectory(self, "Каталог сохранения заявок")
        self.lineEdit_2.setText(self.folder_xml)
        return self.folder_xml

    def converter(self, csv_data, xml_name, result, part):

        self.data_for_xml = self.create_dict(csv_data)
        #Для контроля использую Условный шифр знака поверки, если такого ключа нет в словаре, формат файла не совпадает
        signCipher_element = self.data_for_xml["signCipher"].upper()

        if self.folder_xml != self.folder:
            self.folder = self.folder_xml

        try:
            self.path_for_files = self.folder + '/' + xml_name
            os.makedirs(self.path_for_files)
        except OSError:
            self.path_for_files = self.folder + '/' + xml_name

        #Префикс названия файла
        prefix = f'{xml_name}_'

        #Название файла
        self.name_of_file = f'{prefix}записей_{str(result)}_part_{part}.xml'

        FileFullPath = os.path.join(self.path_for_files, self.name_of_file)  #Путь сохранения файла

        with open (FileFullPath, 'w', encoding='utf-8') as sample:

            header_1 = f'<?xml version="1.0" encoding="utf-8" ?>\n'
            header_2 = f'<gost:application xmlns:gost="urn://fgis-arshin.gost.ru/module-verifications/import/2020-04-14">\n'
            header = header_1 + header_2
            sample.write(header)

        with open (FileFullPath, 'a', encoding='utf-8') as sample_body:

            for i in range(result):

                self.data_for_xml = self.create_dict(csv_data)

                #Условный шифр знака поверки
                signCipher_element = self.data_for_xml["signCipher"].upper()

                #Модификация СИ и Тип СИ
                mitypeNumber = self.data_for_xml['mitypeNumber']
                modification = self.data_for_xml['modification']


                manufactureNum = self.data_for_xml['manufactureNum']     #Заводской номер СИ
                manufactureYear_csv = self.data_for_xml['manufactureYear']   #Дата производства СИ

                result_start = f'<gost:result>\n'
                miInfo_start = f'<gost:miInfo>\n'
                singleMI_start = f'<gost:singleMI>\n'
                mitypeNumber = f'<gost:mitypeNumber>{mitypeNumber}</gost:mitypeNumber>\n'
                manufactureNum = f'<gost:manufactureNum>{manufactureNum}</gost:manufactureNum>\n'
                manufactureYear = f'<gost:manufactureYear>{manufactureYear_csv}</gost:manufactureYear>\n'
                modification = f'<gost:modification>{modification}</gost:modification>\n'
                singleMI_close = f'</gost:singleMI>\n'
                miInfo_close = f'</gost:miInfo>\n'

                if manufactureYear_csv != '':
                    miInfo = miInfo_start + singleMI_start + mitypeNumber + manufactureNum + manufactureYear + modification + singleMI_close + miInfo_close
                else:
                    miInfo = miInfo_start + singleMI_start + mitypeNumber + manufactureNum + modification + singleMI_close + miInfo_close

                verification_marker = self.data_for_xml['applicable']  # (пригодно, непригодно)

                try:
                    datePov = self.data_for_xml['vrfDate']
                    vrfDate = datetime.strptime(datePov, '%d.%m.%Y').date()       #Отформатированная дата поверки

                    dateNextPov = self.data_for_xml['validDate']
                    validDate = datetime.strptime(dateNextPov, '%d.%m.%Y').date() #Отформатированная дата действия поверки
                except ValueError:
                    datePov = self.data_for_xml['vrfDate']
                    vrfDate = datetime.strptime(datePov, '%Y-%m-%d').date()       #Отформатированная дата поверки

                    dateNextPov = self.data_for_xml['validDate']
                    validDate = datetime.strptime(dateNextPov, '%Y-%m-%d').date() #Отформатированная дата действия поверки


                if verification_marker.lower() == 'пригодно':
                    signCipher = f'<gost:signCipher>{signCipher_element}</gost:signCipher>\n'
                    vrfDate = f'<gost:vrfDate>{vrfDate}+03:00</gost:vrfDate>\n'
                    validDate = f'<gost:validDate>{validDate}+03:00</gost:validDate>\n'

                    valid = signCipher + vrfDate + validDate

                    certNum = self.data_for_xml['certNum']   #Номер свидетельства на СИ

                    if self.data_for_xml['signPass'].lower() == 'да':
                        signPass = 'true'
                    else:
                        signPass = 'false'

                    if self.data_for_xml['signMi'].lower() == 'да':
                        signMi = 'true'
                    else:
                        signMi = 'false'                                #Знак поверки на СИ


                    applicable_start = f'<gost:applicable>\n'
                    certNum = f'<gost:certNum>{certNum}</gost:certNum>\n'
                    signPass = f'<gost:signPass>{signPass}</gost:signPass>\n'
                    signMi = f'<gost:signMi>{signMi}</gost:signMi>\n'
                    applicable_close = f'</gost:applicable>\n'
                    verification_res = applicable_start + certNum + signPass + signMi + applicable_close

                elif verification_marker.lower() == 'непригодно' or self.data_for_xml['noticeNum'] != '':
                    signCipher = f'<gost:signCipher>{signCipher_element}</gost:signCipher>\n'
                    vrfDate = f'<gost:vrfDate>{vrfDate}+03:00</gost:vrfDate>\n'

                    valid = signCipher + vrfDate

                    inapplicable_start = f'<gost:inapplicable>\n'
                    noticeNum = f'<gost:noticeNum>{self.data_for_xml["noticeNum"]}</gost:noticeNum>\n' #Номер извещения о непригодности СИ
                    inapplicable_close = f'</gost:inapplicable>\n'
                    verification_res = inapplicable_start + noticeNum + inapplicable_close

                docTitle = f'<gost:docTitle>{self.data_for_xml["docTitle"]}</gost:docTitle>\n'

                means_start = f'<gost:means>\n'

                npe = ''
                if self.data_for_xml['npe'] != '':
                    text = self.data_for_xml['npe'].rstrip('|')
                    text = text.split('|')
                    npe_list = ''
                    npe_start = f'<gost:npe>\n'
                    for t in text:
                        npe_number = f'<gost:number>{t}</gost:number>\n'
                        npe_list += npe_number
                    npe_close = f'</gost:npe>\n'

                    npe = npe_start + npe_list + npe_close

                uve = ''
                if self.data_for_xml['uve'] != '':
                    text = self.data_for_xml['uve'].rstrip('|')
                    text = text.split('|')
                    uve_list = ''
                    uve_start = f'<gost:uve>\n'
                    for t in text:
                        uve_number = f'<gost:number>{t}</gost:number>\n'
                        uve_list += uve_number
                    uve_close = f'</gost:uve>\n'

                    uve = uve_start + uve_list + uve_close

                ses = ''
                if self.data_for_xml['ses'] != '':
                    text = self.data_for_xml['ses'].rstrip('|')
                    text = text.split('|')
                    count = 1
                    se_list = ''
                    ses_start = f'<gost:ses>\n'
                    for i in range(len(text)):
                        text_list = text[i].split('*')
                        for t in text_list:
                            if count == 1:
                                se_start = f'<gost:se>\n'
                                typeNum = f'<gost:typeNum>{t}</gost:typeNum>\n'
                                se_many = se_start + typeNum
                            if count == 2:
                                ses_manufactureYear = f'<gost:manufactureYear>{t}</gost:manufactureYear>\n'
                                se_many = ses_manufactureYear
                            if count == 3:
                                ses_manufactureNum = f'<gost:manufactureNum>{t}</gost:manufactureNum>\n'
                                count = 0
                                se_close = f'</gost:se>\n'
                                se_many = ses_manufactureNum + se_close
                            count += 1

                            se_list += se_many
                    ses_close = f'</gost:ses>\n'
                    ses = ses_start + se_list + ses_close

                mieta = ''
                if self.data_for_xml['mieta'] != '':
                    text = self.data_for_xml['mieta'].rstrip('|')
                    text = text.split('|')
                    mieta_list = ''
                    mieta_start = f'<gost:mieta>\n'
                    for t in text:
                        mieta_number = f'<gost:number>{t}</gost:number>\n'
                        mieta_list += mieta_number
                    mieta_close = f'</gost:mieta>\n'

                    mieta = mieta_start + mieta_list + mieta_close

                mis = ''
                if self.data_for_xml['mis'] != '':
                    text = self.data_for_xml['mis'].rstrip('|')
                    text = text.split('|')
                    count = 1
                    mi_list = ''
                    mis_start =	f'<gost:mis>\n'
                    for i in range(len(text)):
                        text_list = text[i].split('*')
                        for t in text_list:
                            if count == 1:
                                mi_start = f'<gost:mi>\n'
                                typeNum = f'<gost:typeNum>{t}</gost:typeNum>\n'
                                mi_many = mi_start + typeNum
                            if count == 2:
                                mieta_manufactureNum = f'<gost:manufactureNum>{t}</gost:manufactureNum>\n'
                                count = 0
                                mi_close = f'</gost:mi>\n'
                                mi_many = mieta_manufactureNum + mi_close
                            count += 1

                            mi_list += mi_many
                    mis_close =	f'</gost:mis>\n'
                    mis = mis_start + mi_list + mis_close

                means_close = f'</gost:means>\n'

                additional_info = ''
                ranges = ''
                values = ''
                channels = ''
                blocks = ''

                if {self.data_for_xml['additional_info']} != '':
                    additional_info = f'<gost:additional_info>{self.data_for_xml["additional_info"]}</gost:additional_info>\n'

                if {self.data_for_xml['ranges']} != '':
                    ranges = f'<gost:ranges>{self.data_for_xml["ranges"]}</gost:ranges>\n'

                if {self.data_for_xml['values']} != '':
                    values = f'<gost:values>{self.data_for_xml["values"]}</gost:values>\n'

                if {self.data_for_xml['channels']} != '':
                    channels = f'<gost:channels>{self.data_for_xml["channels"]}</gost:channels>\n'

                if {self.data_for_xml['blocks']} != '':
                    blocks = f'<gost:blocks>{self.data_for_xml["blocks"]}</gost:blocks>\n'

                result_close = f'</gost:result>\n'


                body = result_start + miInfo + valid + verification_res + docTitle + means_start + npe + uve + ses + mieta + mis + means_close + additional_info + ranges + values + channels + blocks + result_close
                sample_body.write(body)

                csv_data.remove(csv_data[1])

                self.data_for_xml.clear()


            with open (FileFullPath, 'a', encoding='utf-8') as sample:
                footer = f'</gost:application>\n'
                sample.write(footer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = main_window()
    ex.show()
    app.exec()