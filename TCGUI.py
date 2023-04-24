# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TCG.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1132, 924)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CardsList = QtWidgets.QTabWidget(self.centralwidget)
        self.CardsList.setGeometry(QtCore.QRect(0, 170, 312, 497))
        self.CardsList.setObjectName("CardsList")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.BotCardList = QtWidgets.QListWidget(self.tab)
        self.BotCardList.setGeometry(QtCore.QRect(0, 0, 306, 471))
        self.BotCardList.setObjectName("BotCardList")
        self.CardsList.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.BattleCardList = QtWidgets.QListWidget(self.tab_3)
        self.BattleCardList.setGeometry(QtCore.QRect(0, 0, 306, 471))
        self.BattleCardList.setObjectName("BattleCardList")
        self.verticalScrollBar_3 = QtWidgets.QScrollBar(self.tab_3)
        self.verticalScrollBar_3.setGeometry(QtCore.QRect(306, -1, 20, 471))
        self.verticalScrollBar_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_3.setObjectName("verticalScrollBar_3")
        self.CardsList.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.tab_2)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(306, -1, 20, 471))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.StrategemCardList = QtWidgets.QListWidget(self.tab_2)
        self.StrategemCardList.setGeometry(QtCore.QRect(0, 0, 306, 471))
        self.StrategemCardList.setObjectName("StrategemCardList")
        self.StrategemCardList.raise_()
        self.verticalScrollBar_2.raise_()
        self.CardsList.addTab(self.tab_2, "")
        self.AutobotCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.AutobotCheckbox.setGeometry(QtCore.QRect(840, 40, 81, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AutobotCheckbox.sizePolicy().hasHeightForWidth())
        self.AutobotCheckbox.setSizePolicy(sizePolicy)
        self.AutobotCheckbox.setObjectName("AutobotCheckbox")
        self.MercenaryCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.MercenaryCheckbox.setGeometry(QtCore.QRect(840, 70, 81, 31))
        self.MercenaryCheckbox.setObjectName("MercenaryCheckbox")
        self.DecepticonCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.DecepticonCheckbox.setGeometry(QtCore.QRect(840, 100, 81, 31))
        self.DecepticonCheckbox.setObjectName("DecepticonCheckbox")
        self.CardPreview = QtWidgets.QGraphicsView(self.centralwidget)
        self.CardPreview.setGeometry(QtCore.QRect(837, 190, 296, 471))
        self.CardPreview.setObjectName("CardPreview")
        self.SelectedBotAndStrategemCards = QtWidgets.QListWidget(self.centralwidget)
        self.SelectedBotAndStrategemCards.setGeometry(QtCore.QRect(326, 190, 241, 441))
        self.SelectedBotAndStrategemCards.setObjectName("SelectedBotAndStrategemCards")
        self.SelectedBattleCards = QtWidgets.QListWidget(self.centralwidget)
        self.SelectedBattleCards.setGeometry(QtCore.QRect(587, 190, 230, 441))
        self.SelectedBattleCards.setObjectName("SelectedBattleCards")
        self.CardTotal = QtWidgets.QListWidget(self.centralwidget)
        self.CardTotal.setGeometry(QtCore.QRect(326, 630, 241, 81))
        self.CardTotal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CardTotal.setObjectName("CardTotal")
        item = QtWidgets.QListWidgetItem()
        self.CardTotal.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.CardTotal.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.CardTotal.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.CardTotal.addItem(item)
        self.PointTotal_2 = QtWidgets.QListWidget(self.centralwidget)
        self.PointTotal_2.setGeometry(QtCore.QRect(587, 630, 230, 81))
        self.PointTotal_2.setObjectName("PointTotal_2")
        item = QtWidgets.QListWidgetItem()
        self.PointTotal_2.addItem(item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 170, 231, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 170, 231, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(840, 170, 231, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(930, 20, 31, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(930, 50, 51, 16))
        self.label_5.setObjectName("label_5")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(1020, 160, 75, 23))
        self.SearchButton.setObjectName("SearchButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(930, 80, 47, 14))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1040, 80, 47, 14))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(930, 100, 47, 14))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1040, 100, 47, 14))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(930, 130, 51, 16))
        self.label_10.setObjectName("label_10")
        self.TraitsSearch = QtWidgets.QComboBox(self.centralwidget)
        self.TraitsSearch.setGeometry(QtCore.QRect(1079, 100, 31, 16))
        self.TraitsSearch.setObjectName("TraitsSearch")
        self.SidenameSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.SidenameSearch.setGeometry(QtCore.QRect(990, 130, 141, 20))
        self.SidenameSearch.setObjectName("SidenameSearch")
        self.DefenseSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.DefenseSearch.setGeometry(QtCore.QRect(990, 100, 31, 20))
        self.DefenseSearch.setObjectName("DefenseSearch")
        self.AttackSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.AttackSearch.setGeometry(QtCore.QRect(990, 80, 31, 20))
        self.AttackSearch.setObjectName("AttackSearch")
        self.HealthSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.HealthSearch.setGeometry(QtCore.QRect(1080, 80, 31, 20))
        self.HealthSearch.setObjectName("HealthSearch")
        self.lCardNameSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.lCardNameSearch.setGeometry(QtCore.QRect(990, 20, 141, 20))
        self.lCardNameSearch.setObjectName("lCardNameSearch")
        self.CardTextSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.CardTextSearch.setGeometry(QtCore.QRect(990, 50, 141, 20))
        self.CardTextSearch.setObjectName("CardTextSearch")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1132, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.CardsList.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CardsList.setToolTip(_translate("MainWindow", "<html><head/><body><p>Battle Cards</p></body></html>"))
        self.CardsList.setTabText(self.CardsList.indexOf(self.tab), _translate("MainWindow", "Bot"))
        self.CardsList.setTabText(self.CardsList.indexOf(self.tab_3), _translate("MainWindow", "Battle"))
        self.CardsList.setTabText(self.CardsList.indexOf(self.tab_2), _translate("MainWindow", "Strategem"))
        self.AutobotCheckbox.setText(_translate("MainWindow", "AutoBots"))
        self.MercenaryCheckbox.setText(_translate("MainWindow", "Mercenaries"))
        self.DecepticonCheckbox.setText(_translate("MainWindow", "Decepticons"))
        __sortingEnabled = self.CardTotal.isSortingEnabled()
        self.CardTotal.setSortingEnabled(False)
        item = self.CardTotal.item(0)
        item.setText(_translate("MainWindow", "Bot Cards:"))
        item = self.CardTotal.item(1)
        item.setText(_translate("MainWindow", "Strategem Cards:"))
        item = self.CardTotal.item(2)
        item.setText(_translate("MainWindow", "Battle Cards:"))
        item = self.CardTotal.item(3)
        item.setText(_translate("MainWindow", "Card Total:"))
        self.CardTotal.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.PointTotal_2.isSortingEnabled()
        self.PointTotal_2.setSortingEnabled(False)
        item = self.PointTotal_2.item(0)
        item.setText(_translate("MainWindow", "PointTotal:"))
        self.PointTotal_2.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Selected Bot & Strategem Cards"))
        self.label_2.setText(_translate("MainWindow", "Selected Battle Cards"))
        self.label_3.setText(_translate("MainWindow", "Card Preview"))
        self.label_4.setText(_translate("MainWindow", "Name:"))
        self.label_5.setText(_translate("MainWindow", "Card Text:"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))
        self.label_6.setText(_translate("MainWindow", "Attack:"))
        self.label_7.setText(_translate("MainWindow", "Health:"))
        self.label_8.setText(_translate("MainWindow", "Defense:"))
        self.label_9.setText(_translate("MainWindow", "Traits:"))
        self.label_10.setText(_translate("MainWindow", "SideName:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
