import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow


class Lobby(QMainWindow):
    def __init__(self):
        super(Lobby, self).__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('untitled.ui', self)

        self.btnPlay.clicked.connect(self.openGame)

    def openGame(self):
        self.Game = Game()
        self.Game.show()


class Game(QWidget):
    def __init__(self):
        super(Game, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Game')
        self.setGeometry(300, 300, 300, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex0 = Lobby()
    ex0.show()
    sys.exit(app.exec())
