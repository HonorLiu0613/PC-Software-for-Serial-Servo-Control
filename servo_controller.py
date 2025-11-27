"""
servo_controller.py
负责封装 0x55 0x55 舵机协议
由 SerialManager / MySerial 执行真正发送
"""

class ServoController:
    def __init__(self, serial_mgr):
        self.serial_mgr = serial_mgr
        self.HEAD = 0x55
        self.CMD_DO = 0x01
        self.LEN_DO = 0x07

    def _checksum(self, data: bytes) -> int:
        """计算校验和：~sum(data[2..8]) & 0xFF"""
        return (~sum(data) & 0xFF) & 0xFF

    def pack_do(self, servo_id: int, angle_deg: int, time_ms: int) -> bytes:
        """
        生成 DO 指令包 (10 bytes)
        angle_deg: 0~240°
        """
        # 角度映射到 0~1000，与原程序一致
        angle_val = int(angle_deg * 1000 / 240)

        angle_L = angle_val & 0xFF
        angle_H = (angle_val >> 8) & 0xFF

        time_L = time_ms & 0xFF
        time_H = (time_ms >> 8) & 0xFF

        # 前 9 字节
        buf = bytearray([
            self.HEAD, self.HEAD,   # [0] [1]
            servo_id,               # [2]
            self.LEN_DO,            # [3] = 7
            self.CMD_DO,            # [4] = 1
            angle_L, angle_H,       # [5] [6]
            time_L, time_H          # [7] [8]
        ])

        # 校验范围：data[2..8]
        checksum = self._checksum(buf[2:9])
        buf.append(checksum)  # [9]

        return bytes(buf)

    def send_do(self, servo_id: int, angle_deg: int, time_ms: int) -> bool:
        """发送 DO 指令"""
        if not self.serial_mgr.is_open():
            self.serial_mgr.log("串口未打开，无法发送舵机指令。")
            return False

        packet = self.pack_do(servo_id, angle_deg, time_ms)

        ok = self.serial_mgr.write_bytes(packet)
        if ok:
            self.serial_mgr.log(
                f"DO -> id={servo_id} angle={angle_deg}° time={time_ms}ms"
            )
        return ok

    def pack_change_id(self, new_id: int) -> bytes:
        """
        生成修改舵机 ID 的指令包
        new_id: 目标舵机 ID
        返回完整字节包
        """
        base_packet = bytearray([
            0x55, 0x55,  # 头
            0xFE,  # 舵机ID，广播
            4,  # 长度
            13,  # CMD=13 改ID
            int(new_id)  # 新ID
        ])
        checksum = (~sum(base_packet[2:6])) & 0xFF  # 校验范围 2..5
        base_packet.append(checksum)
        return bytes(base_packet)

    def send_change_id(self, new_id: int) -> bool:
        """
        发送修改舵机 ID 指令
        """
        if not self.serial_mgr.is_open():
            self.serial_mgr.log("串口未打开，无法修改ID。")
            return False
        packet = self.pack_change_id(new_id)
        try:
            self.serial_mgr.write_bytes(packet)
            self.serial_mgr.log(f"成功修改ID为: {new_id}")
            return True
        except Exception as e:
            self.serial_mgr.log(f"发送数据失败: {e}")
            return False