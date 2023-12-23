# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res_main_window_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 569)
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(41,61,132, 235), stop:1 rgba(155,79, 165, 255));\n"
"font-family: Noto Sans SC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.balanca_and_categories = QFrame(self.centralwidget)
        self.balanca_and_categories.setObjectName(u"balanca_and_categories")
        self.balanca_and_categories.setStyleSheet(u"")
        self.balance_frame = QHBoxLayout(self.balanca_and_categories)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame_2 = QFrame(self.balanca_and_categories)
        self.balance_frame_2.setObjectName(u"balance_frame_2")
        self.balance_frame_2.setStyleSheet(u"background-color: rgba(255,255,255,40);\n"
"border: 1px solid rgba(255,255,255,30);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.balance_frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.lbl_current_balance = QLabel(self.balance_frame_2)
        self.lbl_current_balance.setObjectName(u"lbl_current_balance")
        self.lbl_current_balance.setStyleSheet(u"color: white;\n"
"font-weight:bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: nine;")

        self.verticalLayout.addWidget(self.lbl_current_balance)

        self.lbl_balance = QLabel(self.balance_frame_2)
        self.lbl_balance.setObjectName(u"lbl_balance")
        self.lbl_balance.setStyleSheet(u"color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: nine;")

        self.verticalLayout.addWidget(self.lbl_balance)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_up_arrow = QLabel(self.balance_frame_2)
        self.icon_up_arrow.setObjectName(u"icon_up_arrow")
        self.icon_up_arrow.setMaximumSize(QSize(50, 16777215))
        self.icon_up_arrow.setCursor(QCursor(Qt.PointingHandCursor))
        self.icon_up_arrow.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding: 10px")
        self.icon_up_arrow.setPixmap(QPixmap(u":/icon/icons/up-arrow.svg"))

        self.horizontalLayout.addWidget(self.icon_up_arrow)

        self.lbl_income = QLabel(self.balance_frame_2)
        self.lbl_income.setObjectName(u"lbl_income")
        self.lbl_income.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding: 10px")

        self.horizontalLayout.addWidget(self.lbl_income)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lbl_income_balance = QLabel(self.balance_frame_2)
        self.lbl_income_balance.setObjectName(u"lbl_income_balance")
        self.lbl_income_balance.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lbl_income_balance)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.icon_down_arrow = QLabel(self.balance_frame_2)
        self.icon_down_arrow.setObjectName(u"icon_down_arrow")
        self.icon_down_arrow.setMaximumSize(QSize(50, 16777215))
        self.icon_down_arrow.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding: 10px")
        self.icon_down_arrow.setPixmap(QPixmap(u":/icon/icons/down-arrow.svg"))

        self.horizontalLayout_2.addWidget(self.icon_down_arrow)

        self.lbl_outcome = QLabel(self.balance_frame_2)
        self.lbl_outcome.setObjectName(u"lbl_outcome")
        self.lbl_outcome.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding: 10px")

        self.horizontalLayout_2.addWidget(self.lbl_outcome)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lbl_outcome_balance = QLabel(self.balance_frame_2)
        self.lbl_outcome_balance.setObjectName(u"lbl_outcome_balance")
        self.lbl_outcome_balance.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lbl_outcome_balance)


        self.balance_frame.addWidget(self.balance_frame_2)

        self.categories_frame_2 = QFrame(self.balanca_and_categories)
        self.categories_frame_2.setObjectName(u"categories_frame_2")
        self.categories_frame_2.setStyleSheet(u"background-color: rgba(255,255,255,40);\n"
"border: 1px solid rgba(255,255,255,30);\n"
"border-radius: 7px;")
        self.categories_frame = QVBoxLayout(self.categories_frame_2)
        self.categories_frame.setSpacing(0)
        self.categories_frame.setObjectName(u"categories_frame")
        self.categories_frame.setContentsMargins(16, 16, 16, 16)
        self.label_9 = QLabel(self.categories_frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: white;\n"
"font-weight:bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: nine;")

        self.categories_frame.addWidget(self.label_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.icon_grocery = QLabel(self.categories_frame_2)
        self.icon_grocery.setObjectName(u"icon_grocery")
        self.icon_grocery.setMaximumSize(QSize(50, 16777215))
        self.icon_grocery.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_grocery.setPixmap(QPixmap(u":/icon/icons/grocery.svg"))
        self.icon_grocery.setMargin(10)

        self.horizontalLayout_4.addWidget(self.icon_grocery)

        self.lbl_grocery = QLabel(self.categories_frame_2)
        self.lbl_grocery.setObjectName(u"lbl_grocery")
        self.lbl_grocery.setMaximumSize(QSize(250, 16777215))
        self.lbl_grocery.setStyleSheet(u"color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding: 10px")

        self.horizontalLayout_4.addWidget(self.lbl_grocery)

        self.balance_grocery = QLabel(self.categories_frame_2)
        self.balance_grocery.setObjectName(u"balance_grocery")
        self.balance_grocery.setMaximumSize(QSize(100, 16777215))
        self.balance_grocery.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_4.addWidget(self.balance_grocery)


        self.categories_frame.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.icon_entertainment = QLabel(self.categories_frame_2)
        self.icon_entertainment.setObjectName(u"icon_entertainment")
        self.icon_entertainment.setMaximumSize(QSize(50, 16777215))
        self.icon_entertainment.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_entertainment.setPixmap(QPixmap(u":/icon/icons/entertainment.svg"))
        self.icon_entertainment.setMargin(10)

        self.horizontalLayout_5.addWidget(self.icon_entertainment)

        self.lbl_entertainment = QLabel(self.categories_frame_2)
        self.lbl_entertainment.setObjectName(u"lbl_entertainment")
        self.lbl_entertainment.setStyleSheet(u"color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding: 10px")

        self.horizontalLayout_5.addWidget(self.lbl_entertainment)

        self.balance_entertainment = QLabel(self.categories_frame_2)
        self.balance_entertainment.setObjectName(u"balance_entertainment")
        self.balance_entertainment.setMaximumSize(QSize(100, 16777215))
        self.balance_entertainment.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_5.addWidget(self.balance_entertainment)


        self.categories_frame.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.icon_auto = QLabel(self.categories_frame_2)
        self.icon_auto.setObjectName(u"icon_auto")
        self.icon_auto.setMaximumSize(QSize(50, 16777215))
        self.icon_auto.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_auto.setPixmap(QPixmap(u":/icon/icons/auto.svg"))
        self.icon_auto.setMargin(10)

        self.horizontalLayout_6.addWidget(self.icon_auto)

        self.lbl_auto = QLabel(self.categories_frame_2)
        self.lbl_auto.setObjectName(u"lbl_auto")
        self.lbl_auto.setStyleSheet(u"color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding: 10px")

        self.horizontalLayout_6.addWidget(self.lbl_auto)

        self.balance_auto = QLabel(self.categories_frame_2)
        self.balance_auto.setObjectName(u"balance_auto")
        self.balance_auto.setMaximumSize(QSize(100, 16777215))
        self.balance_auto.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_6.addWidget(self.balance_auto)


        self.categories_frame.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.icon_other = QLabel(self.categories_frame_2)
        self.icon_other.setObjectName(u"icon_other")
        self.icon_other.setMaximumSize(QSize(50, 16777215))
        self.icon_other.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_other.setPixmap(QPixmap(u":/icon/icons/other.svg"))
        self.icon_other.setMargin(10)

        self.horizontalLayout_3.addWidget(self.icon_other)

        self.lbl_other = QLabel(self.categories_frame_2)
        self.lbl_other.setObjectName(u"lbl_other")
        self.lbl_other.setStyleSheet(u"color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding: 10px")

        self.horizontalLayout_3.addWidget(self.lbl_other)

        self.balance_other = QLabel(self.categories_frame_2)
        self.balance_other.setObjectName(u"balance_other")
        self.balance_other.setMaximumSize(QSize(100, 16777215))
        self.balance_other.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_3.addWidget(self.balance_other)


        self.categories_frame.addLayout(self.horizontalLayout_3)


        self.balance_frame.addWidget(self.categories_frame_2)


        self.verticalLayout_3.addWidget(self.balanca_and_categories)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_new_transaction = QPushButton(self.centralwidget)
        self.btn_new_transaction.setObjectName(u"btn_new_transaction")
        self.btn_new_transaction.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"font-size: 16pt;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width:230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/income.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_transaction.setIcon(icon)
        self.btn_new_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_new_transaction)

        self.btn_edit_transaction = QPushButton(self.centralwidget)
        self.btn_edit_transaction.setObjectName(u"btn_edit_transaction")
        self.btn_edit_transaction.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"font-size: 16pt;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width:230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit_transaction.setIcon(icon1)
        self.btn_edit_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_edit_transaction)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"font-size: 16pt;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width:230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.pushButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView{\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QTableView:section{\n"
