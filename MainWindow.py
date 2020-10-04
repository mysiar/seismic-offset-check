import os
import time
import webbrowser
from PyQt5.QtWidgets import QDialog, QFileDialog
from UIMainWindowForm import Ui_MainWindowForm
from PyQt5.QtGui import QTextCursor
import dbupdate
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolBar,
    QAction,
    qApp,
    QFileDialog,
    QGridLayout,
    QLabel,
    QWidget,
    QStatusBar,
    QLineEdit,
)

import app_info
import check
import AboutDialog


def about():
    """
        Displays Application About Dialog
    """
    dlg = AboutDialog.AboutDialog()
    dlg.exec_()


def help():
    webbrowser.open(app_info.HELP_URL)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindowForm()
        self.ui.setupUi(self)

        self.ui.actionOpen_DB_File.triggered.connect(self.open_db)
        self.ui.actionOpen_SPS_File.triggered.connect(self.open_sps)
        self.ui.actionProcess.triggered.connect(self.process)
        self.ui.actionAbout.triggered.connect(about)
        self.ui.actionHelp.triggered.connect(help)

        # status tips copied from tool tip ?
        self.ui.actionOpen_DB_File.setStatusTip(self.ui.actionOpen_DB_File.toolTip())

        self.ui.lblDb.setText('')
        self.ui.lblSPS.setText('')

        self.db_file = None
        self.sps_file = None

    def open_db(self):
        """
            Opens DB file
        """

        self.db_file, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "SQLite (*.sqlite );;All files (*.*)",
            # options=QFileDialog.DontUseNativeDialog
        )

        if not self.db_file:
            return

        self.ui.lblDb.setText(self.db_file)

    def open_sps(self):
        """
            Opens SPS file
        """
        self.sps_file, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "SPS Source (*.S *.SPS *.s *.sps);;SPS Receiver (*.R *.RPS *.r *.rps);;All files (*.*)",
            # options=QFileDialog.DontUseNativeDialog
        )

        if not self.sps_file:
            return

        self.ui.lblSPS.setText(self.sps_file)

    def process(self):
        sps_count = 10000
        self.ui.txtOutput.clear()

        if self.db_file and self.sps_file:
            self.runner()


        self.print2output('Number of points processed: %d' % sps_count)

    def runner(self):
        start_time = time.time()
        if self.db_file and self.sps_source_file:
            limit_easting = float(self.ui.limitX.text())
            limit_northing = float(self.ui.limitY.text())
            result = check.process(self.db_file, self.sps_file, limit_easting, limit_northing)
            self.print_stats(result)

    def print2output(self, text):
        self.ui.txtOutput.append(text)
