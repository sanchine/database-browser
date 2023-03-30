from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from utils.Database import Database
from pathlib import Path
import os
import sys

class Table(QMainWindow):
    def __init__(self, name, info, db):
        super(Table, self).__init__()

        self.setWindowTitle(name)
        self.setGeometry(800, 300, 1200, 450)

        self.table = QtWidgets.QTableWidget(self)
        self.table.setGeometry(0, 0, 1200, 450)
        self.rows_count = info[0]
        self.cols_count = info[1]
        self.table.setRowCount(self.rows_count)
        self.table.setColumnCount(self.cols_count)
        self.table.setGeometry(0, 0, 600, 450)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        self.table.itemClicked.connect(self.getInfoAboutItem)

        self.info_bar = QtWidgets.QPlainTextEdit(self)
        self.info_bar.setGeometry(600, 0, 600, 450)

        self.database = db
        self.fields_info = db.getFieldsInfo(name)
        self.table_values = db.getTable(name)

        self.fields_list = []
        self.key_list = []
        self.extra_list = []
        self.fillTable()


    def getInfoAboutItem(self, it):
        print(it.text())


    def fillTable(self):
        for i in range(len(self.fields_info)):
            header = self.fields_info[i]['Field']
            if self.fields_info[i]['Key'] != "":
                header += " [" + self.fields_info[i]['Key'] + " | "
            if self.fields_info[i]['Extra'] != "":
                header += self.fields_info[i]['Extra'] + "]"
            self.fields_list.append(header)
        self.table.setHorizontalHeaderLabels(self.fields_list)

        for i in range(len(self.table_values)):
            j = 0
            for v in self.table_values[i].values():
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(v)))
                j += 1



