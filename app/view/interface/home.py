from typing import Optional

from qfluentwidgets import ScrollArea
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout

from core import StyleSheet
from view.component import InterfaceTitleBar, RobotCard, FlowLayout, StatisticsCard
from qfluentwidgets import FluentIcon as FI, SubtitleLabel


class HomeInterface(ScrollArea):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        # Instantiating Widget Objects
        self.view_container = QWidget()
        self.title_bar = InterfaceTitleBar("控制台概览", "实时监控您的机器人集群状态")
        # Instantiating Layout Objects
        self.view_container_layout_manager = QVBoxLayout(self.view_container)
        # Initialize Widgets & Layouts
        self.__init_sub_widget()
        self.__init_widget()
        self.__init_layout()

    def __init_widget(self) -> None:
        # Set Object Name
        self.setObjectName("HomeInterface")
        # Set Widget & Geometry
        self.setWidget(self.view_container)
        # Set Widget Options
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # Apply stylesheet
        StyleSheet.HOME_INTERFACE.apply(self)

    def __init_sub_widget(self):
        self.view_container.setObjectName("HomeInterfaceViewContainer")

    def __init_layout(self) -> None:
        # Set Layout Options
        self.view_container_layout_manager.setContentsMargins(36, 20, 36, 36)
        self.view_container_layout_manager.setSpacing(30)
        self.view_container_layout_manager.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # 1. 标题栏
        self.view_container_layout_manager.addWidget(self.title_bar)

        # 2. 统计区块
        self.stats_title = SubtitleLabel("系统状态", self.view_container)
        self.view_container_layout_manager.addWidget(self.stats_title)
        
        self.stats_layout = FlowLayout()
        self.view_container_layout_manager.addLayout(self.stats_layout)
        
        self.stats_cards = [
            StatisticsCard("运行中机器人", "12", FI.IOT, "个"),
            StatisticsCard("今日消息数", "1.2k", FI.CHAT, "条"),
            StatisticsCard("平均负载", "45", FI.TILES, "%"),
            StatisticsCard("系统在线时长", "15", FI.HISTORY, "天"),
        ]
        for card in self.stats_cards:
            self.stats_layout.addWidget(card)

        # 3. 机器人列表区块
        self.robots_title = SubtitleLabel("机器人集群", self.view_container)
        self.view_container_layout_manager.addWidget(self.robots_title)

        self.flow_layout = FlowLayout()
        self.view_container_layout_manager.addLayout(self.flow_layout)

        # Add Robot Cards with new format
        self.robot_data = [
            ("智能客服 A", "bot-001", "运行中", 24, True),
            ("数据分析 B", "bot-002", "异常离线", 0, False),
            ("流程自动化 C", "bot-003", "待机", 12, True),
            ("视觉识别 D", "bot-004", "满载运行", 89, True),
            ("测试助手 E", "bot-005", "运行中", 35, True),
        ]

        for name, uid, status, usage, online in self.robot_data:
            card = RobotCard(name, uid, status, usage, online)
            self.flow_layout.addWidget(card)
