import sys
import time
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Lobby(QMainWindow):
    def __init__(self):
        super(Lobby, self).__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('untitled.ui', self)

        self.btnPlay.clicked.connect(self.openGame)
        self.Exit.clicked.connect(self.close)

    def openGame(self):
        self.Game = Game()
        self.Game.show()


class Game(QWidget):
    def __init__(self):
        super(Game, self).__init__()
        self.initUI()
        self.gameButton00.hide()
        self.timeBar.setValue(100)
        self.count = 15

    def initUI(self):
        uic.loadUi('Game.ui', self)
        self.StartBtn.clicked.connect(self.StartGame)
        self.otschot = QLabel(self)

    def StartGame(self):
        self.timeText.setText(str(self.count))
        self.timeBar.setValue(50)
        self.StartBtn.hide()
        self.otschot.move(200, 200)
        self.otschot.resize(200, 20)
        self.game()

    def game(self):
        self.gaming = True
        timer = QTimer(self)
        timer.timeout.connect(self.Timeme)
        timer.start(1000)

    def Timeme(self):
        if self.count != 0:
            self.count -= 1
            self.timeText.setText(str(self.count))
            self.timeBar.setValue(self.count / (30 / 100))
            print(self.count)
        else:
            self.endGame()

    def endGame(self):
        self.gaming = False



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex0 = Lobby()
    ex0.show()
    sys.exit(app.exec())
