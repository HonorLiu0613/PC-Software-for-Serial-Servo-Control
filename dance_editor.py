import re
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

class DanceEditor:
    def __init__(self, textedit_output):
        # 接收主窗口的文本编辑框控件
        self.textedit_output = textedit_output
        self.line = 1  # 行号计数器

    def add_index(self):
        """添加/刷新行号注释"""
        self.textedit_output.blockSignals(True)

        # 保存光标位置
        cursor = self.textedit_output.textCursor()
        pos = cursor.position()

        # 修改内容
        code = self.textedit_output.toPlainText()
        lineslist = code.split('\n')

        updated_lines = []
        for i, line in enumerate(lineslist):
            # 移除原有行号注释，重新添加
            line = re.sub(r'//\d{2}$', '', line).strip()
            updated_lines.append(f"{line}  //{i + 1:02d}")

        # 更新文本内容
        self.textedit_output.setPlainText('\n'.join(updated_lines))

        # 恢复光标位置（如果原位置超出新内容长度，就用末尾）
        new_cursor = self.textedit_output.textCursor()
        new_pos = min(pos, len(self.textedit_output.toPlainText()))
        new_cursor.setPosition(new_pos)
        self.textedit_output.setTextCursor(new_cursor)

        self.textedit_output.blockSignals(False)

    def paste_content(self):
        """粘贴剪切板内容"""
        clipboard = QApplication.clipboard()
        text = clipboard.text()
        self.textedit_output.append(text)
        self.add_index()

    def add_frame(self, servo_id, angle, time_val):
        """添加单个动作帧"""
        self.textedit_output.append(f"Servo_Do({servo_id}, {angle}, {time_val});")
        self.add_index()

    def clear_all_frames(self):
        """清空所有帧"""
        self.textedit_output.clear()
        self.line = 1

    def insert_move(self, insert_line, servo_id, angle, time_val):
        """插入动作帧"""
        new_content = f"Servo_Do({servo_id}, {angle}, {time_val});"
        code = self.textedit_output.toPlainText()
        lineslist = code.split('\n')

        if 0 <= insert_line <= len(lineslist):
            lineslist.insert(insert_line, new_content)
            self.textedit_output.setPlainText('\n'.join(lineslist))
            self.add_index()
            self.line += 1

    def insert_delay(self, insert_line, delay_val):
        """插入延时"""
        new_content = f"HAL_Delay({delay_val});"
        code = self.textedit_output.toPlainText()
        lineslist = code.split('\n')

        if 0 <= insert_line < len(lineslist):
            lineslist.insert(insert_line, new_content)
            self.textedit_output.setPlainText('\n'.join(lineslist))
            self.add_index()
            self.line += 1

    def add_delay(self, delay_val):
        """添加延时"""
        self.textedit_output.append(f"HAL_Delay({delay_val});")
        self.add_index()

    def delete_line(self, delete_line):
        """删除指定行"""
        code = self.textedit_output.toPlainText()
        lineslist = code.split('\n')

        if 0 <= delete_line < len(lineslist):
            lineslist.pop(delete_line)
            self.textedit_output.setPlainText('\n'.join(lineslist))
            self.add_index()
            self.line = max(1, self.line - 1)  # 防止行号为负

    def play_all_frames(self, servo_ctrl):
        """播放所有帧"""
        code = self.textedit_output.toPlainText()
        lineslist = code.split('\n')
        for line in lineslist:
            if line.strip().startswith("HAL_Delay"):
                match = re.search(r"\((\d+)\)", line)
                if match:
                    delay = int(match.group(1))
                    import time
                    time.sleep(delay / 1000)
            elif "Servo_Do" in line:
                match = re.search(r"\((\d+),\s*(\d+),\s*(\d+)\)", line)
                if match:
                    servo_id = int(match.group(1))
                    angle = int(match.group(2))
                    time_val = int(match.group(3))
                    servo_ctrl.send_do(servo_id, angle, time_val)