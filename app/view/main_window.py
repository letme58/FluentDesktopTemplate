from qfluentwidgets import NavigationItemPosition, FluentIcon as FI

from view.component import Window
from view.interface import (
    InterfaceTemplates,
    HomeInterface,

    ConsoleInterface,
    SettingInterface,

)
from core import MyFluentIcon as MFI


class MainWindow(Window):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.__createSubInterface()
        self.__initNavigation()
        self.__initWindow()

    def __createSubInterface(self):
        self.home_interface = HomeInterface(self)

        self.global_instance_interface = InterfaceTemplates("GlobalInstanceSelection", "选择全局实例子界面", self)
        self.console_interface = ConsoleInterface(self)
        self.setting_interface = SettingInterface(self)

    def __initNavigation(self):
        # set top menu
        self.addSubInterface(self.home_interface, FI.HOME, "首页")

        # set menu separator
        self.navigation_interface.addSeparator()
        # set scroll menu


        # set bottom menu
        self.addSubInterface(
            self.global_instance_interface,
            MFI.BOTSPARKLE,
            "全局实例选择",
            NavigationItemPosition.BOTTOM,
        )
        self.addSubInterface(self.console_interface, FI.PRINT, "控制台", NavigationItemPosition.BOTTOM)
        self.addSubInterface(
            self.setting_interface,
            FI.SETTING,
            "设置",
            NavigationItemPosition.BOTTOM,
        )

    def __initWindow(self):
        self.setWindowTitle("模板项目名")
