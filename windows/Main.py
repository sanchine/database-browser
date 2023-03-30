from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from utils.Database import Database
from windows.ERDiagram import ERDiagram
from windows.Table import Table
from pathlib import Path
import os
import sys

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        self.setWindowTitle("MainFrame")
        self.setGeometry(750, 300, 250, 450)

        self.select_database_btn = QtWidgets.QPushButton(self)
        self.select_database_btn.setText("Select database")
        self.select_database_btn.move(5, 5)
        self.select_database_btn.setFixedWidth(240)
        self.select_database_btn.clicked.connect(self.selectDatabaseFileName)

        self.database = None

        self.database_name_label = QtWidgets.QLabel(self)
        self.database_name_label.move(100, 50)
        self.database_name_label.setText("Unknown")

        self.tables_area = QtWidgets.QListWidget(self)
        self.tables_area.setGeometry(5, 100, 240, 200)
        self.tables_area.clicked.connect(self.showTableWindow)

        self.erschema_show_btn = QtWidgets.QPushButton(self)
        self.erschema_show_btn.setText("ER-Diagram")
        self.erschema_show_btn.move(5, 300)
        self.erschema_show_btn.clicked.connect(self.showERSchema)

        self.table_window = None
        self.erschema_window = None

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.select_database_btn)
        self.layout.addWidget(self.database_name_label)
        self.layout.addWidget(self.tables_area)
        self.layout.addWidget(self.erschema_show_btn)
        self.setLayout(self.layout)


    def showERSchema(self):
        self.erschema_window = ERDiagram(self.database)
        self.erschema_window.show()


    def showTableWindow(self, qmodelindex):
        table_name = self.tables_area.currentItem().text()
        about_table = self.database.getAbout(table_name)
        self.table_window = Table(table_name, about_table, self.database)
        self.table_window.show()


    def selectDatabaseFileName(self):
        dir = "/var/lib"
        fpath = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory", directory=dir))
        fname = fpath.split('/')[-1]
        if fname == "":
            return
        self.database = Database(fname)
        self.database_name_label.setText(fname)
        self.setGeometry(self.geometry().x(), self.geometry().y(), self.geometry().width() * 2, self.geometry().height())
        self.showDatabaseTables()


    def showDatabaseTables(self):
        self.tables_area.clear()
        if self.database:
            data = self.database.getTables()
        else:
            return
        tables = []
        i = 0
        for row in data:
            tables.append(row["Tables_in_" + self.database.name])
            self.tables_area.insertItem(i, tables[i])
            i += 1
