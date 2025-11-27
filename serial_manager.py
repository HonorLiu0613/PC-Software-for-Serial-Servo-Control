"""
serial_manager.py
封装串口操作（列出、打开、关闭、写入、日志），新增定时器自动刷新串口列表。
"""
import serial
import serial.tools.list_ports
from typing import Optional
from PySide6.QtCore import QTimer

class SerialManager:
    def __init__(self, logger=None, refresh_interval: int = 1000):
        """
        初始化串口管理器
        :param logger: 日志输出对象
        :param refresh_interval: 串口列表刷新间隔（毫秒），默认 1 秒
        """
        self.logger = logger
        self._serial: Optional[serial.Serial] = None
        self.ports_list = self.list_ports()  # 初始串口列表

        # 初始化定时器
        self.refresh_timer = QTimer()
        self.refresh_timer.setInterval(refresh_interval)  # 设置刷新间隔
        self.refresh_timer.timeout.connect(self._auto_refresh_ports)  # 绑定刷新函数
        self.refresh_timer.start()  # 启动定时器

    def log(self, msg: str):
        if self.logger and hasattr(self.logger, "append"):
            try:
                self.logger.append(msg)
            except Exception:
                print(msg)
        else:
            print(msg)

    def list_ports(self):
        """列出当前所有可用串口"""
        ports = list(serial.tools.list_ports.comports())
        return ports

    def refresh_ports(self):
        """手动刷新串口列表（返回最新列表）"""
        self.ports_list = self.list_ports()
        return self.ports_list

    def _auto_refresh_ports(self):
        """定时器回调：自动刷新串口列表（内部使用）"""
        old_ports = set(p.device for p in self.ports_list)  # 旧串口设备名集合
        new_ports = self.list_ports()  # 扫描新串口列表
        new_ports_devices = set(p.device for p in new_ports)  # 新串口设备名集合

        # 对比新旧串口列表，输出变化日志
        added_ports = new_ports_devices - old_ports  # 新增的串口
        removed_ports = old_ports - new_ports_devices  # 移除的串口

        if added_ports:
            self.log(f"新增串口: {', '.join(added_ports)}")
        if removed_ports:
            self.log(f"移除串口: {', '.join(removed_ports)}")

        # 更新串口列表
        self.ports_list = new_ports

    def set_refresh_interval(self, interval: int):
        """设置串口刷新间隔（毫秒）"""
        if interval > 0:
            self.refresh_timer.setInterval(interval)
            self.log(f"串口刷新间隔已设置为 {interval}ms")

    def stop_refresh(self):
        """停止自动刷新串口列表"""
        self.refresh_timer.stop()
        self.log("串口自动刷新已停止")

    def start_refresh(self):
        """启动自动刷新串口列表（默认初始化时已启动）"""
        self.refresh_timer.start()
        self.log("串口自动刷新已启动")

    def open(self, port: str, baudrate: int = 115200, timeout: float = 1):
        try:
            if self._serial and self._serial.is_open:
                self.log(f"已有串口连接: {self._serial.port}. 先关闭再打开新串口。")
                self.close()
            self._serial = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
            if self._serial.is_open:
                self.log(f"已打开串口: {port} ({baudrate})")
                return True
            else:
                self.log(f"打开串口失败: {port}")
                return False
        except Exception as e:
            self.log(f"打开串口异常: {e}")
            self._serial = None
            return False

    def close(self):
        try:
            if self._serial and self._serial.is_open:
                self._serial.close()
                self.log("串口已关闭。")
                self._serial = None
        except Exception as e:
            self.log(f"关闭串口异常: {e}")

    def is_open(self):
        return self._serial is not None and self._serial.is_open

    def write_bytes(self, data: bytes):
        if not self.is_open():
            self.log("写入失败：串口未打开。")
            return False
        try:
            self._serial.write(data)
            return True
        except Exception as e:
            self.log(f"写入串口失败: {e}")
            return False

    def get_native(self):
        return self._serial

    def __del__(self):
        """析构时停止定时器，避免资源泄漏"""
        self.refresh_timer.stop()
        self.close()