# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wudao.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1013, 633)
        Form.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QSize(0, 400))
        self.tabWidget.setMaximumSize(QSize(16777215, 400))
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"/* QTabWidget */\n"
"QTabWidget::pane {\n"
"    border: none;  /* \u53bb\u9664\u9762\u677f\u7684\u8fb9\u6846 */\n"
"    background: white;  /* \u8bbe\u7f6e\u9762\u677f\u80cc\u666f\u4e3a\u767d\u8272 */\n"
"}\n"
"\n"
"/* Tab Bar */\n"
"QTabWidget::tab-bar {\n"
"    left: 5px;  /* \u8bbe\u7f6e tab-bar \u4e0e\u5de6\u8fb9\u7f18\u7684\u95f4\u8ddd */\n"
"}\n"
"\n"
"/* Tab \u6837\u5f0f */\n"
"QTabBar::tab {\n"
"    background: white;  /* \u8bbe\u7f6e tab \u7684\u80cc\u666f\u4e3a\u767d\u8272 */\n"
"    border: 2px solid #dcdcdc;  /* \u8bbe\u7f6e\u8fb9\u6846\u989c\u8272\u4e3a\u6d45\u7070\u8272 */\n"
"    border-radius: 4px;  /* \u8bbe\u7f6e\u5706\u89d2 */\n"
"    min-width: 80px;  /* \u8bbe\u7f6e tab \u6700\u5c0f\u5bbd\u5ea6 */\n"
"    padding: 10px;  /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */\n"
"}\n"
"\n"
"/* \u9009\u4e2d\u7684 tab \u6837\u5f0f */\n"
"QTabBar::tab:selected {\n"
"    background: #e0e0e0;  /* \u9009\u4e2d\u65f6\u7684\u80cc\u666f\u8272\u4e3a\u6d45\u7070\u8272 */\n"
"    border-color: #ffffff;  /* \u9009\u4e2d\u65f6"
                        "\u8fb9\u6846\u7684\u989c\u8272 */\n"
"    font-weight: bold;  /* \u8bbe\u7f6e\u9009\u4e2d\u65f6\u5b57\u4f53\u52a0\u7c97 */\n"
"}\n"
"\n"
"/* \u672a\u9009\u4e2d\u7684 tab \u6837\u5f0f */\n"
"QTabBar::tab:!selected {\n"
"    background: #f0f0f0;  /* \u672a\u9009\u4e2d\u65f6\u80cc\u666f\u989c\u8272\u4e3a\u975e\u5e38\u6d45\u7684\u7070\u8272 */\n"
"    margin-top: 5px;  /* \u672a\u9009\u4e2d\u65f6\u7684\u95f4\u8ddd */\n"
"    border-color: #dcdcdc;  /* \u672a\u9009\u4e2d\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"/* Tab \u4e0b\u5c5e\u754c\u9762 */\n"
"#tab, #tab_2, #tab_3, #tab_4 {\n"
"    background: white;  /* \u8bbe\u7f6e\u56db\u4e2a tab \u754c\u9762\u7684\u80cc\u666f\u4e3a\u767d\u8272 */\n"
"    border-radius: 6px;  /* \u8bbe\u7f6e\u5706\u89d2 */\n"
"    padding: 10px;  /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */\n"
"}\n"
"")
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setMovable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 60, 951, 122))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_create = QPushButton(self.layoutWidget)
        self.pushButton_create.setObjectName(u"pushButton_create")
        self.pushButton_create.setMinimumSize(QSize(50, 120))
        font = QFont()
        font.setPointSize(14)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setStyleSheet(u"QPushButton {\n"
"    background: white;  /* \u80cc\u666f\u8272\u4e3a\u767d\u8272 */\n"
"    border: 2px solid #59969b;  /* \u8bbe\u7f6e\u8fb9\u6846\u989c\u8272\u548c\u5bbd\u5ea6 */\n"
"    border-radius: 20px;  /* \u5706\u89d2\u8fb9\u6846 */ \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #f0f0f0;  /* \u60ac\u505c\u65f6\u80cc\u666f\u989c\u8272\u53d8\u5316 */\n"
"    border-color: #4a7b87;  /* \u60ac\u505c\u65f6\u8fb9\u6846\u989c\u8272\u53d8\u5316 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #e0e0e0;  /* \u6309\u4e0b\u65f6\u80cc\u666f\u989c\u8272\u53d8\u5316 */\n"
"    border-color: #3e6c72;  /* \u6309\u4e0b\u65f6\u8fb9\u6846\u989c\u8272\u53d8\u5316 */\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.pushButton_create)

        self.pushButton_importinit = QPushButton(self.layoutWidget)
        self.pushButton_importinit.setObjectName(u"pushButton_importinit")
        self.pushButton_importinit.setMinimumSize(QSize(50, 120))
        self.pushButton_importinit.setMaximumSize(QSize(620, 16777215))
        self.pushButton_importinit.setFont(font)
        self.pushButton_importinit.setStyleSheet(u"QPushButton {\n"
"    background: white;  /* \u80cc\u666f\u8272\u4e3a\u767d\u8272 */\n"
"    border: 2px solid #59969b;  /* \u8bbe\u7f6e\u8fb9\u6846\u989c\u8272\u548c\u5bbd\u5ea6 */\n"
"    border-radius: 20px;  /* \u5706\u89d2\u8fb9\u6846 */ \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #f0f0f0;  /* \u60ac\u505c\u65f6\u80cc\u666f\u989c\u8272\u53d8\u5316 */\n"
"    border-color: #4a7b87;  /* \u60ac\u505c\u65f6\u8fb9\u6846\u989c\u8272\u53d8\u5316 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #e0e0e0;  /* \u6309\u4e0b\u65f6\u80cc\u666f\u989c\u8272\u53d8\u5316 */\n"
"    border-color: #3e6c72;  /* \u6309\u4e0b\u65f6\u8fb9\u6846\u989c\u8272\u53d8\u5316 */\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.pushButton_importinit)

        self.layoutWidget1 = QWidget(self.tab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 951, 61))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(21)
        self.label_2.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.comboBox_ports = QComboBox(self.layoutWidget1)
        self.comboBox_ports.setObjectName(u"comboBox_ports")
        self.comboBox_ports.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setPointSize(10)
        self.comboBox_ports.setFont(font2)

        self.horizontalLayout_6.addWidget(self.comboBox_ports)

        self.labelID = QLabel(self.layoutWidget1)
        self.labelID.setObjectName(u"labelID")
        self.labelID.setMinimumSize(QSize(20, 20))
        font3 = QFont()
        font3.setPointSize(21)
        font3.setBold(False)
        self.labelID.setFont(font3)
        self.labelID.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelID)

        self.spinBox_ID = QSpinBox(self.layoutWidget1)
        self.spinBox_ID.setObjectName(u"spinBox_ID")
        self.spinBox_ID.setMinimumSize(QSize(20, 20))
        self.spinBox_ID.setFont(font3)
        self.spinBox_ID.setMaximum(20)

        self.horizontalLayout_6.addWidget(self.spinBox_ID)

        self.pushButton_broadcast = QPushButton(self.layoutWidget1)
        self.pushButton_broadcast.setObjectName(u"pushButton_broadcast")
        font4 = QFont()
        font4.setPointSize(21)
        font4.setBold(True)
        self.pushButton_broadcast.setFont(font4)
        self.pushButton_broadcast.setStyleSheet(u"QPushButton {\n"
"    background: white;  /* \u80cc\u666f\u8272\u4e3a\u767d\u8272 */\n"
"    border: 2px solid #59969b;  /* \u8bbe\u7f6e\u8fb9\u6846\u989c\u8272\u548c\u5bbd\u5ea6 */\n"
"    border-radius: 20px;  /* \u5706\u89d2\u8fb9\u6846 */ \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #f0f0f0;  /* \u60ac\u505c\u65f6\u80cc\u666f\u989c\u8272\u53d8\u5316 */\n"
"    border-color: #4a7b87;  /* \u60ac\u505c\u65f6\u8fb9\u6846\u989c\u8272\u53d8\u5316 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #e0e0e0;  /* \u6309\u4e0b\u65f6\u80cc\u666f\u989c\u8272\u53d8\u5316 */\n"
"    border-color: #3e6c72;  /* \u6309\u4e0b\u65f6\u8fb9\u6846\u989c\u8272\u53d8\u5316 */\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.pushButton_broadcast)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setStyleSheet(u".parent {\n"
"  border: 2px solid black; /* \u7236\u5bb9\u5668\u8fb9\u6846 */\n"
"  overflow: hidden; /* \u9632\u6b62\u5185\u5bb9\u6ea2\u51fa */\n"
"}")
        self.layoutWidget2 = QWidget(self.tab_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 861, 351))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.layoutWidget2)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.Slider_Servo1 = QSlider(self.frame)
        self.Slider_Servo1.setObjectName(u"Slider_Servo1")
        self.Slider_Servo1.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo1.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo1.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo1.setMinimum(0)
        self.Slider_Servo1.setMaximum(240)
        self.Slider_Servo1.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo1.setInvertedAppearance(False)
        self.Slider_Servo1.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo1.setTickInterval(1)
        self.lineEdit_servo1 = QLineEdit(self.frame)
        self.lineEdit_servo1.setObjectName(u"lineEdit_servo1")
        self.lineEdit_servo1.setEnabled(True)
        self.lineEdit_servo1.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo1.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo1.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_id1 = QLabel(self.frame)
        self.label_id1.setObjectName(u"label_id1")
        self.label_id1.setGeometry(QRect(1, 2, 139, 10))
        self.label_id1.setMinimumSize(QSize(0, 10))
        self.label_id1.setMaximumSize(QSize(16777215, 10))
        self.label_id1.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time1 = QLineEdit(self.frame)
        self.lineEdit_time1.setObjectName(u"lineEdit_time1")
        self.lineEdit_time1.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time1.setMaximumSize(QSize(120, 15))
        self.lineEdit_time1.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time1.setDragEnabled(False)

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.layoutWidget2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_2.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_id2 = QLabel(self.frame_2)
        self.label_id2.setObjectName(u"label_id2")
        self.label_id2.setGeometry(QRect(1, 1, 139, 10))
        self.label_id2.setMinimumSize(QSize(0, 10))
        self.label_id2.setMaximumSize(QSize(16777215, 10))
        self.label_id2.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"border: none; ")
        self.label_id2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_servo2 = QLineEdit(self.frame_2)
        self.lineEdit_servo2.setObjectName(u"lineEdit_servo2")
        self.lineEdit_servo2.setEnabled(True)
        self.lineEdit_servo2.setGeometry(QRect(17, 33, 106, 18))
        self.lineEdit_servo2.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo2.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }\n"
