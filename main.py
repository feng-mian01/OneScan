import sys
import os
from PyQt5.QtWidgets import QApplication, QMessageBox
from ui.main_window import MainWindow
from utils.log_utils import logger

def check_env():
    #检查nmap环境
    config = configparser.ConfigParser()
    config.read('./config/scan_config.ini',encoding='utf-8')
    nmap_path = config.get('port_scan','nmap_path')
    if not os.path.exists(nmap_path):
        return False,f"nmap路劲不存在:{nmap_path}(请检查配置文件)"
    
    #检查dirsearch环境
    dirsearch_path = config.get('dir_path','dirsearch_path')
    if not os.path.exists(dirsearch_path):
        return False,f"dirsearch路径不存在:{dirsearch_path}(请检查配置文件)"
    
    #检查字典文件
    default_path = config.get('dir_scan','default_wordlists')
    if not os.path.exists(default_path):
        return False,f"dirsearch路径不存在:{default_path}(请检查配置文件)"
    
    return True,"环境检查通过"

if __name__ == '__main__':
    logger.info("程序启动")

    env_ok,env_msg = check_env()
    if not env_ok:
        logger.error(f"环境检查失败: {env_msg}")
        app = QApplication(None,"环境错误",env_msg)
        sys.exit(1)
    logger.info(env_msg)

    #；启动窗口
    app = QApplication(sys.argv)
    winodw = MainWindow()
    winodw.show()
    sys.exit(app.exit_())
