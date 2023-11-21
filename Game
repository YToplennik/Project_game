import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow


class Lobby(QMainWindow):
    def __init__(self):
        super(Lobby, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Lobby')
        self.setGeometry(750, 250, 400, 550)

        self.btnPlay = QPushButton("Play", self)
        self.btnPlay.resize(100, 100)
        self.btnPlay.move(150, 180)

        self.btnLiders = QPushButton("Лидеры", self)
        self.btnLiders.resize(60, 60)
        self.btnLiders.move(75, 240)

        self.btnSkins = QPushButton("скины", self)
        self.btnSkins.resize(60, 60)
        self.btnSkins.move(265, 240)

        self.btnPlay.clicked.connect(self.openGame)
        self.btnPlay.clicked.connect(self.closeLobby)

    def openGame(self):
        self.Game = Game()
        self.Game.show()

    def closeLobby(self):
        self.closeLobby = Lobby()
        self.closeLobby.close()


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
