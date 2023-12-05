import sys
import sqlite3
import random
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import tkinter as tk
from tkinter import simpledialog


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
        ROOT = tk.Tk()

        ROOT.withdraw()
        self.USER_INP = simpledialog.askstring(title="Test",
                                          prompt="Как тебя зовут?:")
        if self.USER_INP:
            self.Game = Game(self.con, self.USER_INP)
            self.Game.show()


class Game(QWidget):
    def __init__(self, coun, user):
        super(Game, self).__init__()
        self.initUI()
        self.user = user
        self.color_True = (random.choice([255, 0]), 255, random.choice([255, 0]))
        self.hide_buttons_and_connect()
        self.setButtonColorBase()
        self.Gameover_text.hide()
        self.timeBar.setValue(100)
        self.count = coun

    def hide_buttons_and_connect(self):
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
        self.gameButton_True.hide()

        # коннектим неправильные кнопки
        self.gameButton_00.clicked.connect(self.FalseButton)
        self.gameButton_01.clicked.connect(self.FalseButton)
        self.gameButton_02.clicked.connect(self.FalseButton)
        self.gameButton_03.clicked.connect(self.FalseButton)

        self.gameButton_10.clicked.connect(self.FalseButton)
        self.gameButton_11.clicked.connect(self.FalseButton)
        self.gameButton_12.clicked.connect(self.FalseButton)
        self.gameButton_13.clicked.connect(self.FalseButton)

        self.gameButton_20.clicked.connect(self.FalseButton)
        self.gameButton_21.clicked.connect(self.FalseButton)
        self.gameButton_22.clicked.connect(self.FalseButton)
        self.gameButton_23.clicked.connect(self.FalseButton)

        self.gameButton_30.clicked.connect(self.FalseButton)
        self.gameButton_31.clicked.connect(self.FalseButton)
        self.gameButton_32.clicked.connect(self.FalseButton)
        self.gameButton_33.clicked.connect(self.FalseButton)

        self.gameButton_40.clicked.connect(self.FalseButton)
        self.gameButton_41.clicked.connect(self.FalseButton)
        self.gameButton_42.clicked.connect(self.FalseButton)

    def setButtonColorBase(self):
        # Устанавливаем цвет кнопок
        self.gameButton_00.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_01.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_02.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_03.setStyleSheet('background-color: #FFFFFF')

        self.gameButton_10.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_11.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_12.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_13.setStyleSheet('background-color: #FFFFFF')

        self.gameButton_20.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_21.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_22.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_23.setStyleSheet('background-color: #FFFFFF')

        self.gameButton_30.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_31.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_32.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_33.setStyleSheet('background-color: #FFFFFF')

        self.gameButton_40.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_41.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_42.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_True.setStyleSheet(f'background-color: rgb{self.color_True}')

    def setButtonColor(self):
        if self.lvl > 0:
            b = self.randomColor()
            self.gameButton_00.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_00', b)
        if self.lvl > 1:
            b = self.randomColor()
            self.gameButton_01.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_01', b)
        if self.lvl > 2:
            b = self.randomColor()
            self.gameButton_02.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_02', b)
        if self.lvl > 3:
            b = self.randomColor()
            self.gameButton_03.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_03', b)
        if self.lvl > 4:
            b = self.randomColor()
            self.gameButton_10.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_10', b)
        if self.lvl > 5:
            b = self.randomColor()
            self.gameButton_11.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_11', b)
        if self.lvl > 6:
            b = self.randomColor()
            self.gameButton_12.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_12', b)
        if self.lvl > 7:
            b = self.randomColor()
            self.gameButton_13.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_13', b)
        if self.lvl > 8:
            b = self.randomColor()
            self.gameButton_20.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_20', b)
        if self.lvl > 9:
            b = self.randomColor()
            self.gameButton_21.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_21', b)
        if self.lvl > 10:
            b = self.randomColor()
            self.gameButton_22.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_22', b)
        if self.lvl > 11:
            b = self.randomColor()
            self.gameButton_23.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_23', b)
        if self.lvl > 12:
            b = self.randomColor()
            self.gameButton_30.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_30', b)
        if self.lvl > 13:
            b = self.randomColor()
            self.gameButton_31.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_31', b)
        if self.lvl > 14:
            b = self.randomColor()
            self.gameButton_32.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_32', b)
        if self.lvl > 15:
            b = self.randomColor()
            self.gameButton_33.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_33', b)
        if self.lvl > 16:
            b = self.randomColor()
            self.gameButton_40.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_40', b)
        if self.lvl > 17:
            b = self.randomColor()
            self.gameButton_41.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_41', b)
        if self.lvl > 18:
            b = self.randomColor()
            self.gameButton_42.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_42', b)

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
        self.gameButton_True.show()

        self.StartBtn.hide()
        self.StartBtn.resize(0, 0)

    def initUI(self):
        self.lvl = 0
        db = "BD.sqlite"
        con = sqlite3.connect(db)
        cur = con.cursor()
        uic.loadUi('Game.ui', self)
        self.StartBtn.clicked.connect(self.StartGame)
        self.tab = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radioButtonTxt)
        self.button_group.addButton(self.radioButtonRGB)
        self.button_group.buttonClicked.connect(self.radio)

    def StartGame(self):
        self.gameButton_True.clicked.connect(self.TrueButton)
        self.timeText.setText(str(self.count))
        self.radioButtonRGB.hide()
        self.radioButtonTxt.hide()
        self.timeBar.setValue(self.count / (30 / 100))
        self.game()
        self.show_buttons()
        self.new_lvl()

    def game(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Timeme)
        self.timer.start(1000)

    def randomColor(self):
        return random.choice([255, 0]), random.choice([255, 0]), random.choice([255, 0])

    def Timeme(self):
        if self.count > 1:
            self.count -= 1
            self.timeText.setText(str(self.count))
            self.timeBar.setValue(int(self.count / (30 / 100)))
            # print(self.count)
        else:
            self.timeText.setText(str(0))
            self.timeBar.setValue(int(0))
            self.endGame()
            # print(self.count - 1)

    def radio(self, button):
        if button.text() == 'Текстовый режим':
            self.rezim = 'txt'
        elif button.text() == 'RGB режим':
            self.rezim = 'rgb'
        self.StartBtn.setEnabled(True)

    def randomFalseText(self, a, col):
        flag = True
        while flag:
            g = self.randomColor()
            eval(a).setText(f'{g}')
            if col == (0, 0, 0) or col == (0, 0, 255):
                eval(a).setStyleSheet(f'background-color: rgb{col}; color: white;')
            else:
                eval(a).setStyleSheet(f'background-color: rgb{col}; color: black;')
            if g != col:
                flag = False
        self.rgbInText(g, a)

    def rgbInText(self, g, a):
        if self.rezim == 'txt':
            if g == (0, 0, 0):
                eval(a).setText('Чёрный')
            elif g == (255, 0, 0):
                eval(a).setText('Красный')
            elif g == (0, 255, 0):
                eval(a).setText('Зелёный')
            elif g == (0, 0, 255):
                eval(a).setText('Синий')
            elif g == (255, 0, 255):
                eval(a).setText('Розовый')
            elif g == (0, 255, 255):
                eval(a).setText('Голубой')
            elif g == (255, 255, 255):
                eval(a).setText('Белый')
            elif g == (255, 255, 0):
                eval(a).setText('Жёлтый')
        elif self.rezim == 'rgb':
            if g == (0, 0, 0):
                eval(a).setText('0 0 0')
            elif g == (255, 0, 0):
                eval(a).setText('255 0 0')
            elif g == (0, 255, 0):
                eval(a).setText('0 255 0')
            elif g == (0, 0, 255):
                eval(a).setText('0 0 255')
            elif g == (255, 0, 255):
                eval(a).setText('255 0 255')
            elif g == (0, 255, 255):
                eval(a).setText('0 255 255')
            elif g == (255, 255, 255):
                eval(a).setText('255 255 255')
            elif g == (255, 255, 0):
                eval(a).setText('255 255 0')

    def TrueButton(self):
        if self.count + 5 <= 30:
            self.count += 5
            self.timeBar.setValue(int(self.count / (30 / 100)))
            self.timeText.setText(str(self.count))
        else:
            self.count = 30
            # print('Больше')
            self.timeBar.setValue(int(self.count / (30 / 100)))
            self.timeText.setText(str(self.count))
        self.lvl_text.setText(str(self.lvl))
        self.new_lvl()

    def new_lvl(self):
        self.lvl += 1
        self.setButtonColor()
        ok = True
        for y in range(4):
            for x in range(5):
                try:
                    # eval('self.gameButton_{}'.format(str(x) + str(y))).setText(str(x) + str(y))

                    while ok:
                        self.rx, self.ry = random.choice(range(0, 4)), random.choice(range(0, 5))
                        if self.tab[self.ry][self.rx] != self.lvl:
                            # print(f'x={self.rx}, y={self.ry}')
                            self.tab[self.ry][self.rx] = self.lvl
                            ok = False
                    eval('self.gameButton_{}'.format(str(x) + str(y))).move(30 + self.rx * 100, 60 + self.ry * 100)
                    ok = True
                # Для True_Button
                except Exception:
                    while ok:
                        self.rx, self.ry = random.choice(range(0, 4)), random.choice(range(0, 5))
                        if self.tab[self.ry][self.rx] != self.lvl:
                            self.tab[self.ry][self.rx] = self.lvl
                            ok = False
                    self.gameButton_True.move(30 + self.rx * 100, 60 + self.ry * 100)
                    self.color_True = (random.choice([255, 0]), random.choice([255, 0]), random.choice([255, 0]))
                    self.gameButton_True.setText(f'{self.color_True}')
                    if self.color_True == (0, 0, 0) or self.color_True == (0, 0, 255):
                        self.gameButton_True.setStyleSheet(f'background-color: rgb{self.color_True}; color: white;')
                    else:
                        self.gameButton_True.setStyleSheet(f'background-color: rgb{self.color_True}; color: black;')
                    self.rgbInText(self.color_True, 'self.gameButton_True')

    def FalseButton(self):
        if self.count - 5 > 0:
            self.count -= 5
            self.timeBar.setValue(int(self.count / (30 / 100)))
            self.timeText.setText(str(self.count))
        else:
            self.endGame()
            self.timeBar.setValue(0)
            self.timeText.setText(str(0))

    def endGame(self):
        self.hide_buttons_and_connect()
        self.Gameover_text.show()
        self.timer.stop()
        a = None
        con = sqlite3.connect('BD.sqlite')
        cur = con.cursor()
        name = self.user
        score = self.lvl

        result = cur.execute(f"""SELECT max_result FROM players
                    WHERE player = '{name}' """)
        for res in result:
            for prov in res:
                self.prov = prov
            a = True
        if not a:
            cur.execute(f'''INSERT INTO players(player, max_result) VALUES('{name}', {score - 1})''')
            print('Добавлен игрок')

        if a and self.prov < self.lvl:
            cur.execute(f"""UPDATE players SET max_result = {score - 1} WHERE player = '{name}'""")
            print('Результат обновлён')

        con.commit()
        con.close()


class Liders(QWidget):
    def __init__(self):
        super(Liders, self).__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex0 = Lobby(20)
    ex0.show()
    sys.exit(app.exec())
