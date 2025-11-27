"""
main.py
依赖 ui.wudao 和 ui.create
"""
import time
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import Qt,QTimer
from ui.wudao import Ui_Form
from ui.create import Ui_Form2
from serial_manager import SerialManager
from servo_controller import ServoController
from config_manager import load_config, save_config, default_config
from dance_editor import DanceEditor
class ActionFrame:
    def __init__(self, angles, times):
        self.angles = angles  # list[int]
        self.times = times    # list[int]

class ActionGroup:
    def __init__(self):
        self.frames = []

    def add_frame(self, angles, times):
        self.frames.append(ActionFrame(angles, times))

    def clear(self):
        self.frames.clear()

    def to_lines(self):
        return [",".join(map(str, f.angles + f.times)) for f in self.frames]

    def from_lines(self, lines):
        self.frames = []
        for line in lines:
            values = list(map(int, line.strip().split(",")))
            if len(values) == 48:
                angles = values[:24]
                times = values[24:]
                self.frames.append(ActionFrame(angles, times))
class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        try:
            self.setFixedSize(self.width(), self.height())
            self.setWindowOpacity(0.85)
        except Exception:
            pass

        # 导入实例化
        self.serial_mgr = SerialManager(logger=self.textEdit)
        self.servo_ctrl = ServoController(self.serial_mgr)
        self.dance_editor = DanceEditor(self.textedit_output)

        self.combo_sync_timer = QTimer(self)
        # 同步间隔与 SerialManager 刷新间隔
        self.combo_sync_timer.setInterval(1000)
        # 绑定同步函数
        self.combo_sync_timer.timeout.connect(self.sync_combo_ports)
        # 启动定时器
        self.combo_sync_timer.start()
        # 绑定 UI 命名规则
        self.servo_values = {
            i: {
                "slider": getattr(self, f"Slider_Servo{i}"),
                "lineEdit": getattr(self, f"lineEdit_servo{i}"),
                "lineEdit_time": getattr(self, f"lineEdit_time{i}")
            } for i in range(1, 25)
        }

        # 设置 time 默认为 500
        for i in range(1, 25):
            try:
                self.servo_values[i]["lineEdit_time"].setText("500")
            except Exception:
                pass

        self.bind_ui()
        self.setup_dance_editor()
        self.populate_serial_ports()
        self.config_data = None  # 当前加载的配置内容

    def sync_combo_ports(self):
        """自动同步串口下拉框"""
        current_selected_text = self.comboBox_ports.currentText()
        # 获取 SerialManager 中最新的串口列表
        latest_ports = self.serial_mgr.ports_list
        combo_devices = set()
        for i in range(1, self.comboBox_ports.count()):
            item_text = self.comboBox_ports.itemText(i)
            device = item_text.split(" ")[0]
            combo_devices.add(device)

        # 提取最新串口列表中的设备名
        latest_devices = set(p.device for p in latest_ports)

        if combo_devices != latest_devices:
            self.populate_serial_ports()
            if current_selected_text != "请选择你的串口...":
                new_index = self.comboBox_ports.findText(current_selected_text)
                if new_index != -1:
                    self.comboBox_ports.setCurrentIndex(new_index)
    def bind_ui(self):
        # 角度与时间输入校验和响应
        for i in range(1, 25):
            le = self.servo_values[i]["lineEdit"]
            lt = self.servo_values[i]["lineEdit_time"]
            sl = self.servo_values[i]["slider"]
            le.setValidator(QIntValidator(0, 240, self))
            lt.setValidator(QIntValidator(0, 200, self))
            sl.valueChanged.connect(self.on_slider_changed)
            le.editingFinished.connect(self.on_angle_edit_finished)
            lt.editingFinished.connect(self.on_time_edit_finished)


        self.pushButton_init.clicked.connect(self.servo_init)
        self.pushButton_importinit.clicked.connect(self.import_init)
        self.pushButton_create.clicked.connect(self.open_createwindow)
        self.pushButton_clean.clicked.connect(lambda: self.textEdit.clear())
        self.comboBox_ports.currentIndexChanged.connect(self.select_port)
        self.pushButton_broadcast.clicked.connect(self.on_change_id_clicked)

    def setup_dance_editor(self):
        self.action_group = ActionGroup()
        self.pushButton_addFrame.clicked.connect(self.on_add_frame_clicked)
        self.pushButton_clearFrames.clicked.connect(self.on_clear_frames_clicked)
        self.pushButton_playGroup.clicked.connect(self.on_play_group_clicked)
        self.pushButton_delay.clicked.connect(self.pushButton_delay_clicked)
        self.pushButton_clearline.clicked.connect(self.pushButton_clearline_clicked)
        self.pushButton_insertmove.clicked.connect(self.pushButton_insertmove_clicked)
        self.pushButton_insertdelay.clicked.connect(self.pushButton_insertdelay_clicked)
        self.pushButton_paste.clicked.connect(self.pushButton_paste_clicked)
        self.pushButton_init_2.clicked.connect(self.servo_init)

    def add_index(self):
        self.dance_editor.add_index()
    def pushButton_paste_clicked(self):
        self.dance_editor.paste_content()

    def on_add_frame_clicked(self):
        ID = int(self.lineEdit_idinput.text())
        angle = int(self.lineEdit_angleinput.text())
        time_val = int(self.lineEdit_timeinput.text())
        self.dance_editor.add_frame(ID, angle, time_val)

    def on_clear_frames_clicked(self):
        self.dance_editor.clear_all_frames()

    def on_play_group_clicked(self):
        # 传入舵机控制器实例，让 DanceEditor 处理播放逻辑
        self.dance_editor.play_all_frames(self.servo_ctrl)

    def pushButton_insertmove_clicked(self):
        insert_line = int(self.lineEdit_confirm.text())
        ID = int(self.lineEdit_idinput.text())
        angle = int(self.lineEdit_angleinput.text())
        time_val = int(self.lineEdit_timeinput.text())
        self.dance_editor.insert_move(insert_line, ID, angle, time_val)

    def pushButton_insertdelay_clicked(self):
        insert_line = int(self.lineEdit_confirm.text()) - 1
        delayval = int(self.lineEdit_delay.text())
        self.dance_editor.insert_delay(insert_line, delayval)

    def pushButton_delay_clicked(self):
        delayval = int(self.lineEdit_delay.text())
        self.dance_editor.add_delay(delayval)

    def pushButton_clearline_clicked(self):
        delateline = int(self.lineEdit_confirm.text()) - 1
        self.dance_editor.delete_line(delateline)
    def populate_serial_ports(self):
        self.comboBox_ports.clear()
        self.serial_mgr.refresh_ports()
        self.comboBox_ports.addItem("请选择你的串口...")
        for p in self.serial_mgr.ports_list:
            display = f"{p.device} ({p.description})"
            self.comboBox_ports.addItem(display, p.device)

    def select_port(self):
        text = self.comboBox_ports.currentText()
        if text == "请选择你的串口...":
            return
        port = text.split(" ")[0]
        if not port:
            self.serial_mgr.log("未选择有效串口。")
            return
        self.serial_mgr.close()
        ok = self.serial_mgr.open(port)
        if ok:
            self.serial = self.serial_mgr.get_native()

    def on_slider_changed(self):
        # 找到哪个 slider 有焦点，再发送
        for i in range(1, 25):
            if self.servo_values[i]["slider"].hasFocus():
                val = self.servo_values[i]["slider"].value()
                self.servo_values[i]["lineEdit"].setText(str(val))
                self.servo_ctrl.send_do(i, val, 20)
                break

    def on_angle_edit_finished(self):
        for i in range(1, 25):
            if self.servo_values[i]["lineEdit"].hasFocus():
                try:
                    val = int(self.servo_values[i]["lineEdit"].text())
                    t = int(self.servo_values[i]["lineEdit_time"].text())
                    self.servo_values[i]["slider"].setValue(val)
                    self.servo_ctrl.send_do(i, val, t)
                except Exception:
                    self.serial_mgr.log(f"舵机{i}：角度或时间输入无效")
                break

    def on_time_edit_finished(self):
        for i in range(1, 25):
            if self.servo_values[i]["lineEdit_time"].hasFocus():
                try:
                    angle = int(self.servo_values[i]["lineEdit"].text())
                    t = int(self.servo_values[i]["lineEdit_time"].text())
                    self.servo_values[i]["slider"].setValue(angle)
                    self.servo_ctrl.send_do(i, angle, t)
                except Exception:
                    self.serial_mgr.log(f"舵机{i}：角度或时间输入无效")
                break

    def servo_init(self):
        """
        将当前加载的 config 的初始角度写到界面并发送到舵机
        """
        if not self.config_data:
            self.serial_mgr.log("未加载配置文件，请先导入 config.json")
            return
        servos = self.config_data.get("servos", {})
        for i in range(1, 25):
            key = str(i)
            val = int(servos.get(key, 120))
            try:
                self.servo_values[i]["slider"].setValue(val)
                self.servo_values[i]["lineEdit"].setText(str(val))
                # 发送舵机指令
                self.servo_ctrl.send_do(i, val, 500)
                time.sleep(0.00001)
            except Exception as e:
                self.serial_mgr.log(f"舵机初始化写入失败: {e}")
        self.serial_mgr.log("机器人初始化完成。")

    def import_init(self):
        path = QFileDialog.getOpenFileName(self, "选择 config.json", "./", "JSON 文件 (*.json)")[0]
        if not path:
            return
        try:
            cfg = load_config(path)
            self.config_data = cfg
            self.serial_mgr.log(f"配置文件 {cfg.get('name','<unnamed>')} 导入成功。")
            # 解锁其他选项卡（如果存在）
            try:
                self.tabWidget.setTabEnabled(1, True)
                self.tabWidget.setTabEnabled(2, True)
            except Exception:
                pass
            # 自动初始化
            self.servo_init()
        except Exception as e:
            QMessageBox.critical(self, "错误", f"加载配置失败: {e}")

    def open_createwindow(self):
        self.create_window = ConfigWindow(parent=self)
        self.create_window.show()

    def on_change_id_clicked(self):
        if not self.serial_mgr.is_open():
            self.serial_mgr.log("串口未打开，无法修改ID。")
            return
        try:
            new_id = int(self.spinBox_ID.value())
            self.servo_ctrl.send_change_id(new_id)
        except Exception as e:
            self.serial_mgr.log(f"修改 ID 失败: {e}")

    def closeEvent(self, event):
        try:
            if hasattr(self, "create_window") and self.create_window:
                self.create_window.close()
        finally:
            self.serial_mgr.close()
            super().closeEvent(event)


