import os
from enum import Enum
from qfluentwidgets import getIconColor, Theme, FluentIconBase


class MyFluentIcon(FluentIconBase, Enum):
    ADD = "Add"
    CUT = "Cut"
    COPY = "Copy"
    BOT = "Bot"
    BOTSPARKLE = "BotSparkle"
    OFFICALMARK = "OfficalMark"
    NOTOFFICALMARK = "NotOfficalMark"
    CHECKPASS = "CheckPass"
    CHECKNOTPASS = "CheckNotPass"

    def path(self, theme=Theme.AUTO):
        theme_remap = {"black": "dark", "white": "light"}[getIconColor(theme)]
        
        # 使用绝对路径以确保图标加载可靠
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(base_path, "res", "icons", f"{self.value}_{theme_remap}.svg").replace("\\", "/")
        
        # 如果当前主题的图标不存在，尝试使用另一种主题的图标
        if not os.path.exists(path):
            other_theme = "light" if theme_remap == "dark" else "dark"
            fallback_path = os.path.join(base_path, "res", "icons", f"{self.value}_{other_theme}.svg").replace("\\", "/")
            if os.path.exists(fallback_path):
                return fallback_path
                
        return path
