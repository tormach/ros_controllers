# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'double_editor.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QHBoxLayout,
    QSizePolicy, QSlider, QWidget)

class Ui_double_editor(object):
    def setupUi(self, double_editor):
        if not double_editor.objectName():
            double_editor.setObjectName(u"double_editor")
        double_editor.setEnabled(True)
        double_editor.resize(249, 121)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(double_editor.sizePolicy().hasHeightForWidth())
        double_editor.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(double_editor)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.slider = QSlider(double_editor)
        self.slider.setObjectName(u"slider")
        self.slider.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slider.sizePolicy().hasHeightForWidth())
        self.slider.setSizePolicy(sizePolicy1)
        self.slider.setBaseSize(QSize(0, 0))
        self.slider.setMaximum(100)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setInvertedAppearance(False)
        self.slider.setInvertedControls(False)

        self.horizontalLayout.addWidget(self.slider)

        self.spin_box = QDoubleSpinBox(double_editor)
        self.spin_box.setObjectName(u"spin_box")
        self.spin_box.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spin_box.sizePolicy().hasHeightForWidth())
        self.spin_box.setSizePolicy(sizePolicy2)
        self.spin_box.setMinimumSize(QSize(60, 0))
        self.spin_box.setBaseSize(QSize(100, 0))
        self.spin_box.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spin_box.setKeyboardTracking(False)

        self.horizontalLayout.addWidget(self.spin_box)

        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(double_editor)

        QMetaObject.connectSlotsByName(double_editor)
    # setupUi

    def retranslateUi(self, double_editor):
        double_editor.setWindowTitle(QCoreApplication.translate("double_editor", u"Form", None))
    # retranslateUi

