import sys
from PyQt5.QtWidgets import(QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox)
from PyQt5.QtCore import Qt
from ui.asset_ui import AssetWidget
from ui.port_ui import PortWidget
from ui.dir_ui import DirWidget
from utils.log_utils import logger

#主窗口
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    #窗口大小和标题
    def init_ui(self):
        self.setWindowTitle("ScanSight V1.0")
        self.setGeometry(100,100,1000,700)
    
    #标签页
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

    #子界面
        self.asset_widget = AssetWidget()
        self.port_widget = PortWidget()
        self.dir_widget = DirWidget()

    #子界面题目
        self.tab_widget.addTab(self.asset_widget,"资产收集")
        self.tab_widget.addTab(self.port_widget,"端口扫描")
        self.tab_widget.addTab(self.dir_widget,"目录扫描")
    
    #状态栏
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("就绪")

        logger.info("主窗口初始化完成")

    #关闭窗口
    def closeEvent(self,event):
        reply = QMessageBox.question(
            self,"确认退出","是否退出程序?",
            QMessageBox.Yes | QMessageBox.No,QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            logger.info("程序退出")
            event.accept()
        else:
            event.ignore()

#
if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())