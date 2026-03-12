from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTextEdit, QLabel, QSpinBox
from core.asset_collector import AssetCollector
from utils.log_utils import logger

class AssetWidget(QWidget):
    def __init__(self,):
        super().__init__()
        self.collector = AssetWidget()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        #查询条件输入
        query_layout = QHBoxLayout()
        query_layout.addWidget(QLabel("fofa查询语句"))
        self.query_edit = QLineEdit()
        self.query_edit.setPlaceholderText('示例: domain="baidu.com"')
        query_layout.addChildWidget(self.query_edit)
        layout.addLayout(query_layout)

        #页码/数量设置
        page_layout = QHBoxLayout()
        page_layout.addWidget(QLabel("页码: "))
        self.page_spin = QSpinBox()
        self.page_spin.setRange(1,100)
        self.page_spin.setValue(1)
        page_layout.addWidget(self.page_spin)

        page_layout.addWidget(QLabel("每页数量: "))
        self.size_spin = QSpinBox()
        self.size_spin.setRange(1,1000)
        self.size_spin.setValue(100)
        page_layout.addWidget(self.size_spin)
        layout.addLayout(page_layout)

        #扫描按钮
        self.scan_btn = QPushButton("开始收集")
        self.scan_btn.clicked.connect(self.collect_asset)
        layout.addWidget(self.scan_btn)

        #结果显示
        layout.addWidget(QLabel("收集信息: "))
        self.result_edit = QTextEdit()
        self.result_edit.setReadOnly(True)
        layout.addWidget(self.result_edit)

        self.setLayout(layout)

    def collect_asset(self):
        query = self.query_edit.text().strip()
        if not query:
            self.result_edit.append("错误: 查询语句不能为空!")
            return
        
        page = self.page_spin.value()
        size = self.size_spin.value()

        self.scan_btn.setEnabled(False)
        self.result_edit.clear()
        self.result_edit.append(f"开始资产收集,查询语句: {query},页码: {page},数量: {size}")

        #调用资产收集函数
        asserts = self.collector.collect_fofa(query,page,size)
        if asserts:
            for asset in asserts:
                self.result_edit.append(f"IP: {asset['ip'],} 端口: {asset['port']},域名: {asset['domain']}")
        else:
                self.result_edit.append("未收集到资产 (请检查fofa配置/查询语句)")
        self.scan_btn.setEnabled(True)
            