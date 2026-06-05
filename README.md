# FluentDesktopTemplate

`FluentDesktopTemplate` 是一个基于 `PySide6` 和 `Fluent Design System` 的桌面应用程序模板。它旨在提供一个结构清晰、易于扩展和美观的用户界面，帮助开发者快速启动他们的桌面应用项目。

## :sparkles: 主要特性

-   **现代 Fluent Design UI**: 采用 `PySide6-Fluent-Widgets` 库，提供符合 Fluent Design 规范的现代化用户界面。
-   **模块化架构**: 清晰的 `app` 目录结构，将配置、控制器、核心逻辑、模型、资源和视图分离，便于管理和维护。
-   **异步加载机制**: 引入异步加载模块 (`AsyncLoader`)，提升应用启动和数据处理的响应速度。
-   **可扩展的图标系统**: 基于 `FluentIconBase` 和 `Enum` 实现的图标管理，轻松扩展和切换主题图标。
-   **自定义样式表**: 支持深色/浅色主题的 QSS 样式文件，实现界面的灵活定制。
-   **可复用组件**: 包含 `FlowLayout`, `StackedWidget`, `InterfaceTitleBar` 等通用 UI 组件，提高开发效率。
-   **设置界面**: 预置了主题模式、语言选择、自动更新等功能设置，提供良好的用户体验。
-   **控制台日志**: 集成的控制台界面用于显示应用程序日志。
-   **Git 友好配置**: 包含 `.gitignore` 和 `.ruff.toml`，帮助您管理代码版本和格式。

## :rocket: 安装

在开始之前，请确保您已安装 Python 3.9 或更高版本。

1.  **克隆仓库**:
    ```bash
    git clone https://github.com/letme58/FluentDesktopTemplate.git
    cd FluentDesktopTemplate
    ```

2.  **创建并激活虚拟环境 (推荐)**:
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **安装依赖**:
    ```bash
    pip install -r requirements.txt
    ```

## :gear: 使用方法

激活虚拟环境后，您可以运行主应用程序：

```bash
python app/main.py
```

您也可以运行 `playground.py` 文件来查看一些组件的演示：

```bash
python app/playground.py
```

## :card_file_box: 项目结构

项目的核心结构如下：

```
FluentDesktopTemplate/
├── .github/                       # GitHub Actions 工作流
│   └── workflows/
│       └── ruff.yml               # Ruff 代码检查工作流
├── app/                           # 应用程序核心代码
│   ├── config/                    # 应用程序配置
│   │   ├── __init__.py
│   │   ├── config.py              # 配置项定义
│   │   └── constan.py             # 常量定义 (如语言枚举)
│   ├── controller/                # 应用程序控制器逻辑
│   │   └── controller.py
│   ├── core/                      # 核心功能模块
│   │   ├── __init__.py
│   │   ├── async_loader.py        # 异步加载器
│   │   ├── extension_object_design_patterns_experiment.py # 扩展对象设计模式实验
│   │   ├── icon.py                # 自定义图标系统
│   │   ├── signal_bus.py          # 信号总线
│   │   └── style.py               # 样式表管理
│   ├── model/                     # 数据模型定义
│   │   └── __init__.py
│   ├── res/                       # 资源文件 (图标、样式等)
│   │   ├── icons/                 # SVG 格式的图标文件
│   │   └── style/                 # QSS 样式表文件
│   │       ├── dark/
│   │       └── light/
│   ├── view/                      # UI 视图层
│   │   ├── component/             # 可复用的 UI 组件
│   │   ├── interface/             # 不同的应用界面
│   │   └── main_window.py         # 主窗口定义
│   ├── __init__.py
│   ├── main.py                    # 应用程序入口
│   └── playground.py              # 组件和功能演示
├── config/
│   └── config.json                # 应用程序的默认配置
├── .gitignore                     # Git 忽略文件配置
├── .ruff.toml                     # Ruff Linter 配置
├── LICENSE                        # 项目许可证 (MIT License)
└── README.md                      # 项目说明文档
```

## :raising_hands: 贡献

欢迎通过提交 Issue 或 Pull Request 来贡献您的代码。

## :page_with_curl: 许可证

本项目采用 MIT 许可证，详情请参见 [LICENSE](LICENSE) 文件。
