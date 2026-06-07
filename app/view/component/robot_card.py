from typing import Optional
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from qfluentwidgets import (SubtitleLabel, BodyLabel, IconWidget, TransparentToolButton, 
                            FluentIcon as FI, CaptionLabel, CardWidget, ProgressBar, 
                            PrimaryPushButton, PushButton)

from core import MyFluentIcon as MFI

class RobotCard(CardWidget):
    def __init__(self, name: str, bot_id: str, status: str, usage: int = 0, is_online: bool = True, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(280, 220)
        
        # 主布局
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(0)

        # 顶部布局：图标 + 状态指示器
        self.header_layout = QHBoxLayout()
        self.icon_widget = IconWidget(MFI.BOT, self)
        self.icon_widget.setFixedSize(36, 36)
        
        self.status_container = QWidget(self)
        self.status_layout = QHBoxLayout(self.status_container)
        self.status_layout.setContentsMargins(0, 0, 0, 0)
        self.status_layout.setSpacing(6)
        
        self.status_dot = QWidget(self)
        self.status_dot.setFixedSize(8, 8)
        dot_color = "#4CAF50" if is_online else "#F44336"
        self.status_dot.setStyleSheet(f"background-color: {dot_color}; border-radius: 4px;")
        
        self.status_label = CaptionLabel(status, self)
        self.status_label.setStyleSheet(f"color: {dot_color}; font-weight: bold;")
        
        self.status_layout.addWidget(self.status_dot)
        self.status_layout.addWidget(self.status_label)
        
        self.header_layout.addWidget(self.icon_widget)
        self.header_layout.addStretch(1)
        self.header_layout.addWidget(self.status_container)
        
        # 中部：名称和ID
        self.name_label = SubtitleLabel(name, self)
        self.id_label = CaptionLabel(f"UID: {bot_id}", self)
        self.id_label.setProperty("lightColor", Qt.GlobalColor.gray)
        
        # 资源监控部分
        self.usage_layout = QVBoxLayout()
        self.usage_layout.setSpacing(4)
        self.usage_header = QHBoxLayout()
        self.usage_title = CaptionLabel("CPU 负载", self)
        self.usage_value = CaptionLabel(f"{usage}%", self)
        self.usage_header.addWidget(self.usage_title)
        self.usage_header.addStretch(1)
        self.usage_header.addWidget(self.usage_value)
        
        self.progress_bar = ProgressBar(self)
        self.progress_bar.setValue(usage)
        self.progress_bar.setFixedHeight(4)
        
        self.usage_layout.addLayout(self.usage_header)
        self.usage_layout.addWidget(self.progress_bar)
        
        # 底部操作按钮
        self.actions_layout = QHBoxLayout()
        self.actions_layout.setSpacing(10)
        if is_online:
            self.main_action = PushButton("停止", self)
        else:
            self.main_action = PrimaryPushButton("启动", self)
        self.main_action.setFixedHeight(32)
        
        self.config_button = TransparentToolButton(FI.SETTING, self)
        self.config_button.setFixedSize(32, 32)
        
        self.actions_layout.addWidget(self.main_action, 1)
        self.actions_layout.addWidget(self.config_button)

        # 组合所有部分
        self.main_layout.addLayout(self.header_layout)
        self.main_layout.addSpacing(15)
        self.main_layout.addWidget(self.name_label)
        self.main_layout.addWidget(self.id_label)
        self.main_layout.addSpacing(15)
        self.main_layout.addLayout(self.usage_layout)
        self.main_layout.addStretch(1)
        self.main_layout.addLayout(self.actions_layout)

        self.setCursor(Qt.CursorShape.PointingHandCursor)
