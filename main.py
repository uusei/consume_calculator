# code:utf-8
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
import calculator as ca
from electric_tool import Ui_MainWindow


class elec_func(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initate()
        # 初始化
        self.pushButton_6.clicked.connect(self.initate)
        self.pushButton.clicked.connect(self.pasteit)
        self.actioninfomatiation.triggered.connect(self.link_xw)
        self.pushButton_4.setToolTip("呃呃，其实是截图处理模块啦")
        self.pushButton_4.clicked.connect(self.shootit)
        # 线缆记点
        self.pushButton_2.clicked.connect(self.update_cable)
        self.lineEdit_5.returnPressed.connect(self.update_cable)  # 绑定键盘上回车键
        # 额外记点
        self.pushButton_3.clicked.connect(self.ex_cable)
        self.lineEdit_6.returnPressed.connect(self.ex_cable)  # 绑定键盘上回车键
        # 复制到剪贴板
        self.pushButton_5.clicked.connect(self.copyit)
        self.lineEdit_11.returnPressed.connect(self.copyit)  # 绑定键盘上回车键

    # 初始化 全部置零
    def initate(self):
        da1.k4n = 'K4N10012345'
        da1.now_time = 0
        da1.ex_time = 0
        da1.p_now = 0
        da1.add_p = 0
        da1.ex_p = 0
        da1.ca_min = 0
        da1.ca_h = 0.00
        da1.se_min = 0
        da1.se_h = 0.00
        da1.real_min = 0
        self.lineEdit.setText(str(da1.k4n))
        self.lineEdit_2.setText(str(da1.now_time))
        self.lineEdit_3.setText(str(da1.ex_time))
        self.lineEdit_4.setText(str(da1.p_now))
        self.lineEdit_5.setText(str(da1.add_p))
        self.lineEdit_6.setText(str(da1.ex_p))
        self.lineEdit_7.setText(str(da1.ca_min))
        self.lineEdit_8.setText(str(da1.ca_h))
        self.lineEdit_9.setText(str(da1.se_min))
        self.lineEdit_10.setText(str(da1.se_h))
        self.lineEdit_11.setText(str(da1.real_min))

    # 粘贴件号
    def pasteit(self):
        clipboard = QApplication.clipboard()
        self.lineEdit.setText(clipboard.text())

    # 线缆记点函数
    def update_cable(self):
        try:
            da1.p_now = int(mk1.lineEdit_4.text())
            da1.add_p = int(mk1.lineEdit_5.text())
            da1.p_now = ca.addit(da1.p_now, da1.add_p)
            da1.now_time = da1.p_now * 5
            mk1.lineEdit_4.setText(str(da1.p_now))
            mk1.lineEdit_2.setText(str(da1.now_time))
            mk1.lineEdit_5.setText('')
        except:
            self.reply = QMessageBox(QMessageBox.Question, "提示", "请输入整数数字")
            # 添加自定义按钮
            self.reply.addButton('知道了', QMessageBox.YesRole)
            self.reply.addButton('也不是不可以啦', QMessageBox.NoRole)
            self.reply.setWindowFlags(Qt.WindowStaysOnTopHint)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/pic/dwr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.reply.setWindowIcon(icon)
            # 设置消息框中内容前面的图标
            # self.reply.setIcon(1)
            self.reply.show()

    def ex_cable(self):
        # 计算操作
        da1.ex_p = int(mk1.lineEdit_6.text())
        da1.ex_time = da1.ex_p * 15
        da1.ca_min = ca.enoughtime(da1.now_time, da1.ex_time)
        da1.ca_h = round(da1.ca_min / 60, 2)
        da1.se_h = ca.changeit(da1.ca_h)
        da1.se_min = int(da1.se_h * 60)
        da1.real_min = int(da1.se_min - 15)
        # 设置空格
        mk1.lineEdit_3.setText(str(da1.ex_time))
        mk1.lineEdit_7.setText(str(da1.ca_min))
        mk1.lineEdit_8.setText(str(da1.ca_h))
        mk1.lineEdit_9.setText(str(da1.se_h))
        mk1.lineEdit_10.setText(str(da1.se_min))
        mk1.lineEdit_11.setText(str(da1.real_min))

    # 复制对应时间
    def copyit(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(str(da1.real_min))

    # 信息窗口
    def link_xw(self):
        import xw_ui
        self.xwin = xw_ui.ui_xw()
        self.xwin.show()

    # 截图工具和图像处理方法
    def shootit(self):
        # try:
            import shoot
            self.shin = shoot.WScreenShot()
            self.shin.show()
            self.shin.closed.connect(self.picpaste)
            # self.reply = QMessageBox(QMessageBox.Question, "提示", "请截取正确的电线")
            #  添加自定义按钮
            # self.reply.addButton('知道了', QMessageBox.YesRole)
            # self.reply.addButton('也不是不可以啦', QMessageBox.NoRole)
            # self.reply.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            # icon = QtGui.QIcon()
            # icon.addPixmap(QtGui.QPixmap(":/pic/dwr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            # self.reply.setWindowIcon(icon)
            # self.reply.show()

    def picpaste(self):
        import picform
        da1.p_now = int(mk1.lineEdit_4.text())
        da1.add_p = int(picform.picchange())
        da1.p_now = ca.addit(da1.p_now, da1.add_p)
        da1.now_time = da1.p_now * 5
        mk1.lineEdit_4.setText(str(da1.p_now))
        mk1.lineEdit_2.setText(str(da1.now_time))


class data1:
    def __init__(self, k4n, now_time, ex_time, p_now, add_p, ex_p, ca_min, ca_h, se_min, se_h, real_min):
        self.k4n = k4n  # 件号
        self.now_time = now_time  # 当前电路记录点
        self.ex_time = ex_time  # 附加时间
        self.p_now = p_now  # 电路点数
        self.add_p = add_p  # 计数增加点数
        self.ex_p = ex_p  # 附加点数
        self.ca_min = ca_min  # 计算时间 分钟
        self.ca_h = ca_h  # 计算时间 小时
        self.se_min = se_min  # 实际时间 分钟
        self.se_h = se_h  # 实际时间 小时
        self.real_min = real_min  # 扣除测试的时间


if __name__ == "__main__":
    da1 = data1('K4N10012345', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    app = QApplication(sys.argv)
    mk1 = elec_func()
    mk1.show()

    sys.exit(app.exec_())
