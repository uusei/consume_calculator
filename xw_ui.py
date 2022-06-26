import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLabel
from PyQt5.QtGui import QMovie, QCursor
from PyQt5.QtCore import Qt
import myicon


class ui_xw(QWidget):
    __dragWin = False

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        try:
            # pyqt5设置窗体透明控件不透明
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
            # 加载gif动画
            self.movie = QMovie(":/pic/xw02.gif")
            self.lab = QLabel("", self)
            self.lab.setAlignment(Qt.AlignCenter)
            self.lab.setMovie(self.movie)
            # 播放gif动画
            self.movie.start()
            # 设置窗体位置和尺寸
            self.setGeometry(300, 300, 300, 500)
            self.center()
        except:
            pass

    def center(self):
        # 让窗体居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, e):
        self.__dragWin = True
        self.__dragWin_x = e.x()
        self.__dragWin_y = e.y()
        self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, e):
        # 移动gif题
        if self.__dragWin == True:
            pos = e.globalPos()
            self.move(pos.x() - self.__dragWin_x, pos.y() - self.__dragWin_y)

    def mouseReleaseEvent(self, e):
        self.__dragWin = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def mouseDoubleClickEvent(self, e):
        '''
        双击关闭程序
        :param e:
        :return:
        '''
        self.close()




