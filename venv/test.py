from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import sys

#ui, _ = loadUiType('login.ui')
ui, _ = loadUiType('main.ui')

class MainApp(QMainWindow,ui):
    # 定义构造方法
    def __init__ (self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handle_ui_change()
        self.handle_buttons()

    # UI变化处理
    def handle_ui_change(self):
        # 隐藏右边的样式
        self.hide_themes()
        # 隐藏最上层的标签
        self.tabWidget.tabBar().setVisible(False)


    # 处理button的消息与槽的通讯
    def handle_buttons(self):
        self.themeButton.clicked.connect(self.show_themes)
        self.theme_change_Button.clicked.connect(self.hide_themes)

    # 处理主题的显示
    def show_themes(self):
        self.theme_groupBox.show()
    # 处理主题的隐藏
    def hide_themes(self):
        self.theme_groupBox.hide()

def main():
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
