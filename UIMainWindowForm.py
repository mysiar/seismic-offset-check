# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/UIMainWindowForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowForm(object):
    def setupUi(self, MainWindowForm):
        MainWindowForm.setObjectName("MainWindowForm")
        MainWindowForm.resize(790, 464)
        MainWindowForm.setMinimumSize(QtCore.QSize(790, 464))
        MainWindowForm.setMaximumSize(QtCore.QSize(790, 464))
        self.centralwidget = QtWidgets.QWidget(MainWindowForm)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 771, 61))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 771, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblDb = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblDb.setWordWrap(True)
        self.lblDb.setObjectName("lblDb")
        self.verticalLayout.addWidget(self.lblDb)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 80, 771, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 20, 771, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblSPS = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.lblSPS.setWordWrap(True)
        self.lblSPS.setObjectName("lblSPS")
        self.verticalLayout_3.addWidget(self.lblSPS)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 160, 771, 211))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 771, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtOutput = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.txtOutput.setObjectName("txtOutput")
        self.horizontalLayout.addWidget(self.txtOutput)
        MainWindowForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindowForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowForm)
        self.statusbar.setObjectName("statusbar")
        MainWindowForm.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindowForm)
        self.toolBar.setObjectName("toolBar")
        MainWindowForm.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen_DB_File = QtWidgets.QAction(MainWindowForm)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/offset_check/icons/tree-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_DB_File.setIcon(icon)
        self.actionOpen_DB_File.setObjectName("actionOpen_DB_File")
        self.actionOpen_SPS_File = QtWidgets.QAction(MainWindowForm)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/offset_check/icons/folder-open-document-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_SPS_File.setIcon(icon1)
        self.actionOpen_SPS_File.setObjectName("actionOpen_SPS_File")
        self.actionQuit = QtWidgets.QAction(MainWindowForm)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/offset_check/icons/cross-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName("actionQuit")
        self.actionProcess = QtWidgets.QAction(MainWindowForm)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/offset_check/icons/burn-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProcess.setIcon(icon3)
        self.actionProcess.setObjectName("actionProcess")
        self.actionHelp = QtWidgets.QAction(MainWindowForm)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/offset_check/icons/question-button-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon4)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindowForm)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/offset_check/icons/information-button-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon5)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen_DB_File)
        self.menuFile.addAction(self.actionOpen_SPS_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuRun.addAction(self.actionProcess)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionOpen_DB_File)
        self.toolBar.addAction(self.actionOpen_SPS_File)
        self.toolBar.addAction(self.actionProcess)
        self.toolBar.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionQuit)

        self.retranslateUi(MainWindowForm)
        self.actionQuit.triggered.connect(MainWindowForm.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindowForm)

    def retranslateUi(self, MainWindowForm):
        _translate = QtCore.QCoreApplication.translate
        MainWindowForm.setWindowTitle(_translate("MainWindowForm", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindowForm", "SQLite DB"))
        self.lblDb.setText(_translate("MainWindowForm", "label to display DB file"))
        self.groupBox_2.setTitle(_translate("MainWindowForm", "SPS"))
        self.lblSPS.setText(_translate("MainWindowForm", "label to display SPS file"))
        self.groupBox_3.setTitle(_translate("MainWindowForm", "Output"))
        self.menuFile.setTitle(_translate("MainWindowForm", "File"))
        self.menuRun.setTitle(_translate("MainWindowForm", "Process"))
        self.menuHelp.setTitle(_translate("MainWindowForm", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindowForm", "toolBar"))
        self.actionOpen_DB_File.setText(_translate("MainWindowForm", "Open DB File"))
        self.actionOpen_DB_File.setToolTip(_translate("MainWindowForm", "Open SQLite DB File"))
        self.actionOpen_SPS_File.setText(_translate("MainWindowForm", "Open SPS File"))
        self.actionQuit.setText(_translate("MainWindowForm", "Quit"))
        self.actionProcess.setText(_translate("MainWindowForm", "Process"))
        self.actionHelp.setText(_translate("MainWindowForm", "Help"))
        self.actionHelp.setToolTip(_translate("MainWindowForm", "Help"))
        self.actionAbout.setText(_translate("MainWindowForm", "About"))
import resources_rc
