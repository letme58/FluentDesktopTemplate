from typing import Optional
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from qfluentwidgets import (CardWidget, IconWidget, TitleLabel, BodyLabel, 
                            CaptionLabel, FluentIconBase)

class StatisticsCard(CardWidget):
    def __init__(self, title: str, value: str, icon: FluentIconBase, unit: str = "", parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(200, 100)
        
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(15, 15, 15, 15)
        self.layout.setSpacing(15)
        
        # 图标背景色
        self.icon_widget = IconWidget(icon, self)
        self.icon_widget.setFixedSize(32, 32)
        
        # 文本信息
        self.text_layout = QVBoxLayout()
        self.text_layout.setSpacing(2)
        
        self.title_label = CaptionLabel(title, self)
        self.title_label.setStyleSheet("color: gray;")
        
        self.value_layout = QHBoxLayout()
        self.value_label = TitleLabel(value, self)
        self.value_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.unit_label = CaptionLabel(unit, self)
        self.unit_label.setStyleSheet("margin-top: 5px;")
        
        self.value_layout.addWidget(self.value_label)
        self.value_layout.addWidget(self.unit_label)
        self.value_layout.addStretch(1)
        
        self.text_layout.addWidget(self.title_label)
        self.text_layout.addLayout(self.value_layout)
        
        self.layout.addWidget(self.icon_widget)
        self.layout.addLayout(self.text_layout)
        self.layout.addStretch(1)
