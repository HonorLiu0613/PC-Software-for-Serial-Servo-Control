# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

class Ui_Form2(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(860, 422)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 861, 351))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.layoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setLayoutDirection(Qt.RightToLeft)
        self.frame.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Slider_Servo1 = QSlider(self.frame)
        self.Slider_Servo1.setObjectName(u"Slider_Servo1")
        self.Slider_Servo1.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo1.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo1.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo1.setOrientation(Qt.Horizontal)
        self.Slider_Servo1.setInvertedAppearance(False)
        self.Slider_Servo1.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo1.setTickInterval(1)
        self.lineEdit_servo1 = QLineEdit(self.frame)
        self.lineEdit_servo1.setObjectName(u"lineEdit_servo1")
        self.lineEdit_servo1.setEnabled(True)
        self.lineEdit_servo1.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo1.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo1.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo1.setAlignment(Qt.AlignCenter)
        self.label_id1 = QLabel(self.frame)
        self.label_id1.setObjectName(u"label_id1")
        self.label_id1.setGeometry(QRect(1, 2, 139, 10))
        self.label_id1.setMinimumSize(QSize(0, 10))
        self.label_id1.setMaximumSize(QSize(16777215, 10))
        self.label_id1.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.layoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setLayoutDirection(Qt.RightToLeft)
        self.frame_2.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_id2 = QLabel(self.frame_2)
        self.label_id2.setObjectName(u"label_id2")
        self.label_id2.setGeometry(QRect(1, 1, 139, 10))
        self.label_id2.setMinimumSize(QSize(0, 10))
        self.label_id2.setMaximumSize(QSize(16777215, 10))
        self.label_id2.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"border: none; ")
        self.label_id2.setAlignment(Qt.AlignCenter)
        self.lineEdit_servo2 = QLineEdit(self.frame_2)
        self.lineEdit_servo2.setObjectName(u"lineEdit_servo2")
        self.lineEdit_servo2.setEnabled(True)
        self.lineEdit_servo2.setGeometry(QRect(17, 33, 106, 31))
        self.lineEdit_servo2.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo2.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo2.setAlignment(Qt.AlignCenter)
        self.Slider_Servo2 = QSlider(self.frame_2)
        self.Slider_Servo2.setObjectName(u"Slider_Servo2")
        self.Slider_Servo2.setGeometry(QRect(1, 17, 139, 10))
        self.Slider_Servo2.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo2.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo2.setOrientation(Qt.Horizontal)
        self.Slider_Servo2.setInvertedAppearance(False)
        self.Slider_Servo2.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo2.setTickInterval(1)

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.layoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setLayoutDirection(Qt.RightToLeft)
        self.frame_3.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lineEdit_servo3 = QLineEdit(self.frame_3)
        self.lineEdit_servo3.setObjectName(u"lineEdit_servo3")
        self.lineEdit_servo3.setEnabled(True)
        self.lineEdit_servo3.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo3.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo3.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo3.setAlignment(Qt.AlignCenter)
        self.Slider_Servo3 = QSlider(self.frame_3)
        self.Slider_Servo3.setObjectName(u"Slider_Servo3")
        self.Slider_Servo3.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo3.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo3.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo3.setOrientation(Qt.Horizontal)
        self.Slider_Servo3.setInvertedAppearance(False)
        self.Slider_Servo3.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo3.setTickInterval(1)
        self.label_id3 = QLabel(self.frame_3)
        self.label_id3.setObjectName(u"label_id3")
        self.label_id3.setGeometry(QRect(1, 2, 139, 10))
        self.label_id3.setMinimumSize(QSize(0, 10))
        self.label_id3.setMaximumSize(QSize(16777215, 10))
        self.label_id3.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.layoutWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setEnabled(True)
        self.frame_4.setLayoutDirection(Qt.RightToLeft)
        self.frame_4.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_id4 = QLabel(self.frame_4)
        self.label_id4.setObjectName(u"label_id4")
        self.label_id4.setGeometry(QRect(1, 2, 139, 10))
        self.label_id4.setMinimumSize(QSize(0, 10))
        self.label_id4.setMaximumSize(QSize(16777215, 10))
        self.label_id4.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id4.setAlignment(Qt.AlignCenter)
        self.lineEdit_servo4 = QLineEdit(self.frame_4)
        self.lineEdit_servo4.setObjectName(u"lineEdit_servo4")
        self.lineEdit_servo4.setEnabled(True)
        self.lineEdit_servo4.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo4.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo4.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo4.setAlignment(Qt.AlignCenter)
        self.Slider_Servo4 = QSlider(self.frame_4)
        self.Slider_Servo4.setObjectName(u"Slider_Servo4")
        self.Slider_Servo4.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo4.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo4.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo4.setOrientation(Qt.Horizontal)
        self.Slider_Servo4.setInvertedAppearance(False)
        self.Slider_Servo4.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo4.setTickInterval(1)

        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.layoutWidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setEnabled(True)
        self.frame_5.setLayoutDirection(Qt.RightToLeft)
        self.frame_5.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_id5 = QLabel(self.frame_5)
        self.label_id5.setObjectName(u"label_id5")
        self.label_id5.setGeometry(QRect(1, 2, 139, 10))
        self.label_id5.setMinimumSize(QSize(0, 10))
        self.label_id5.setMaximumSize(QSize(16777215, 10))
        self.label_id5.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id5.setAlignment(Qt.AlignCenter)
        self.lineEdit_servo5 = QLineEdit(self.frame_5)
        self.lineEdit_servo5.setObjectName(u"lineEdit_servo5")
        self.lineEdit_servo5.setEnabled(True)
        self.lineEdit_servo5.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo5.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo5.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo5.setAlignment(Qt.AlignCenter)
        self.Slider_Servo5 = QSlider(self.frame_5)
        self.Slider_Servo5.setObjectName(u"Slider_Servo5")
        self.Slider_Servo5.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo5.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo5.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo5.setOrientation(Qt.Horizontal)
        self.Slider_Servo5.setInvertedAppearance(False)
        self.Slider_Servo5.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo5.setTickInterval(1)

        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.layoutWidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setEnabled(True)
        self.frame_6.setLayoutDirection(Qt.RightToLeft)
        self.frame_6.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_id6 = QLabel(self.frame_6)
        self.label_id6.setObjectName(u"label_id6")
        self.label_id6.setGeometry(QRect(1, 2, 139, 10))
        self.label_id6.setMinimumSize(QSize(0, 10))
        self.label_id6.setMaximumSize(QSize(16777215, 10))
        self.label_id6.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id6.setAlignment(Qt.AlignCenter)
        self.lineEdit_servo6 = QLineEdit(self.frame_6)
        self.lineEdit_servo6.setObjectName(u"lineEdit_servo6")
        self.lineEdit_servo6.setEnabled(True)
        self.lineEdit_servo6.setGeometry(QRect(17, 36, 106, 18))
        self.lineEdit_servo6.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo6.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo6.setAlignment(Qt.AlignCenter)
        self.Slider_Servo6 = QSlider(self.frame_6)
        self.Slider_Servo6.setObjectName(u"Slider_Servo6")
        self.Slider_Servo6.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo6.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo6.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo6.setOrientation(Qt.Horizontal)
        self.Slider_Servo6.setInvertedAppearance(False)
        self.Slider_Servo6.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo6.setTickInterval(1)

        self.horizontalLayout.addWidget(self.frame_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_7 = QFrame(self.layoutWidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setEnabled(True)
        self.frame_7.setLayoutDirection(Qt.RightToLeft)
        self.frame_7.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_id7 = QLabel(self.frame_7)
        self.label_id7.setObjectName(u"label_id7")
        self.label_id7.setGeometry(QRect(2, 4, 139, 10))
        self.label_id7.setMinimumSize(QSize(0, 10))
        self.label_id7.setMaximumSize(QSize(16777215, 10))
        self.label_id7.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id7.setAlignment(Qt.AlignCenter)
        self.lineEdit_servo7 = QLineEdit(self.frame_7)
        self.lineEdit_servo7.setObjectName(u"lineEdit_servo7")
        self.lineEdit_servo7.setEnabled(True)
        self.lineEdit_servo7.setGeometry(QRect(18, 38, 106, 31))
        self.lineEdit_servo7.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo7.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo7.setAlignment(Qt.AlignCenter)
        self.Slider_Servo7 = QSlider(self.frame_7)
        self.Slider_Servo7.setObjectName(u"Slider_Servo7")
        self.Slider_Servo7.setGeometry(QRect(2, 21, 139, 10))
        self.Slider_Servo7.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo7.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo7.setOrientation(Qt.Horizontal)
        self.Slider_Servo7.setInvertedAppearance(False)
        self.Slider_Servo7.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo7.setTickInterval(1)

        self.horizontalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.layoutWidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(True)
        self.frame_8.setLayoutDirection(Qt.RightToLeft)
        self.frame_8.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.lineEdit_servo8 = QLineEdit(self.frame_8)
        self.lineEdit_servo8.setObjectName(u"lineEdit_servo8")
        self.lineEdit_servo8.setEnabled(True)
        self.lineEdit_servo8.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo8.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo8.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo8.setAlignment(Qt.AlignCenter)
        self.label_id8 = QLabel(self.frame_8)
        self.label_id8.setObjectName(u"label_id8")
        self.label_id8.setGeometry(QRect(1, 2, 139, 10))
        self.label_id8.setMinimumSize(QSize(0, 10))
        self.label_id8.setMaximumSize(QSize(16777215, 10))
        self.label_id8.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id8.setAlignment(Qt.AlignCenter)
        self.Slider_Servo8 = QSlider(self.frame_8)
        self.Slider_Servo8.setObjectName(u"Slider_Servo8")
        self.Slider_Servo8.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo8.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo8.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo8.setOrientation(Qt.Horizontal)
        self.Slider_Servo8.setInvertedAppearance(False)
        self.Slider_Servo8.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo8.setTickInterval(1)

        self.horizontalLayout_2.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.layoutWidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setEnabled(True)
        self.frame_9.setLayoutDirection(Qt.RightToLeft)
        self.frame_9.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.Slider_Servo9 = QSlider(self.frame_9)
        self.Slider_Servo9.setObjectName(u"Slider_Servo9")
        self.Slider_Servo9.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo9.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo9.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo9.setOrientation(Qt.Horizontal)
        self.Slider_Servo9.setInvertedAppearance(False)
        self.Slider_Servo9.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo9.setTickInterval(1)
        self.lineEdit_servo9 = QLineEdit(self.frame_9)
        self.lineEdit_servo9.setObjectName(u"lineEdit_servo9")
        self.lineEdit_servo9.setEnabled(True)
        self.lineEdit_servo9.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo9.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo9.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo9.setAlignment(Qt.AlignCenter)
        self.label_id9 = QLabel(self.frame_9)
        self.label_id9.setObjectName(u"label_id9")
        self.label_id9.setGeometry(QRect(1, 2, 139, 10))
        self.label_id9.setMinimumSize(QSize(0, 10))
        self.label_id9.setMaximumSize(QSize(16777215, 10))
        self.label_id9.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.layoutWidget)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setEnabled(True)
        self.frame_10.setLayoutDirection(Qt.RightToLeft)
        self.frame_10.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.lineEdit_servo10 = QLineEdit(self.frame_10)
        self.lineEdit_servo10.setObjectName(u"lineEdit_servo10")
        self.lineEdit_servo10.setEnabled(True)
        self.lineEdit_servo10.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo10.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo10.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo10.setAlignment(Qt.AlignCenter)
        self.label_id10 = QLabel(self.frame_10)
        self.label_id10.setObjectName(u"label_id10")
        self.label_id10.setGeometry(QRect(1, 2, 139, 10))
        self.label_id10.setMinimumSize(QSize(0, 10))
        self.label_id10.setMaximumSize(QSize(16777215, 10))
        self.label_id10.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id10.setAlignment(Qt.AlignCenter)
        self.Slider_Servo10 = QSlider(self.frame_10)
        self.Slider_Servo10.setObjectName(u"Slider_Servo10")
        self.Slider_Servo10.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo10.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo10.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo10.setOrientation(Qt.Horizontal)
        self.Slider_Servo10.setInvertedAppearance(False)
        self.Slider_Servo10.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo10.setTickInterval(1)

        self.horizontalLayout_2.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.layoutWidget)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setEnabled(True)
        self.frame_11.setLayoutDirection(Qt.RightToLeft)
        self.frame_11.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_id11 = QLabel(self.frame_11)
        self.label_id11.setObjectName(u"label_id11")
        self.label_id11.setGeometry(QRect(1, 2, 139, 10))
        self.label_id11.setMinimumSize(QSize(0, 10))
        self.label_id11.setMaximumSize(QSize(16777215, 10))
        self.label_id11.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id11.setAlignment(Qt.AlignCenter)
        self.Slider_Servo11 = QSlider(self.frame_11)
        self.Slider_Servo11.setObjectName(u"Slider_Servo11")
        self.Slider_Servo11.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo11.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo11.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo11.setOrientation(Qt.Horizontal)
        self.Slider_Servo11.setInvertedAppearance(False)
        self.Slider_Servo11.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo11.setTickInterval(1)
        self.lineEdit_servo11 = QLineEdit(self.frame_11)
        self.lineEdit_servo11.setObjectName(u"lineEdit_servo11")
        self.lineEdit_servo11.setEnabled(True)
        self.lineEdit_servo11.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo11.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo11.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.layoutWidget)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setEnabled(True)
        self.frame_12.setLayoutDirection(Qt.RightToLeft)
        self.frame_12.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.label_id12 = QLabel(self.frame_12)
        self.label_id12.setObjectName(u"label_id12")
        self.label_id12.setGeometry(QRect(1, 2, 139, 10))
        self.label_id12.setMinimumSize(QSize(0, 10))
        self.label_id12.setMaximumSize(QSize(16777215, 10))
        self.label_id12.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id12.setAlignment(Qt.AlignCenter)
        self.Slider_Servo12 = QSlider(self.frame_12)
        self.Slider_Servo12.setObjectName(u"Slider_Servo12")
        self.Slider_Servo12.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo12.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo12.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo12.setOrientation(Qt.Horizontal)
        self.Slider_Servo12.setInvertedAppearance(False)
        self.Slider_Servo12.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo12.setTickInterval(1)
        self.lineEdit_servo12 = QLineEdit(self.frame_12)
        self.lineEdit_servo12.setObjectName(u"lineEdit_servo12")
        self.lineEdit_servo12.setEnabled(True)
        self.lineEdit_servo12.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo12.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo12.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.frame_12)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_19 = QFrame(self.layoutWidget)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setEnabled(True)
        self.frame_19.setLayoutDirection(Qt.RightToLeft)
        self.frame_19.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.label_id13 = QLabel(self.frame_19)
        self.label_id13.setObjectName(u"label_id13")
        self.label_id13.setGeometry(QRect(1, 2, 139, 10))
        self.label_id13.setMinimumSize(QSize(0, 10))
        self.label_id13.setMaximumSize(QSize(16777215, 10))
        self.label_id13.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id13.setAlignment(Qt.AlignCenter)
        self.Slider_Servo13 = QSlider(self.frame_19)
        self.Slider_Servo13.setObjectName(u"Slider_Servo13")
        self.Slider_Servo13.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo13.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo13.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo13.setOrientation(Qt.Horizontal)
        self.Slider_Servo13.setInvertedAppearance(False)
        self.Slider_Servo13.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo13.setTickInterval(1)
        self.lineEdit_servo13 = QLineEdit(self.frame_19)
        self.lineEdit_servo13.setObjectName(u"lineEdit_servo13")
        self.lineEdit_servo13.setEnabled(True)
        self.lineEdit_servo13.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo13.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo13.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.layoutWidget)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setEnabled(True)
        self.frame_20.setLayoutDirection(Qt.RightToLeft)
        self.frame_20.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.Slider_Servo14 = QSlider(self.frame_20)
        self.Slider_Servo14.setObjectName(u"Slider_Servo14")
        self.Slider_Servo14.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo14.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo14.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo14.setOrientation(Qt.Horizontal)
        self.Slider_Servo14.setInvertedAppearance(False)
        self.Slider_Servo14.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo14.setTickInterval(1)
        self.lineEdit_servo14 = QLineEdit(self.frame_20)
        self.lineEdit_servo14.setObjectName(u"lineEdit_servo14")
        self.lineEdit_servo14.setEnabled(True)
        self.lineEdit_servo14.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo14.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo14.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo14.setAlignment(Qt.AlignCenter)
        self.label_id14 = QLabel(self.frame_20)
        self.label_id14.setObjectName(u"label_id14")
        self.label_id14.setGeometry(QRect(1, 2, 139, 10))
        self.label_id14.setMinimumSize(QSize(0, 10))
        self.label_id14.setMaximumSize(QSize(16777215, 10))
        self.label_id14.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.layoutWidget)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setEnabled(True)
        self.frame_21.setLayoutDirection(Qt.RightToLeft)
        self.frame_21.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.label_id15 = QLabel(self.frame_21)
        self.label_id15.setObjectName(u"label_id15")
        self.label_id15.setGeometry(QRect(1, 2, 139, 10))
        self.label_id15.setMinimumSize(QSize(0, 10))
        self.label_id15.setMaximumSize(QSize(16777215, 10))
        self.label_id15.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id15.setAlignment(Qt.AlignCenter)
        self.lineEdit_servo15 = QLineEdit(self.frame_21)
        self.lineEdit_servo15.setObjectName(u"lineEdit_servo15")
        self.lineEdit_servo15.setEnabled(True)
        self.lineEdit_servo15.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo15.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo15.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo15.setAlignment(Qt.AlignCenter)
        self.Slider_Servo15 = QSlider(self.frame_21)
        self.Slider_Servo15.setObjectName(u"Slider_Servo15")
        self.Slider_Servo15.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo15.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo15.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo15.setOrientation(Qt.Horizontal)
        self.Slider_Servo15.setInvertedAppearance(False)
        self.Slider_Servo15.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo15.setTickInterval(1)

        self.horizontalLayout_4.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.layoutWidget)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setEnabled(True)
        self.frame_22.setLayoutDirection(Qt.RightToLeft)
        self.frame_22.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.label_id16 = QLabel(self.frame_22)
        self.label_id16.setObjectName(u"label_id16")
        self.label_id16.setGeometry(QRect(1, 2, 139, 10))
        self.label_id16.setMinimumSize(QSize(0, 10))
        self.label_id16.setMaximumSize(QSize(16777215, 10))
        self.label_id16.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id16.setAlignment(Qt.AlignCenter)
        self.Slider_Servo16 = QSlider(self.frame_22)
        self.Slider_Servo16.setObjectName(u"Slider_Servo16")
        self.Slider_Servo16.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo16.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo16.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo16.setOrientation(Qt.Horizontal)
        self.Slider_Servo16.setInvertedAppearance(False)
        self.Slider_Servo16.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo16.setTickInterval(1)
        self.lineEdit_servo16 = QLineEdit(self.frame_22)
        self.lineEdit_servo16.setObjectName(u"lineEdit_servo16")
        self.lineEdit_servo16.setEnabled(True)
        self.lineEdit_servo16.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo16.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo16.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.layoutWidget)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setEnabled(True)
        self.frame_23.setLayoutDirection(Qt.RightToLeft)
        self.frame_23.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.lineEdit_servo17 = QLineEdit(self.frame_23)
        self.lineEdit_servo17.setObjectName(u"lineEdit_servo17")
        self.lineEdit_servo17.setEnabled(True)
        self.lineEdit_servo17.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo17.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo17.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo17.setAlignment(Qt.AlignCenter)
        self.label_id17 = QLabel(self.frame_23)
        self.label_id17.setObjectName(u"label_id17")
        self.label_id17.setGeometry(QRect(1, 2, 139, 10))
        self.label_id17.setMinimumSize(QSize(0, 10))
        self.label_id17.setMaximumSize(QSize(16777215, 10))
        self.label_id17.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id17.setAlignment(Qt.AlignCenter)
        self.Slider_Servo17 = QSlider(self.frame_23)
        self.Slider_Servo17.setObjectName(u"Slider_Servo17")
        self.Slider_Servo17.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo17.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo17.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo17.setOrientation(Qt.Horizontal)
        self.Slider_Servo17.setInvertedAppearance(False)
        self.Slider_Servo17.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo17.setTickInterval(1)

        self.horizontalLayout_4.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.layoutWidget)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setEnabled(True)
        self.frame_24.setLayoutDirection(Qt.RightToLeft)
        self.frame_24.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.Slider_Servo18 = QSlider(self.frame_24)
        self.Slider_Servo18.setObjectName(u"Slider_Servo18")
        self.Slider_Servo18.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo18.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo18.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo18.setOrientation(Qt.Horizontal)
        self.Slider_Servo18.setInvertedAppearance(False)
        self.Slider_Servo18.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo18.setTickInterval(1)
        self.label_id18 = QLabel(self.frame_24)
        self.label_id18.setObjectName(u"label_id18")
        self.label_id18.setGeometry(QRect(1, 2, 139, 10))
        self.label_id18.setMinimumSize(QSize(0, 10))
        self.label_id18.setMaximumSize(QSize(16777215, 10))
        self.label_id18.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id18.setAlignment(Qt.AlignCenter)
        self.lineEdit_servo18 = QLineEdit(self.frame_24)
        self.lineEdit_servo18.setObjectName(u"lineEdit_servo18")
        self.lineEdit_servo18.setEnabled(True)
        self.lineEdit_servo18.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo18.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo18.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.frame_24)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_13 = QFrame(self.layoutWidget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setEnabled(True)
        self.frame_13.setLayoutDirection(Qt.RightToLeft)
        self.frame_13.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.lineEdit_servo19 = QLineEdit(self.frame_13)
        self.lineEdit_servo19.setObjectName(u"lineEdit_servo19")
        self.lineEdit_servo19.setEnabled(True)
        self.lineEdit_servo19.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo19.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo19.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo19.setAlignment(Qt.AlignCenter)
        self.Slider_Servo19 = QSlider(self.frame_13)
        self.Slider_Servo19.setObjectName(u"Slider_Servo19")
        self.Slider_Servo19.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo19.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo19.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo19.setOrientation(Qt.Horizontal)
        self.Slider_Servo19.setInvertedAppearance(False)
        self.Slider_Servo19.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo19.setTickInterval(1)
        self.label_id19 = QLabel(self.frame_13)
        self.label_id19.setObjectName(u"label_id19")
        self.label_id19.setGeometry(QRect(1, 2, 139, 10))
        self.label_id19.setMinimumSize(QSize(0, 10))
        self.label_id19.setMaximumSize(QSize(16777215, 10))
        self.label_id19.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.layoutWidget)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setEnabled(True)
        self.frame_14.setLayoutDirection(Qt.RightToLeft)
        self.frame_14.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.Slider_Servo20 = QSlider(self.frame_14)
        self.Slider_Servo20.setObjectName(u"Slider_Servo20")
        self.Slider_Servo20.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo20.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo20.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo20.setOrientation(Qt.Horizontal)
        self.Slider_Servo20.setInvertedAppearance(False)
        self.Slider_Servo20.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo20.setTickInterval(1)
        self.label_id20 = QLabel(self.frame_14)
        self.label_id20.setObjectName(u"label_id20")
        self.label_id20.setGeometry(QRect(1, 2, 139, 10))
        self.label_id20.setMinimumSize(QSize(0, 10))
        self.label_id20.setMaximumSize(QSize(16777215, 10))
        self.label_id20.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id20.setAlignment(Qt.AlignCenter)
        self.lineEdit_servo20 = QLineEdit(self.frame_14)
        self.lineEdit_servo20.setObjectName(u"lineEdit_servo20")
        self.lineEdit_servo20.setEnabled(True)
        self.lineEdit_servo20.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo20.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo20.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.layoutWidget)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setEnabled(True)
        self.frame_15.setLayoutDirection(Qt.RightToLeft)
        self.frame_15.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.label_id21 = QLabel(self.frame_15)
        self.label_id21.setObjectName(u"label_id21")
        self.label_id21.setGeometry(QRect(1, 2, 139, 10))
        self.label_id21.setMinimumSize(QSize(0, 10))
        self.label_id21.setMaximumSize(QSize(16777215, 10))
        self.label_id21.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id21.setAlignment(Qt.AlignCenter)
        self.lineEdit_servo21 = QLineEdit(self.frame_15)
        self.lineEdit_servo21.setObjectName(u"lineEdit_servo21")
        self.lineEdit_servo21.setEnabled(True)
        self.lineEdit_servo21.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo21.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo21.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo21.setAlignment(Qt.AlignCenter)
        self.Slider_Servo21 = QSlider(self.frame_15)
        self.Slider_Servo21.setObjectName(u"Slider_Servo21")
        self.Slider_Servo21.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo21.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo21.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo21.setOrientation(Qt.Horizontal)
        self.Slider_Servo21.setInvertedAppearance(False)
        self.Slider_Servo21.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo21.setTickInterval(1)

        self.horizontalLayout_3.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.layoutWidget)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setEnabled(True)
        self.frame_16.setLayoutDirection(Qt.RightToLeft)
        self.frame_16.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.Slider_Servo22 = QSlider(self.frame_16)
        self.Slider_Servo22.setObjectName(u"Slider_Servo22")
        self.Slider_Servo22.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo22.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo22.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo22.setOrientation(Qt.Horizontal)
        self.Slider_Servo22.setInvertedAppearance(False)
        self.Slider_Servo22.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo22.setTickInterval(1)
        self.label_id22 = QLabel(self.frame_16)
        self.label_id22.setObjectName(u"label_id22")
        self.label_id22.setGeometry(QRect(1, 2, 139, 10))
        self.label_id22.setMinimumSize(QSize(0, 10))
        self.label_id22.setMaximumSize(QSize(16777215, 10))
        self.label_id22.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id22.setAlignment(Qt.AlignCenter)
        self.lineEdit_servo22 = QLineEdit(self.frame_16)
        self.lineEdit_servo22.setObjectName(u"lineEdit_servo22")
        self.lineEdit_servo22.setEnabled(True)
        self.lineEdit_servo22.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo22.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo22.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.layoutWidget)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setEnabled(True)
        self.frame_17.setLayoutDirection(Qt.RightToLeft)
        self.frame_17.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.lineEdit_servo23 = QLineEdit(self.frame_17)
        self.lineEdit_servo23.setObjectName(u"lineEdit_servo23")
        self.lineEdit_servo23.setEnabled(True)
        self.lineEdit_servo23.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo23.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo23.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo23.setAlignment(Qt.AlignCenter)
        self.Slider_Servo23 = QSlider(self.frame_17)
        self.Slider_Servo23.setObjectName(u"Slider_Servo23")
        self.Slider_Servo23.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo23.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo23.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo23.setOrientation(Qt.Horizontal)
        self.Slider_Servo23.setInvertedAppearance(False)
        self.Slider_Servo23.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo23.setTickInterval(1)
        self.label_id23 = QLabel(self.frame_17)
        self.label_id23.setObjectName(u"label_id23")
        self.label_id23.setGeometry(QRect(1, 2, 139, 10))
        self.label_id23.setMinimumSize(QSize(0, 10))
        self.label_id23.setMaximumSize(QSize(16777215, 10))
        self.label_id23.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.layoutWidget)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setEnabled(True)
        self.frame_18.setLayoutDirection(Qt.RightToLeft)
        self.frame_18.setStyleSheet(u"* {\n"
"  background: white; /* \u80cc\u666f\u6539\u4e3a\u767d\u8272 */\n"
"  border: 2px solid #59969b; /* \u4f7f\u7528\u4e0e\u6ed1\u5757\u4e00\u81f4\u7684\u989c\u8272 */\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.lineEdit_servo24 = QLineEdit(self.frame_18)
        self.lineEdit_servo24.setObjectName(u"lineEdit_servo24")
        self.lineEdit_servo24.setEnabled(True)
        self.lineEdit_servo24.setGeometry(QRect(17, 36, 106, 31))
        self.lineEdit_servo24.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_servo24.setLayoutDirection(Qt.LeftToRight)
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
        self.lineEdit_servo24.setAlignment(Qt.AlignCenter)
        self.Slider_Servo24 = QSlider(self.frame_18)
        self.Slider_Servo24.setObjectName(u"Slider_Servo24")
        self.Slider_Servo24.setGeometry(QRect(1, 19, 139, 10))
        self.Slider_Servo24.setMaximumSize(QSize(16777215, 10))
        self.Slider_Servo24.setLayoutDirection(Qt.LeftToRight)
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
        self.Slider_Servo24.setOrientation(Qt.Horizontal)
        self.Slider_Servo24.setInvertedAppearance(False)
        self.Slider_Servo24.setTickPosition(QSlider.NoTicks)
        self.Slider_Servo24.setTickInterval(1)
        self.label_id24 = QLabel(self.frame_18)
        self.label_id24.setObjectName(u"label_id24")
        self.label_id24.setGeometry(QRect(1, 2, 139, 10))
        self.label_id24.setMinimumSize(QSize(0, 10))
        self.label_id24.setMaximumSize(QSize(16777215, 10))
        self.label_id24.setStyleSheet(u"QLabel{border: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}\n"
"QLabel{background: none; /* \u53bb\u6389\u63a7\u4ef6\u7684\u8fb9\u6846 */}")
        self.label_id24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.frame_18)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.pushButton_create = QPushButton(Form)
        self.pushButton_create.setObjectName(u"pushButton_create")
        self.pushButton_create.setGeometry(QRect(330, 370, 185, 40))
        font = QFont()
        font.setPointSize(21)
        font.setBold(True)
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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u521b\u5efa\u673a\u5668\u4eba\u914d\u7f6e", None))
        self.lineEdit_servo1.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id1.setText(QCoreApplication.translate("Form", u"ID:1", None))
        self.label_id2.setText(QCoreApplication.translate("Form", u"ID:2", None))
        self.lineEdit_servo2.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_servo3.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id3.setText(QCoreApplication.translate("Form", u"ID:3", None))
        self.label_id4.setText(QCoreApplication.translate("Form", u"ID:4", None))
        self.lineEdit_servo4.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id5.setText(QCoreApplication.translate("Form", u"ID:5", None))
        self.lineEdit_servo5.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id6.setText(QCoreApplication.translate("Form", u"ID:6", None))
        self.lineEdit_servo6.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id7.setText(QCoreApplication.translate("Form", u"ID:7", None))
        self.lineEdit_servo7.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_servo8.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id8.setText(QCoreApplication.translate("Form", u"ID:8", None))
        self.lineEdit_servo9.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id9.setText(QCoreApplication.translate("Form", u"ID:9", None))
        self.lineEdit_servo10.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id10.setText(QCoreApplication.translate("Form", u"ID:10", None))
        self.label_id11.setText(QCoreApplication.translate("Form", u"ID:11", None))
        self.lineEdit_servo11.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id12.setText(QCoreApplication.translate("Form", u"ID:12", None))
        self.lineEdit_servo12.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id13.setText(QCoreApplication.translate("Form", u"ID:13", None))
        self.lineEdit_servo13.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_servo14.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id14.setText(QCoreApplication.translate("Form", u"ID:14", None))
        self.label_id15.setText(QCoreApplication.translate("Form", u"ID:15", None))
        self.lineEdit_servo15.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id16.setText(QCoreApplication.translate("Form", u"ID:16", None))
        self.lineEdit_servo16.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_servo17.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id17.setText(QCoreApplication.translate("Form", u"ID:17", None))
        self.label_id18.setText(QCoreApplication.translate("Form", u"ID:18", None))
        self.lineEdit_servo18.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_servo19.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id19.setText(QCoreApplication.translate("Form", u"ID:19", None))
        self.label_id20.setText(QCoreApplication.translate("Form", u"ID:20", None))
        self.lineEdit_servo20.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id21.setText(QCoreApplication.translate("Form", u"ID:21", None))
        self.lineEdit_servo21.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id22.setText(QCoreApplication.translate("Form", u"ID:22", None))
        self.lineEdit_servo22.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.lineEdit_servo23.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id23.setText(QCoreApplication.translate("Form", u"ID:23", None))
        self.lineEdit_servo24.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u8f93\u5165\u8235\u673a\u89d2\u5ea6", None))
        self.label_id24.setText(QCoreApplication.translate("Form", u"ID:24", None))
        self.pushButton_create.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u521b\u5efa", None))
    # retranslateUi

