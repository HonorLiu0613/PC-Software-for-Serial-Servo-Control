# 串口舵机控制项目

这是一个基于 Python 的串口通信控制舵机项目，主要通过图形界面操作舵机运动，适用于机器人动作编辑、自动化控制等场景。
## 演示视频
【基于PySide6的BUS舵机控制上位机演示视频】 https://www.bilibili.com/video/BV1YQSTBvEAJ/?share_source=copy_web&vd_source=ed252459302a17b4b11f3eeb7d925a3d
## 项目功能

- **串口通信**：通过 `SerialManager` 类实现串口设备的自动检测、连接与数据发送。
- **舵机控制**：使用 `ServoController` 类发送指令控制舵机角度、运行时间以及修改舵机 ID。
- **动作编辑**：提供图形界面（GUI）进行动作帧的添加、删除、插入延迟等操作。
- **配置管理**：支持舵机配置的保存与加载（通过 `config_manager.py`）。

## 主要模块

- `main.py`：主程序入口，包含图形界面逻辑。
- `servo_controller.py`：舵机指令生成与发送模块。
- `serial_manager.py`：串口管理模块，支持自动刷新串口列表。
- `dance_editor.py`：动作编辑模块，支持多帧动作管理。
- `config_manager.py`：配置文件读写模块。

## 使用方法

1. 运行 `main.py` 启动图形界面。
2. 选择可用串口并连接舵机设备。
3. 使用界面操作添加动作帧，设置舵机角度与时间。
4. 可通过“播放”按钮执行当前动作序列。
5. 使用配置功能保存或加载舵机配置。

## 依赖库

- PyQt5：用于构建图形界面。
- pyserial：用于串口通信。

## 许可证

本项目遵循 MIT 许可证，请参阅 `LICENSE` 文件。