class ConfigWindow(QWidget, Ui_Form2):
    """
    用于创建 config.json 的窗口（来自 create.ui）。
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(Qt.Window)
        self.parent = parent
        self.bind_ui()

    def bind_ui(self):
        # 初始化控件集合
        self.servo_values = {
            i: {
                "slider": getattr(self, f"Slider_Servo{i}"),
                "lineEdit": getattr(self, f"lineEdit_servo{i}")
            } for i in range(1, 25)
        }
        # 设置默认值
        for i in range(1, 25):
            try:
                self.servo_values[i]["slider"].setValue(120)
                self.servo_values[i]["lineEdit"].setText("120")
            except Exception:
                pass

        self.pushButton_create.clicked.connect(self.create_file)
        # 绑定 slider=>lineEdit
        for i in range(1, 25):
            try:
                self.servo_values[i]["slider"].valueChanged.connect(self._make_slider_cb(i))
            except Exception:
                pass

    def _make_slider_cb(self, idx):
        def cb(val):
            try:
                self.servo_values[idx]["lineEdit"].setText(str(val))
            except Exception:
                pass
        return cb

    def create_file(self):
        # 读取 robot name（如果你在 UI 里添加 lineEdit_robotName）
        robot_name = ""
        try:
            robot_name = self.lineEdit_robotName.text().strip()
        except Exception:
            robot_name = ""
        default_name = robot_name or "DanceRobot"
        filename = QFileDialog.getSaveFileName(self, "保存配置文件为", "./", "JSON 文件 (*.json)")[0]
        if not filename:
            # 如果用户取消，自动使用 robot_name.json
            filename = f"{default_name}.json"
        # 读 24 路角度
        servos = {}
        for i in range(1, 25):
            try:
                servos[str(i)] = int(self.servo_values[i]["lineEdit"].text())
            except Exception:
                servos[str(i)] = 120
        # 保存
        try:
            from config_manager import save_config
            save_config(filename, default_name, servos)
            QMessageBox.information(self, "成功", f"配置已保存: {filename}")
        except Exception as e:
            QMessageBox.critical(self, "失败", f"保存配置失败: {e}")


if __name__ == "__main__":
    app = QApplication([])
    w = MainWindow()
    w.show()
    app.exec()