"color: white;\n"
"background-color: rgb(53,53,53);\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"\n"
"QTableView:item{\n"
"border-style: none;\n"
"border-bottom: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QTableView:item:selected{\n"
"border: none;\n"
"color: rgba(255,255,255);\n"
"background-color: rgb(255,255,255,50);\n"
"}")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Expence tracker", None))
        self.lbl_current_balance.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0431\u0430\u043b\u0430\u043d\u0441", None))
        self.lbl_balance.setText(QCoreApplication.translate("MainWindow", u"51200", None))
        self.icon_up_arrow.setText("")
        self.lbl_income.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0445\u043e\u0434", None))
        self.lbl_income_balance.setText(QCoreApplication.translate("MainWindow", u"51200", None))
        self.icon_down_arrow.setText("")
        self.lbl_outcome.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434", None))
        self.lbl_outcome_balance.setText(QCoreApplication.translate("MainWindow", u"51200", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0437\u0430\u0442\u0440\u0430\u0442", None))
        self.icon_grocery.setText("")
        self.lbl_grocery.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b", None))
        self.balance_grocery.setText(QCoreApplication.translate("MainWindow", u"$15000", None))
        self.icon_entertainment.setText("")
        self.lbl_entertainment.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u044f", None))
        self.balance_entertainment.setText(QCoreApplication.translate("MainWindow", u"$15000", None))
        self.icon_auto.setText("")
        self.lbl_auto.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e", None))
        self.balance_auto.setText(QCoreApplication.translate("MainWindow", u"$15000", None))
        self.icon_other.setText("")
        self.lbl_other.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0447\u0435\u0435", None))
        self.balance_other.setText(QCoreApplication.translate("MainWindow", u"$15000", None))
        self.btn_new_transaction.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.btn_edit_transaction.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

