from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow


class ERDiagram(QMainWindow):
    def __init__(self, db):
        super(ERDiagram, self).__init__()

        self.setWindowTitle("ER Diagram")
        self.setGeometry(200, 300, 450, 450)

        self.database = db