"border: none; ")
        self.lineEdit_servo2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Slider_Servo2 = QSlider(self.frame_2)
        self.Slider_Servo2.setObjectName(u"Slider_Servo2")
        self.Slider_Servo2.setGeometry(QRect(1, 17, 139, 10))
        self.Slider_Servo2.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo2.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo2.setMinimum(0)
        self.Slider_Servo2.setMaximum(240)
        self.Slider_Servo2.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo2.setInvertedAppearance(False)
        self.Slider_Servo2.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo2.setTickInterval(1)
        self.lineEdit_time2 = QLineEdit(self.frame_2)
        self.lineEdit_time2.setObjectName(u"lineEdit_time2")
        self.lineEdit_time2.setGeometry(QRect(17, 57, 106, 15))
        self.lineEdit_time2.setMaximumSize(QSize(120, 15))
        self.lineEdit_time2.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }\n"
"border: none; ")
        self.lineEdit_time2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time2.setDragEnabled(False)

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.layoutWidget2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_3.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_time3 = QLineEdit(self.frame_3)
        self.lineEdit_time3.setObjectName(u"lineEdit_time3")
        self.lineEdit_time3.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time3.setMaximumSize(QSize(120, 15))
        self.lineEdit_time3.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time3.setDragEnabled(False)
        self.lineEdit_servo3 = QLineEdit(self.frame_3)
        self.lineEdit_servo3.setObjectName(u"lineEdit_servo3")
        self.lineEdit_servo3.setEnabled(True)
        self.lineEdit_servo3.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo3.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo3.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Slider_Servo3 = QSlider(self.frame_3)
        self.Slider_Servo3.setObjectName(u"Slider_Servo3")
        self.Slider_Servo3.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo3.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo3.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo3.setMinimum(0)
        self.Slider_Servo3.setMaximum(240)
        self.Slider_Servo3.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo3.setInvertedAppearance(False)
        self.Slider_Servo3.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo3.setTickInterval(1)
        self.label_id3 = QLabel(self.frame_3)
        self.label_id3.setObjectName(u"label_id3")
        self.label_id3.setGeometry(QRect(1, 2, 139, 10))
        self.label_id3.setMinimumSize(QSize(0, 10))
        self.label_id3.setMaximumSize(QSize(16777215, 10))
        self.label_id3.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.layoutWidget2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setEnabled(True)
        self.frame_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_4.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_time4 = QLineEdit(self.frame_4)
        self.lineEdit_time4.setObjectName(u"lineEdit_time4")
        self.lineEdit_time4.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time4.setMaximumSize(QSize(120, 15))
        self.lineEdit_time4.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time4.setDragEnabled(False)
        self.label_id4 = QLabel(self.frame_4)
        self.label_id4.setObjectName(u"label_id4")
        self.label_id4.setGeometry(QRect(1, 2, 139, 10))
        self.label_id4.setMinimumSize(QSize(0, 10))
        self.label_id4.setMaximumSize(QSize(16777215, 10))
        self.label_id4.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_servo4 = QLineEdit(self.frame_4)
        self.lineEdit_servo4.setObjectName(u"lineEdit_servo4")
        self.lineEdit_servo4.setEnabled(True)
        self.lineEdit_servo4.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo4.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo4.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Slider_Servo4 = QSlider(self.frame_4)
        self.Slider_Servo4.setObjectName(u"Slider_Servo4")
        self.Slider_Servo4.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo4.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo4.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo4.setMinimum(0)
        self.Slider_Servo4.setMaximum(240)
        self.Slider_Servo4.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo4.setInvertedAppearance(False)
        self.Slider_Servo4.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo4.setTickInterval(1)

        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.layoutWidget2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setEnabled(True)
        self.frame_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_5.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_id5 = QLabel(self.frame_5)
        self.label_id5.setObjectName(u"label_id5")
        self.label_id5.setGeometry(QRect(1, 2, 139, 10))
        self.label_id5.setMinimumSize(QSize(0, 10))
        self.label_id5.setMaximumSize(QSize(16777215, 10))
        self.label_id5.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_servo5 = QLineEdit(self.frame_5)
        self.lineEdit_servo5.setObjectName(u"lineEdit_servo5")
        self.lineEdit_servo5.setEnabled(True)
        self.lineEdit_servo5.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo5.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo5.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time5 = QLineEdit(self.frame_5)
        self.lineEdit_time5.setObjectName(u"lineEdit_time5")
        self.lineEdit_time5.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time5.setMaximumSize(QSize(120, 15))
        self.lineEdit_time5.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time5.setDragEnabled(False)
        self.Slider_Servo5 = QSlider(self.frame_5)
        self.Slider_Servo5.setObjectName(u"Slider_Servo5")
        self.Slider_Servo5.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo5.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo5.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo5.setMinimum(0)
        self.Slider_Servo5.setMaximum(240)
        self.Slider_Servo5.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo5.setInvertedAppearance(False)
        self.Slider_Servo5.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo5.setTickInterval(1)

        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.layoutWidget2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setEnabled(True)
        self.frame_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_6.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.label_id6 = QLabel(self.frame_6)
        self.label_id6.setObjectName(u"label_id6")
        self.label_id6.setGeometry(QRect(1, 2, 139, 10))
        self.label_id6.setMinimumSize(QSize(0, 10))
        self.label_id6.setMaximumSize(QSize(16777215, 10))
        self.label_id6.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time6 = QLineEdit(self.frame_6)
        self.lineEdit_time6.setObjectName(u"lineEdit_time6")
        self.lineEdit_time6.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time6.setMaximumSize(QSize(120, 15))
        self.lineEdit_time6.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time6.setDragEnabled(False)
        self.lineEdit_servo6 = QLineEdit(self.frame_6)
        self.lineEdit_servo6.setObjectName(u"lineEdit_servo6")
        self.lineEdit_servo6.setEnabled(True)
        self.lineEdit_servo6.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo6.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo6.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Slider_Servo6 = QSlider(self.frame_6)
        self.Slider_Servo6.setObjectName(u"Slider_Servo6")
        self.Slider_Servo6.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo6.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo6.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo6.setMinimum(0)
        self.Slider_Servo6.setMaximum(240)
        self.Slider_Servo6.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo6.setInvertedAppearance(False)
        self.Slider_Servo6.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo6.setTickInterval(1)

        self.horizontalLayout.addWidget(self.frame_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_7 = QFrame(self.layoutWidget2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setEnabled(True)
        self.frame_7.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_7.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.label_id7 = QLabel(self.frame_7)
        self.label_id7.setObjectName(u"label_id7")
        self.label_id7.setGeometry(QRect(2, 4, 139, 10))
        self.label_id7.setMinimumSize(QSize(0, 10))
        self.label_id7.setMaximumSize(QSize(16777215, 10))
        self.label_id7.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time7 = QLineEdit(self.frame_7)
        self.lineEdit_time7.setObjectName(u"lineEdit_time7")
        self.lineEdit_time7.setGeometry(QRect(18, 63, 106, 15))
        self.lineEdit_time7.setMaximumSize(QSize(120, 15))
        self.lineEdit_time7.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time7.setDragEnabled(False)
        self.lineEdit_servo7 = QLineEdit(self.frame_7)
        self.lineEdit_servo7.setObjectName(u"lineEdit_servo7")
        self.lineEdit_servo7.setEnabled(True)
        self.lineEdit_servo7.setGeometry(QRect(18, 38, 106, 18))
        self.lineEdit_servo7.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo7.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Slider_Servo7 = QSlider(self.frame_7)
        self.Slider_Servo7.setObjectName(u"Slider_Servo7")
        self.Slider_Servo7.setGeometry(QRect(2, 21, 139, 10))
        self.Slider_Servo7.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo7.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo7.setMinimum(0)
        self.Slider_Servo7.setMaximum(240)
        self.Slider_Servo7.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo7.setInvertedAppearance(False)
        self.Slider_Servo7.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo7.setTickInterval(1)

        self.horizontalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.layoutWidget2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(True)
        self.frame_8.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_8.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_time8 = QLineEdit(self.frame_8)
        self.lineEdit_time8.setObjectName(u"lineEdit_time8")
        self.lineEdit_time8.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time8.setMaximumSize(QSize(120, 15))
        self.lineEdit_time8.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time8.setDragEnabled(False)
        self.lineEdit_servo8 = QLineEdit(self.frame_8)
        self.lineEdit_servo8.setObjectName(u"lineEdit_servo8")
        self.lineEdit_servo8.setEnabled(True)
        self.lineEdit_servo8.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo8.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo8.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_id8 = QLabel(self.frame_8)
        self.label_id8.setObjectName(u"label_id8")
        self.label_id8.setGeometry(QRect(1, 2, 139, 10))
        self.label_id8.setMinimumSize(QSize(0, 10))
        self.label_id8.setMaximumSize(QSize(16777215, 10))
        self.label_id8.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Slider_Servo8 = QSlider(self.frame_8)
        self.Slider_Servo8.setObjectName(u"Slider_Servo8")
        self.Slider_Servo8.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo8.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo8.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo8.setMinimum(0)
        self.Slider_Servo8.setMaximum(240)
        self.Slider_Servo8.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo8.setInvertedAppearance(False)
        self.Slider_Servo8.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo8.setTickInterval(1)

        self.horizontalLayout_2.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.layoutWidget2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setEnabled(True)
        self.frame_9.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_9.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_time9 = QLineEdit(self.frame_9)
        self.lineEdit_time9.setObjectName(u"lineEdit_time9")
        self.lineEdit_time9.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time9.setMaximumSize(QSize(120, 15))
        self.lineEdit_time9.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time9.setDragEnabled(False)
        self.Slider_Servo9 = QSlider(self.frame_9)
        self.Slider_Servo9.setObjectName(u"Slider_Servo9")
        self.Slider_Servo9.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo9.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo9.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo9.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo9.setMinimum(0)
        self.Slider_Servo9.setMaximum(240)
        self.Slider_Servo9.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo9.setInvertedAppearance(False)
        self.Slider_Servo9.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo9.setTickInterval(1)
        self.lineEdit_servo9 = QLineEdit(self.frame_9)
        self.lineEdit_servo9.setObjectName(u"lineEdit_servo9")
        self.lineEdit_servo9.setEnabled(True)
        self.lineEdit_servo9.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo9.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo9.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo9.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_id9 = QLabel(self.frame_9)
        self.label_id9.setObjectName(u"label_id9")
        self.label_id9.setGeometry(QRect(1, 2, 139, 10))
        self.label_id9.setMinimumSize(QSize(0, 10))
        self.label_id9.setMaximumSize(QSize(16777215, 10))
        self.label_id9.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.layoutWidget2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setEnabled(True)
        self.frame_10.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_10.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_servo10 = QLineEdit(self.frame_10)
        self.lineEdit_servo10.setObjectName(u"lineEdit_servo10")
        self.lineEdit_servo10.setEnabled(True)
        self.lineEdit_servo10.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo10.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo10.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_id10 = QLabel(self.frame_10)
        self.label_id10.setObjectName(u"label_id10")
        self.label_id10.setGeometry(QRect(1, 2, 139, 10))
        self.label_id10.setMinimumSize(QSize(0, 10))
        self.label_id10.setMaximumSize(QSize(16777215, 10))
        self.label_id10.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time10 = QLineEdit(self.frame_10)
        self.lineEdit_time10.setObjectName(u"lineEdit_time10")
        self.lineEdit_time10.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time10.setMaximumSize(QSize(120, 15))
        self.lineEdit_time10.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time10.setDragEnabled(False)
        self.Slider_Servo10 = QSlider(self.frame_10)
        self.Slider_Servo10.setObjectName(u"Slider_Servo10")
        self.Slider_Servo10.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo10.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo10.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo10.setMinimum(0)
        self.Slider_Servo10.setMaximum(240)
        self.Slider_Servo10.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo10.setInvertedAppearance(False)
        self.Slider_Servo10.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo10.setTickInterval(1)

        self.horizontalLayout_2.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.layoutWidget2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setEnabled(True)
        self.frame_11.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_11.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.label_id11 = QLabel(self.frame_11)
        self.label_id11.setObjectName(u"label_id11")
        self.label_id11.setGeometry(QRect(1, 2, 139, 10))
        self.label_id11.setMinimumSize(QSize(0, 10))
        self.label_id11.setMaximumSize(QSize(16777215, 10))
        self.label_id11.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Slider_Servo11 = QSlider(self.frame_11)
        self.Slider_Servo11.setObjectName(u"Slider_Servo11")
        self.Slider_Servo11.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo11.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo11.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo11.setMinimum(0)
        self.Slider_Servo11.setMaximum(240)
        self.Slider_Servo11.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo11.setInvertedAppearance(False)
        self.Slider_Servo11.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo11.setTickInterval(1)
        self.lineEdit_servo11 = QLineEdit(self.frame_11)
        self.lineEdit_servo11.setObjectName(u"lineEdit_servo11")
        self.lineEdit_servo11.setEnabled(True)
        self.lineEdit_servo11.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo11.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo11.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time11 = QLineEdit(self.frame_11)
        self.lineEdit_time11.setObjectName(u"lineEdit_time11")
        self.lineEdit_time11.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time11.setMaximumSize(QSize(120, 15))
        self.lineEdit_time11.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time11.setDragEnabled(False)

        self.horizontalLayout_2.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.layoutWidget2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setEnabled(True)
        self.frame_12.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_12.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.label_id12 = QLabel(self.frame_12)
        self.label_id12.setObjectName(u"label_id12")
        self.label_id12.setGeometry(QRect(1, 2, 139, 10))
        self.label_id12.setMinimumSize(QSize(0, 10))
        self.label_id12.setMaximumSize(QSize(16777215, 10))
        self.label_id12.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Slider_Servo12 = QSlider(self.frame_12)
        self.Slider_Servo12.setObjectName(u"Slider_Servo12")
        self.Slider_Servo12.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo12.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo12.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo12.setMinimum(0)
        self.Slider_Servo12.setMaximum(240)
        self.Slider_Servo12.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo12.setInvertedAppearance(False)
        self.Slider_Servo12.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo12.setTickInterval(1)
        self.lineEdit_servo12 = QLineEdit(self.frame_12)
        self.lineEdit_servo12.setObjectName(u"lineEdit_servo12")
        self.lineEdit_servo12.setEnabled(True)
        self.lineEdit_servo12.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo12.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo12.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time12 = QLineEdit(self.frame_12)
        self.lineEdit_time12.setObjectName(u"lineEdit_time12")
        self.lineEdit_time12.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time12.setMaximumSize(QSize(120, 15))
        self.lineEdit_time12.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time12.setDragEnabled(False)

        self.horizontalLayout_2.addWidget(self.frame_12)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_19 = QFrame(self.layoutWidget2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setEnabled(True)
        self.frame_19.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_19.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.label_id13 = QLabel(self.frame_19)
        self.label_id13.setObjectName(u"label_id13")
        self.label_id13.setGeometry(QRect(1, 2, 139, 10))
        self.label_id13.setMinimumSize(QSize(0, 10))
        self.label_id13.setMaximumSize(QSize(16777215, 10))
        self.label_id13.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Slider_Servo13 = QSlider(self.frame_19)
        self.Slider_Servo13.setObjectName(u"Slider_Servo13")
        self.Slider_Servo13.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo13.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo13.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo13.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo13.setMinimum(0)
        self.Slider_Servo13.setMaximum(240)
        self.Slider_Servo13.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo13.setInvertedAppearance(False)
        self.Slider_Servo13.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo13.setTickInterval(1)
        self.lineEdit_servo13 = QLineEdit(self.frame_19)
        self.lineEdit_servo13.setObjectName(u"lineEdit_servo13")
        self.lineEdit_servo13.setEnabled(True)
        self.lineEdit_servo13.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo13.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo13.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo13.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time13 = QLineEdit(self.frame_19)
        self.lineEdit_time13.setObjectName(u"lineEdit_time13")
        self.lineEdit_time13.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time13.setMaximumSize(QSize(120, 15))
        self.lineEdit_time13.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time13.setDragEnabled(False)

        self.horizontalLayout_4.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.layoutWidget2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setEnabled(True)
        self.frame_20.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_20.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.Slider_Servo14 = QSlider(self.frame_20)
        self.Slider_Servo14.setObjectName(u"Slider_Servo14")
        self.Slider_Servo14.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo14.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo14.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo14.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo14.setMinimum(0)
        self.Slider_Servo14.setMaximum(240)
        self.Slider_Servo14.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo14.setInvertedAppearance(False)
        self.Slider_Servo14.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo14.setTickInterval(1)
        self.lineEdit_servo14 = QLineEdit(self.frame_20)
        self.lineEdit_servo14.setObjectName(u"lineEdit_servo14")
        self.lineEdit_servo14.setEnabled(True)
        self.lineEdit_servo14.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo14.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo14.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo14.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time14 = QLineEdit(self.frame_20)
        self.lineEdit_time14.setObjectName(u"lineEdit_time14")
        self.lineEdit_time14.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time14.setMaximumSize(QSize(120, 15))
        self.lineEdit_time14.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time14.setDragEnabled(False)
        self.label_id14 = QLabel(self.frame_20)
        self.label_id14.setObjectName(u"label_id14")
        self.label_id14.setGeometry(QRect(1, 2, 139, 10))
        self.label_id14.setMinimumSize(QSize(0, 10))
        self.label_id14.setMaximumSize(QSize(16777215, 10))
        self.label_id14.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.layoutWidget2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setEnabled(True)
        self.frame_21.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_21.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.label_id15 = QLabel(self.frame_21)
        self.label_id15.setObjectName(u"label_id15")
        self.label_id15.setGeometry(QRect(1, 2, 139, 10))
        self.label_id15.setMinimumSize(QSize(0, 10))
        self.label_id15.setMaximumSize(QSize(16777215, 10))
        self.label_id15.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_servo15 = QLineEdit(self.frame_21)
        self.lineEdit_servo15.setObjectName(u"lineEdit_servo15")
        self.lineEdit_servo15.setEnabled(True)
        self.lineEdit_servo15.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo15.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo15.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo15.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Slider_Servo15 = QSlider(self.frame_21)
        self.Slider_Servo15.setObjectName(u"Slider_Servo15")
        self.Slider_Servo15.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo15.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo15.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo15.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo15.setMinimum(0)
        self.Slider_Servo15.setMaximum(240)
        self.Slider_Servo15.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo15.setInvertedAppearance(False)
        self.Slider_Servo15.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo15.setTickInterval(1)
        self.lineEdit_time15 = QLineEdit(self.frame_21)
        self.lineEdit_time15.setObjectName(u"lineEdit_time15")
        self.lineEdit_time15.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time15.setMaximumSize(QSize(120, 15))
        self.lineEdit_time15.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time15.setDragEnabled(False)

        self.horizontalLayout_4.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.layoutWidget2)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setEnabled(True)
        self.frame_22.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_22.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.label_id16 = QLabel(self.frame_22)
        self.label_id16.setObjectName(u"label_id16")
        self.label_id16.setGeometry(QRect(1, 2, 139, 10))
        self.label_id16.setMinimumSize(QSize(0, 10))
        self.label_id16.setMaximumSize(QSize(16777215, 10))
        self.label_id16.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Slider_Servo16 = QSlider(self.frame_22)
        self.Slider_Servo16.setObjectName(u"Slider_Servo16")
        self.Slider_Servo16.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo16.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo16.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo16.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo16.setMinimum(0)
        self.Slider_Servo16.setMaximum(240)
        self.Slider_Servo16.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo16.setInvertedAppearance(False)
        self.Slider_Servo16.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo16.setTickInterval(1)
        self.lineEdit_servo16 = QLineEdit(self.frame_22)
        self.lineEdit_servo16.setObjectName(u"lineEdit_servo16")
        self.lineEdit_servo16.setEnabled(True)
        self.lineEdit_servo16.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo16.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo16.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo16.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time16 = QLineEdit(self.frame_22)
        self.lineEdit_time16.setObjectName(u"lineEdit_time16")
        self.lineEdit_time16.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time16.setMaximumSize(QSize(120, 15))
        self.lineEdit_time16.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time16.setDragEnabled(False)

        self.horizontalLayout_4.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.layoutWidget2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setEnabled(True)
        self.frame_23.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_23.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_servo17 = QLineEdit(self.frame_23)
        self.lineEdit_servo17.setObjectName(u"lineEdit_servo17")
        self.lineEdit_servo17.setEnabled(True)
        self.lineEdit_servo17.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo17.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo17.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo17.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_id17 = QLabel(self.frame_23)
        self.label_id17.setObjectName(u"label_id17")
        self.label_id17.setGeometry(QRect(1, 2, 139, 10))
        self.label_id17.setMinimumSize(QSize(0, 10))
        self.label_id17.setMaximumSize(QSize(16777215, 10))
        self.label_id17.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Slider_Servo17 = QSlider(self.frame_23)
        self.Slider_Servo17.setObjectName(u"Slider_Servo17")
        self.Slider_Servo17.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo17.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo17.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo17.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo17.setMinimum(0)
        self.Slider_Servo17.setMaximum(240)
        self.Slider_Servo17.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo17.setInvertedAppearance(False)
        self.Slider_Servo17.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo17.setTickInterval(1)
        self.lineEdit_time17 = QLineEdit(self.frame_23)
        self.lineEdit_time17.setObjectName(u"lineEdit_time17")
        self.lineEdit_time17.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time17.setMaximumSize(QSize(120, 15))
        self.lineEdit_time17.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time17.setDragEnabled(False)

        self.horizontalLayout_4.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.layoutWidget2)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setEnabled(True)
        self.frame_24.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_24.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.Slider_Servo18 = QSlider(self.frame_24)
        self.Slider_Servo18.setObjectName(u"Slider_Servo18")
        self.Slider_Servo18.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo18.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo18.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo18.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo18.setMinimum(0)
        self.Slider_Servo18.setMaximum(240)
        self.Slider_Servo18.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo18.setInvertedAppearance(False)
        self.Slider_Servo18.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo18.setTickInterval(1)
        self.label_id18 = QLabel(self.frame_24)
        self.label_id18.setObjectName(u"label_id18")
        self.label_id18.setGeometry(QRect(1, 2, 139, 10))
        self.label_id18.setMinimumSize(QSize(0, 10))
        self.label_id18.setMaximumSize(QSize(16777215, 10))
        self.label_id18.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_servo18 = QLineEdit(self.frame_24)
        self.lineEdit_servo18.setObjectName(u"lineEdit_servo18")
        self.lineEdit_servo18.setEnabled(True)
        self.lineEdit_servo18.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo18.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo18.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo18.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time18 = QLineEdit(self.frame_24)
        self.lineEdit_time18.setObjectName(u"lineEdit_time18")
        self.lineEdit_time18.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time18.setMaximumSize(QSize(120, 15))
        self.lineEdit_time18.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time18.setDragEnabled(False)

        self.horizontalLayout_4.addWidget(self.frame_24)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_13 = QFrame(self.layoutWidget2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setEnabled(True)
        self.frame_13.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_13.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_time19 = QLineEdit(self.frame_13)
        self.lineEdit_time19.setObjectName(u"lineEdit_time19")
        self.lineEdit_time19.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time19.setMaximumSize(QSize(120, 15))
        self.lineEdit_time19.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time19.setDragEnabled(False)
        self.lineEdit_servo19 = QLineEdit(self.frame_13)
        self.lineEdit_servo19.setObjectName(u"lineEdit_servo19")
        self.lineEdit_servo19.setEnabled(True)
        self.lineEdit_servo19.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo19.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo19.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo19.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Slider_Servo19 = QSlider(self.frame_13)
        self.Slider_Servo19.setObjectName(u"Slider_Servo19")
        self.Slider_Servo19.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo19.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo19.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo19.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo19.setMinimum(0)
        self.Slider_Servo19.setMaximum(240)
        self.Slider_Servo19.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo19.setInvertedAppearance(False)
        self.Slider_Servo19.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo19.setTickInterval(1)
        self.label_id19 = QLabel(self.frame_13)
        self.label_id19.setObjectName(u"label_id19")
        self.label_id19.setGeometry(QRect(1, 2, 139, 10))
        self.label_id19.setMinimumSize(QSize(0, 10))
        self.label_id19.setMaximumSize(QSize(16777215, 10))
        self.label_id19.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.layoutWidget2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setEnabled(True)
        self.frame_14.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_14.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.Slider_Servo20 = QSlider(self.frame_14)
        self.Slider_Servo20.setObjectName(u"Slider_Servo20")
        self.Slider_Servo20.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo20.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo20.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo20.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo20.setMinimum(0)
        self.Slider_Servo20.setMaximum(240)
        self.Slider_Servo20.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo20.setInvertedAppearance(False)
        self.Slider_Servo20.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo20.setTickInterval(1)
        self.label_id20 = QLabel(self.frame_14)
        self.label_id20.setObjectName(u"label_id20")
        self.label_id20.setGeometry(QRect(1, 2, 139, 10))
        self.label_id20.setMinimumSize(QSize(0, 10))
        self.label_id20.setMaximumSize(QSize(16777215, 10))
        self.label_id20.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_servo20 = QLineEdit(self.frame_14)
        self.lineEdit_servo20.setObjectName(u"lineEdit_servo20")
        self.lineEdit_servo20.setEnabled(True)
        self.lineEdit_servo20.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo20.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo20.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo20.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time20 = QLineEdit(self.frame_14)
        self.lineEdit_time20.setObjectName(u"lineEdit_time20")
        self.lineEdit_time20.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time20.setMaximumSize(QSize(120, 15))
        self.lineEdit_time20.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time20.setDragEnabled(False)

        self.horizontalLayout_3.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.layoutWidget2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setEnabled(True)
        self.frame_15.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_15.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_time21 = QLineEdit(self.frame_15)
        self.lineEdit_time21.setObjectName(u"lineEdit_time21")
        self.lineEdit_time21.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time21.setMaximumSize(QSize(120, 15))
        self.lineEdit_time21.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time21.setDragEnabled(False)
        self.label_id21 = QLabel(self.frame_15)
        self.label_id21.setObjectName(u"label_id21")
        self.label_id21.setGeometry(QRect(1, 2, 139, 10))
        self.label_id21.setMinimumSize(QSize(0, 10))
        self.label_id21.setMaximumSize(QSize(16777215, 10))
        self.label_id21.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_servo21 = QLineEdit(self.frame_15)
        self.lineEdit_servo21.setObjectName(u"lineEdit_servo21")
        self.lineEdit_servo21.setEnabled(True)
        self.lineEdit_servo21.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo21.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo21.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo21.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Slider_Servo21 = QSlider(self.frame_15)
        self.Slider_Servo21.setObjectName(u"Slider_Servo21")
        self.Slider_Servo21.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo21.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo21.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo21.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo21.setMinimum(0)
        self.Slider_Servo21.setMaximum(240)
        self.Slider_Servo21.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo21.setInvertedAppearance(False)
        self.Slider_Servo21.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo21.setTickInterval(1)

        self.horizontalLayout_3.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.layoutWidget2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setEnabled(True)
        self.frame_16.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_16.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.Slider_Servo22 = QSlider(self.frame_16)
        self.Slider_Servo22.setObjectName(u"Slider_Servo22")
        self.Slider_Servo22.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo22.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo22.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo22.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo22.setMinimum(0)
        self.Slider_Servo22.setMaximum(240)
        self.Slider_Servo22.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo22.setInvertedAppearance(False)
        self.Slider_Servo22.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo22.setTickInterval(1)
        self.lineEdit_time22 = QLineEdit(self.frame_16)
        self.lineEdit_time22.setObjectName(u"lineEdit_time22")
        self.lineEdit_time22.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time22.setMaximumSize(QSize(120, 15))
        self.lineEdit_time22.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time22.setDragEnabled(False)
        self.label_id22 = QLabel(self.frame_16)
        self.label_id22.setObjectName(u"label_id22")
        self.label_id22.setGeometry(QRect(1, 2, 139, 10))
        self.label_id22.setMinimumSize(QSize(0, 10))
        self.label_id22.setMaximumSize(QSize(16777215, 10))
        self.label_id22.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_servo22 = QLineEdit(self.frame_16)
        self.lineEdit_servo22.setObjectName(u"lineEdit_servo22")
        self.lineEdit_servo22.setEnabled(True)
        self.lineEdit_servo22.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo22.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo22.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo22.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.layoutWidget2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setEnabled(True)
        self.frame_17.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_17.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_servo23 = QLineEdit(self.frame_17)
        self.lineEdit_servo23.setObjectName(u"lineEdit_servo23")
        self.lineEdit_servo23.setEnabled(True)
        self.lineEdit_servo23.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo23.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo23.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo23.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time23 = QLineEdit(self.frame_17)
        self.lineEdit_time23.setObjectName(u"lineEdit_time23")
        self.lineEdit_time23.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time23.setMaximumSize(QSize(120, 15))
        self.lineEdit_time23.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time23.setDragEnabled(False)
        self.Slider_Servo23 = QSlider(self.frame_17)
        self.Slider_Servo23.setObjectName(u"Slider_Servo23")
        self.Slider_Servo23.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo23.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo23.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo23.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo23.setMinimum(0)
        self.Slider_Servo23.setMaximum(240)
        self.Slider_Servo23.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo23.setInvertedAppearance(False)
        self.Slider_Servo23.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo23.setTickInterval(1)
        self.label_id23 = QLabel(self.frame_17)
        self.label_id23.setObjectName(u"label_id23")
        self.label_id23.setGeometry(QRect(1, 2, 139, 10))
        self.label_id23.setMinimumSize(QSize(0, 10))
        self.label_id23.setMaximumSize(QSize(16777215, 10))
        self.label_id23.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.layoutWidget2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setEnabled(True)
        self.frame_18.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_18.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_servo24 = QLineEdit(self.frame_18)
        self.lineEdit_servo24.setObjectName(u"lineEdit_servo24")
        self.lineEdit_servo24.setEnabled(True)
        self.lineEdit_servo24.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo24.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo24.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_servo24.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_servo24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time24 = QLineEdit(self.frame_18)
        self.lineEdit_time24.setObjectName(u"lineEdit_time24")
        self.lineEdit_time24.setGeometry(QRect(17, 61, 106, 15))
        self.lineEdit_time24.setMaximumSize(QSize(120, 15))
        self.lineEdit_time24.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_time24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_time24.setDragEnabled(False)
        self.Slider_Servo24 = QSlider(self.frame_18)
        self.Slider_Servo24.setObjectName(u"Slider_Servo24")
        self.Slider_Servo24.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo24.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo24.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Slider_Servo24.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 10px;\n"
"    background-color: lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 12px; /* \u589e\u5927\u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -1px 0px -1px -5px;\n"
"    border-radius: 6px; /* \u4e5f\u53ef\u4ee5\u8c03\u6574\u5706\u89d2\u534a\u5f84\u4ee5\u5339\u914d\u6ed1\u5757\u7684\u5927\u5c0f */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.Slider_Servo24.setMinimum(0)
        self.Slider_Servo24.setMaximum(240)
        self.Slider_Servo24.setOrientation(Qt.Orientation.Horizontal)
        self.Slider_Servo24.setInvertedAppearance(False)
        self.Slider_Servo24.setTickPosition(QSlider.TickPosition.NoTicks)
        self.Slider_Servo24.setTickInterval(1)
        self.label_id24 = QLabel(self.frame_18)
        self.label_id24.setObjectName(u"label_id24")
        self.label_id24.setGeometry(QRect(1, 2, 139, 10))
        self.label_id24.setMinimumSize(QSize(0, 10))
        self.label_id24.setMaximumSize(QSize(16777215, 10))
        self.label_id24.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.frame_18)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.pushButton_init = QPushButton(self.tab_3)
        self.pushButton_init.setObjectName(u"pushButton_init")
        self.pushButton_init.setGeometry(QRect(870, 10, 81, 51))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(False)
        self.pushButton_init.setFont(font5)
        self.pushButton_init.setAutoFillBackground(False)
        self.pushButton_init.setStyleSheet(u"QPushButton {\n"
"    background: white;  /* \u80cc\u666f\u8272\u4e3a\u767d\u8272 */\n"
"    border: 2px solid #59969b;  /* \u8bbe\u7f6e\u8fb9\u6846\u989c\u8272\u548c\u5bbd\u5ea6 */\n"
"    border-radius: 20px;  /* \u5706\u89d2\u8fb9\u6846 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #f0f0f0;  /* \u60ac\u505c\u65f6\u80cc\u666f\u989c\u8272\u53d8\u5316 */\n"
"    border-color: #4a7b87;  /* \u60ac\u505c\u65f6\u8fb9\u6846\u989c\u8272\u53d8\u5316 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #e0e0e0;  /* \u6309\u4e0b\u65f6\u80cc\u666f\u989c\u8272\u53d8\u5316 */\n"
"    border-color: #3e6c72;  /* \u6309\u4e0b\u65f6\u8fb9\u6846\u989c\u8272\u53d8\u5316 */\n"
"}\n"
"")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.layoutWidget3 = QWidget(self.tab_2)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 0, 391, 351))
        self.verticalLayout = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_addFrame = QPushButton(self.layoutWidget3)
        self.pushButton_addFrame.setObjectName(u"pushButton_addFrame")
        self.pushButton_addFrame.setFont(font4)

        self.verticalLayout.addWidget(self.pushButton_addFrame)

        self.pushButton_delay = QPushButton(self.layoutWidget3)
        self.pushButton_delay.setObjectName(u"pushButton_delay")
        self.pushButton_delay.setFont(font4)

        self.verticalLayout.addWidget(self.pushButton_delay)

        self.pushButton_insertmove = QPushButton(self.layoutWidget3)
        self.pushButton_insertmove.setObjectName(u"pushButton_insertmove")
        self.pushButton_insertmove.setFont(font4)

        self.verticalLayout.addWidget(self.pushButton_insertmove)

        self.pushButton_insertdelay = QPushButton(self.layoutWidget3)
        self.pushButton_insertdelay.setObjectName(u"pushButton_insertdelay")
        self.pushButton_insertdelay.setFont(font4)

        self.verticalLayout.addWidget(self.pushButton_insertdelay)

        self.pushButton_playGroup = QPushButton(self.layoutWidget3)
        self.pushButton_playGroup.setObjectName(u"pushButton_playGroup")
        self.pushButton_playGroup.setFont(font4)

        self.verticalLayout.addWidget(self.pushButton_playGroup)

        self.pushButton_clearline = QPushButton(self.layoutWidget3)
        self.pushButton_clearline.setObjectName(u"pushButton_clearline")
        self.pushButton_clearline.setFont(font4)

        self.verticalLayout.addWidget(self.pushButton_clearline)

        self.pushButton_clearFrames = QPushButton(self.layoutWidget3)
        self.pushButton_clearFrames.setObjectName(u"pushButton_clearFrames")
        self.pushButton_clearFrames.setFont(font4)

        self.verticalLayout.addWidget(self.pushButton_clearFrames)

        self.frame_25 = QFrame(self.tab_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setEnabled(True)
        self.frame_25.setGeometry(QRect(400, 10, 138, 81))
        self.frame_25.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_25.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_idinput = QLineEdit(self.frame_25)
        self.lineEdit_idinput.setObjectName(u"lineEdit_idinput")
        self.lineEdit_idinput.setEnabled(True)
        self.lineEdit_idinput.setGeometry(QRect(20, 10, 106, 18))
        self.lineEdit_idinput.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_idinput.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_idinput.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_idinput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_timeinput = QLineEdit(self.frame_25)
        self.lineEdit_timeinput.setObjectName(u"lineEdit_timeinput")
        self.lineEdit_timeinput.setGeometry(QRect(20, 50, 106, 15))
        self.lineEdit_timeinput.setMaximumSize(QSize(120, 15))
        self.lineEdit_timeinput.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_timeinput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_timeinput.setDragEnabled(False)
        self.lineEdit_angleinput = QLineEdit(self.frame_25)
        self.lineEdit_angleinput.setObjectName(u"lineEdit_angleinput")
        self.lineEdit_angleinput.setEnabled(True)
        self.lineEdit_angleinput.setGeometry(QRect(20, 30, 106, 18))
        self.lineEdit_angleinput.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_angleinput.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_angleinput.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_angleinput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_26 = QFrame(self.tab_2)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setEnabled(True)
        self.frame_26.setGeometry(QRect(400, 100, 138, 51))
        self.frame_26.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_26.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_delay = QLineEdit(self.frame_26)
        self.lineEdit_delay.setObjectName(u"lineEdit_delay")
        self.lineEdit_delay.setGeometry(QRect(20, 20, 106, 15))
        self.lineEdit_delay.setMaximumSize(QSize(120, 15))
        self.lineEdit_delay.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_delay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_delay.setDragEnabled(False)
        self.frame_28 = QFrame(self.tab_2)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setEnabled(True)
        self.frame_28.setGeometry(QRect(400, 160, 138, 51))
        self.frame_28.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_28.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_confirm = QLineEdit(self.frame_28)
        self.lineEdit_confirm.setObjectName(u"lineEdit_confirm")
        self.lineEdit_confirm.setGeometry(QRect(20, 20, 106, 15))
        self.lineEdit_confirm.setMaximumSize(QSize(120, 15))
        self.lineEdit_confirm.setStyleSheet(u"QLineEdit {\n"
"            border-top: none;\n"
"            border-left: none;\n"
"            border-right: none;\n"
"            border-bottom: 1px solid black;\n"
"            background-color: transparent;\n"
"        }\n"
"        \n"
"        QLineEdit:focus {\n"
"            border-bottom: 1px solid #2a70f4;\n"
"        }")
        self.lineEdit_confirm.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_confirm.setDragEnabled(False)
        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(400, 220, 151, 41))
        self.pushButton.setFont(font1)
        self.pushButton_paste = QPushButton(self.tab_2)
        self.pushButton_paste.setObjectName(u"pushButton_paste")
        self.pushButton_paste.setGeometry(QRect(400, 260, 151, 41))
        self.pushButton_paste.setFont(font1)
        self.pushButton_init_2 = QPushButton(self.tab_2)
        self.pushButton_init_2.setObjectName(u"pushButton_init_2")
        self.pushButton_init_2.setGeometry(QRect(400, 300, 151, 41))
        self.pushButton_init_2.setFont(font1)
        self.textedit_output = QTextEdit(self.tab_2)
        self.textedit_output.setObjectName(u"textedit_output")
        self.textedit_output.setGeometry(QRect(560, 10, 411, 321))
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"")
        self.textEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit)

        self.pushButton_clean = QPushButton(Form)
        self.pushButton_clean.setObjectName(u"pushButton_clean")
        self.pushButton_clean.setFont(font5)
        self.pushButton_clean.setStyleSheet(u"QPushButton {\n"
"    background: white;  /* \u80cc\u666f\u8272\u4e3a\u767d\u8272 */\n"
"    border: 2px solid #59969b;  /* \u8bbe\u7f6e\u8fb9\u6846\u989c\u8272\u548c\u5bbd\u5ea6 */\n"
"    border-radius: 20px;  /* \u5706\u89d2\u8fb9\u6846 */ \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #f0f0f0;  /* \u60ac\u505c\u65f6\u80cc\u666f\u989c\u8272\u53d8\u5316 */\n"
"    border-color: #4a7b87;  /* \u60ac\u505c\u65f6\u8fb9\u6846\u989c\u8272\u53d8\u5316 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #e0e0e0;  /* \u6309\u4e0b\u65f6\u80cc\u666f\u989c\u8272\u53d8\u5316 */\n"
"    border-color: #3e6c72;  /* \u6309\u4e0b\u65f6\u8fb9\u6846\u989c\u8272\u53d8\u5316 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton_clean)


        self.retranslateUi(Form)
        self.textedit_output.textChanged.connect(Form.add_index)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u821e\u8e48\u673a\u5668\u4eba\u8c03\u8bd5\u5de5\u5177", None))
        self.pushButton_create.setText(QCoreApplication.translate("Form", u"\u521b\u5efa\u673a\u5668\u4eba\u914d\u7f6e", None))
        self.pushButton_importinit.setText(QCoreApplication.translate("Form", u"\u5bfc\u5165\u673a\u5668\u4eba\u914d\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u4e32\u53e3\uff1a", None))
        self.labelID.setText(QCoreApplication.translate("Form", u"\u8235\u673aid\uff1a", None))
        self.pushButton_broadcast.setText(QCoreApplication.translate("Form", u"\u5e7f\u64ad\u4fee\u6539", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u57fa\u7840\u914d\u7f6e\u754c\u9762", None))
        self.lineEdit_servo1.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id1.setText(QCoreApplication.translate("Form", u"ID:1\u5de6\u80a9", None))
        self.lineEdit_time1.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.label_id2.setText(QCoreApplication.translate("Form", u"ID:2\u5de6\u81c2", None))
        self.lineEdit_servo2.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_time2.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.lineEdit_time3.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.lineEdit_servo3.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id3.setText(QCoreApplication.translate("Form", u"ID:3\u5de6\u624b", None))
        self.lineEdit_time4.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.label_id4.setText(QCoreApplication.translate("Form", u"ID:4\u53f3\u80a9", None))
        self.lineEdit_servo4.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id5.setText(QCoreApplication.translate("Form", u"ID:5\u53f3\u81c2", None))
        self.lineEdit_servo5.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_time5.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.label_id6.setText(QCoreApplication.translate("Form", u"ID:6\u53f3\u624b", None))
        self.lineEdit_time6.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.lineEdit_servo6.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id7.setText(QCoreApplication.translate("Form", u"ID:7\u5de6\u80ef", None))
        self.lineEdit_time7.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.lineEdit_servo7.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_time8.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.lineEdit_servo8.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id8.setText(QCoreApplication.translate("Form", u"ID:8\u5de6\u5927\u817f", None))
        self.lineEdit_time9.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.lineEdit_servo9.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id9.setText(QCoreApplication.translate("Form", u"ID:9\u5de6\u5c0f\u817f", None))
        self.lineEdit_servo10.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id10.setText(QCoreApplication.translate("Form", u"ID:10\u5de6\u811a", None))
        self.lineEdit_time10.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.label_id11.setText(QCoreApplication.translate("Form", u"ID:11\u5de6\u811a\u8155", None))
        self.lineEdit_servo11.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_time11.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.label_id12.setText(QCoreApplication.translate("Form", u"ID:12\u53f3\u80ef", None))
        self.lineEdit_servo12.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_time12.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.label_id13.setText(QCoreApplication.translate("Form", u"ID:13\u53f3\u5927\u817f", None))
        self.lineEdit_servo13.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_time13.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.lineEdit_servo14.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_time14.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.label_id14.setText(QCoreApplication.translate("Form", u"ID:14\u53f3\u5c0f\u817f", None))
        self.label_id15.setText(QCoreApplication.translate("Form", u"ID:15\u53f3\u811a", None))
        self.lineEdit_servo15.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_time15.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.label_id16.setText(QCoreApplication.translate("Form", u"ID:16\u53f3\u811a\u8155", None))
        self.lineEdit_servo16.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_time16.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.lineEdit_servo17.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id17.setText(QCoreApplication.translate("Form", u"ID:17", None))
        self.lineEdit_time17.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.label_id18.setText(QCoreApplication.translate("Form", u"ID:18", None))
        self.lineEdit_servo18.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_time18.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.lineEdit_time19.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.lineEdit_servo19.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id19.setText(QCoreApplication.translate("Form", u"ID:19", None))
        self.label_id20.setText(QCoreApplication.translate("Form", u"ID:20", None))
        self.lineEdit_servo20.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_time20.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.lineEdit_time21.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.label_id21.setText(QCoreApplication.translate("Form", u"ID:21", None))
        self.lineEdit_servo21.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_time22.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.label_id22.setText(QCoreApplication.translate("Form", u"ID:22", None))
        self.lineEdit_servo22.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_servo23.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_time23.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.label_id23.setText(QCoreApplication.translate("Form", u"ID:23", None))
        self.lineEdit_servo24.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_time24.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.label_id24.setText(QCoreApplication.translate("Form", u"ID:24", None))
        self.pushButton_init.setText(QCoreApplication.translate("Form", u"\u4e00\u952e\u521d\u59cb\u5316", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u901a\u7528\u6a21\u5f0f", None))
        self.pushButton_addFrame.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u5f53\u524d\u5e27", None))
        self.pushButton_delay.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u5ef6\u65f6", None))
        self.pushButton_insertmove.setText(QCoreApplication.translate("Form", u"\u5728\u6307\u5b9a\u884c\u4e4b\u4e0a\u63d2\u5165\u5e27", None))
        self.pushButton_insertdelay.setText(QCoreApplication.translate("Form", u"\u5728\u6307\u5b9a\u884c\u4e4b\u4e0a\u63d2\u5165\u5ef6\u65f6", None))
        self.pushButton_playGroup.setText(QCoreApplication.translate("Form", u"\u64ad\u653e\u52a8\u4f5c\u7ec4", None))
        self.pushButton_clearline.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u6307\u5b9a\u884c", None))
        self.pushButton_clearFrames.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u6240\u6709\u5e27", None))
        self.lineEdit_idinput.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165ID", None))
        self.lineEdit_timeinput.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u65f6\u95f4", None))
        self.lineEdit_angleinput.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_delay.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u5ef6\u65f6\u65f6\u95f4", None))
        self.lineEdit_confirm.setPlaceholderText(QCoreApplication.translate("Form", u"\u6a21\u62df\u5149\u6807\u6307\u5b9a\u884c", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"copy", None))
        self.pushButton_paste.setText(QCoreApplication.translate("Form", u"paste", None))
        self.pushButton_init_2.setText(QCoreApplication.translate("Form", u"init", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u7f16\u5199\u821e\u8e48\u7ec4", None))
        self.pushButton_clean.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u7ec8\u7aef\u8f93\u51fa", None))
    # retranslateUi

