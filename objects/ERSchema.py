from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget


class ERSchema(QWidget):
    def __init__(self, db):
        super(ERSchema, self).__init__()

        self.setWindowTitle("ER Diagram")
        self.setGeometry(200, 300, 450, 450)

        self.database = db