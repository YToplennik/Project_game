import sys
import time
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Lobby(QMainWindow):
    def __init__(self, con):
        super(Lobby, self).__init__()
        self.initUI()
        self.con = con

    def initUI(self):
        uic.loadUi('untitled.ui', self)

        self.btnPlay.clicked.connect(self.openGame)
        self.Exit.clicked.connect(self.close)

    def openGame(self):
        self.Game = Game(self.con)
        self.Game.show()


class Game(QWidget):
    def __init__(self, coun):
        super(Game, self).__init__()
        self.initUI()
        self.hide_buttons()
        self.Gameover_text.hide()
        self.timeBar.setValue(100)
        self.count = coun

    def hide_buttons(self):
        self.gameButton_00.hide()
        self.gameButton_01.hide()
        self.gameButton_02.hide()
        self.gameButton_03.hide()

        self.gameButton_10.hide()
        self.gameButton_11.hide()
        self.gameButton_12.hide()
        self.gameButton_13.hide()

        self.gameButton_20.hide()
        self.gameButton_21.hide()
        self.gameButton_22.hide()
        self.gameButton_23.hide()

        self.gameButton_30.hide()
        self.gameButton_31.hide()
        self.gameButton_32.hide()
        self.gameButton_33.hide()

        self.gameButton_40.hide()
        self.gameButton_41.hide()
        self.gameButton_42.hide()
        self.gameButton_43.hide()

    def show_buttons(self):
        self.gameButton_00.show()
        self.gameButton_01.show()
        self.gameButton_02.show()
        self.gameButton_03.show()

        self.gameButton_10.show()
        self.gameButton_11.show()
        self.gameButton_12.show()
        self.gameButton_13.show()

        self.gameButton_20.show()
        self.gameButton_21.show()
        self.gameButton_22.show()
        self.gameButton_23.show()

        self.gameButton_30.show()
        self.gameButton_31.show()
        self.gameButton_32.show()
        self.gameButton_33.show()

        self.gameButton_40.show()
        self.gameButton_41.show()
        self.gameButton_42.show()
        self.gameButton_43.show()

        self.StartBtn.hide()
        self.StartBtn.resize(0, 0)

    def initUI(self):
        uic.loadUi('Game.ui', self)
        self.StartBtn.clicked.connect(self.StartGame)
        self.otschot = QLabel(self)

    def StartGame(self):
        self.timeText.setText(str(self.count))
        self.timeBar.setValue(self.count / (30 / 100))
        self.otschot.move(200, 200)
        self.otschot.resize(200, 20)
        self.game()
        self.show_buttons()

    def game(self):
        self.gaming = True
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Timeme)
        self.timer.start(1000)

    def Timeme(self):
        if self.count != 1:
            self.count -= 1
            self.timeText.setText(str(self.count))
            self.timeBar.setValue(int(self.count / (30 / 100)))
            print(self.count)
        else:
            self.timeText.setText(str(0))
            self.timeBar.setValue(int(0))
            self.endGame()
            print(self.count - 1)

    def endGame(self):
        self.gaming = False
        self.hide_buttons()
        self.Gameover_text.show()
        self.timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex0 = Lobby(10)
    ex0.show()
    sys.exit(app.exec())
