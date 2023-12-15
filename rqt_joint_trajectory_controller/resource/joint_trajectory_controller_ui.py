# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'joint_trajectory_controller.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_joint_trajectory_controller(object):
    def setupUi(self, joint_trajectory_controller):
        if not joint_trajectory_controller.objectName():
            joint_trajectory_controller.setObjectName(u"joint_trajectory_controller")
        joint_trajectory_controller.resize(336, 317)
        self.verticalLayout_2 = QVBoxLayout(joint_trajectory_controller)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.controller_group = QGroupBox(joint_trajectory_controller)
        self.controller_group.setObjectName(u"controller_group")
        self.verticalLayout = QVBoxLayout(self.controller_group)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.jtc_combo = QComboBox(self.controller_group)
        self.jtc_combo.setObjectName(u"jtc_combo")

        self.gridLayout.addWidget(self.jtc_combo, 1, 1, 1, 1)

        self.cm_combo = QComboBox(self.controller_group)
        self.cm_combo.setObjectName(u"cm_combo")

        self.gridLayout.addWidget(self.cm_combo, 1, 0, 1, 1)

        self.cm_list_label = QLabel(self.controller_group)
        self.cm_list_label.setObjectName(u"cm_list_label")

        self.gridLayout.addWidget(self.cm_list_label, 0, 0, 1, 1)

        self.controller_list_label = QLabel(self.controller_group)
        self.controller_list_label.setObjectName(u"controller_list_label")

        self.gridLayout.addWidget(self.controller_list_label, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.enable_button = QPushButton(self.controller_group)
        self.enable_button.setObjectName(u"enable_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enable_button.sizePolicy().hasHeightForWidth())
        self.enable_button.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"off.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"on.svg", QSize(), QIcon.Normal, QIcon.On)
        icon.addFile(u"on.svg", QSize(), QIcon.Active, QIcon.On)
        self.enable_button.setIcon(icon)
        self.enable_button.setIconSize(QSize(48, 48))
        self.enable_button.setCheckable(True)

        self.horizontalLayout.addWidget(self.enable_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.controller_group)

        self.joint_group_outer = QGroupBox(joint_trajectory_controller)
        self.joint_group_outer.setObjectName(u"joint_group_outer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.joint_group_outer.sizePolicy().hasHeightForWidth())
        self.joint_group_outer.setSizePolicy(sizePolicy1)
        self.joint_group_outer.setMinimumSize(QSize(0, 0))
        self.joint_group_outer.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.joint_group_outer.setFlat(False)
        self.joint_group_outer.setCheckable(False)
        self.verticalLayout_3 = QVBoxLayout(self.joint_group_outer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.joint_group_scroll = QScrollArea(self.joint_group_outer)
        self.joint_group_scroll.setObjectName(u"joint_group_scroll")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.joint_group_scroll.sizePolicy().hasHeightForWidth())
        self.joint_group_scroll.setSizePolicy(sizePolicy2)
        self.joint_group_scroll.setFrameShape(QFrame.NoFrame)
        self.joint_group_scroll.setFrameShadow(QFrame.Plain)
        self.joint_group_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.joint_group_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.joint_group_scroll.setWidgetResizable(True)
        self.joint_group = QWidget()
        self.joint_group.setObjectName(u"joint_group")
        self.joint_group.setGeometry(QRect(0, 0, 314, 109))
        self.joint_group_scroll.setWidget(self.joint_group)

        self.verticalLayout_3.addWidget(self.joint_group_scroll)


        self.verticalLayout_2.addWidget(self.joint_group_outer)

        self.speed_scaling_group = QGroupBox(joint_trajectory_controller)
        self.speed_scaling_group.setObjectName(u"speed_scaling_group")
        self.speed_scaling_layout = QVBoxLayout(self.speed_scaling_group)
        self.speed_scaling_layout.setObjectName(u"speed_scaling_layout")

        self.verticalLayout_2.addWidget(self.speed_scaling_group)

#if QT_CONFIG(shortcut)
        self.cm_list_label.setBuddy(self.cm_combo)
        self.controller_list_label.setBuddy(self.jtc_combo)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.cm_combo, self.jtc_combo)
        QWidget.setTabOrder(self.jtc_combo, self.enable_button)

        self.retranslateUi(joint_trajectory_controller)

        QMetaObject.connectSlotsByName(joint_trajectory_controller)
    # setupUi

    def retranslateUi(self, joint_trajectory_controller):
        joint_trajectory_controller.setWindowTitle(QCoreApplication.translate("joint_trajectory_controller", u"Joint trajectory controller", None))
        self.controller_group.setTitle("")
#if QT_CONFIG(tooltip)
        self.cm_list_label.setToolTip(QCoreApplication.translate("joint_trajectory_controller", u"<html><head/><body><p><span style=\" font-weight:600;\">controller manager</span> namespace. It is assumed that the <span style=\" font-weight:600;\">robot_description</span> parameter also lives in the same namesapce.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cm_list_label.setText(QCoreApplication.translate("joint_trajectory_controller", u"controller manager ns", None))
        self.controller_list_label.setText(QCoreApplication.translate("joint_trajectory_controller", u"controller", None))
#if QT_CONFIG(tooltip)
        self.enable_button.setToolTip(QCoreApplication.translate("joint_trajectory_controller", u"<html><head/><body><p>Enable/disable sending commands to the controller.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.enable_button.setText("")
        self.joint_group_outer.setTitle(QCoreApplication.translate("joint_trajectory_controller", u"joints", None))
        self.speed_scaling_group.setTitle(QCoreApplication.translate("joint_trajectory_controller", u"speed scaling", None))
    # retranslateUi

