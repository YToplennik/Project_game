import sys
import time
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow, QLabel


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
        self.gameButton00.hide()
        self.Time.hide()

    def initUI(self):
        uic.loadUi('Game.ui', self)
        self.StartBtn.clicked.connect(self.StartGame)
        self.otschot = QLabel(self)

    def StartGame(self):
        self.StartBtn.hide()
        self.otschot.move(200, 200)
        self.otschot.resize(200, 20)
        self.game()

    def game(self):
        self.gaming = True
        timer = QtCore.QTimer()
        timer.timeout.connect(self.endGame)
        timer.start(1000)
        #while self.gaming:
            #lvl = 1
            #for i in range(lvl + 2):
                #for j in range(lvl + 2):
                    #pass


    def endGame(self):
        return None




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex0 = Lobby()
    ex0.show()
    sys.exit(app.exec())
