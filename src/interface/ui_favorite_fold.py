# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_favorite_fold.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_FavoriteFold(object):
    def setupUi(self, FavoriteFold):
        if not FavoriteFold.objectName():
            FavoriteFold.setObjectName(u"FavoriteFold")
        FavoriteFold.resize(400, 300)
        self.verticalLayout = QVBoxLayout(FavoriteFold)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(FavoriteFold)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editButton = QPushButton(FavoriteFold)
        self.editButton.setObjectName(u"editButton")

        self.horizontalLayout.addWidget(self.editButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listWidget = QListWidget(FavoriteFold)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.saveButton = QPushButton(FavoriteFold)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_2.addWidget(self.saveButton)

        self.closeButton = QPushButton(FavoriteFold)
        self.closeButton.setObjectName(u"closeButton")

        self.horizontalLayout_2.addWidget(self.closeButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(FavoriteFold)

        QMetaObject.connectSlotsByName(FavoriteFold)
    # setupUi

    def retranslateUi(self, FavoriteFold):
        FavoriteFold.setWindowTitle(QCoreApplication.translate("FavoriteFold", u"Form", None))
        self.label.setText(QCoreApplication.translate("FavoriteFold", u"\u5206\u7c7b", None))
        self.editButton.setText(QCoreApplication.translate("FavoriteFold", u"\u7f16\u8f91", None))
        self.saveButton.setText(QCoreApplication.translate("FavoriteFold", u"\u4fdd\u5b58", None))
        self.closeButton.setText(QCoreApplication.translate("FavoriteFold", u"\u53d6\u6d88", None))
    # retranslateUi

