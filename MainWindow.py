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

        # self.ui.btnOpenDb.clicked.connect(self.clicked_btn_open_db)
        # self.ui.btnOpenSPS.clicked.connect(self.clicked_btn_open_sps)
        # self.ui.btnProcess.clicked.connect(self.clicked_btn_process)
        # self.ui.btnRemoveSPS.clicked.connect(self.clicked_btn_remove_sps)
        # self.ui.comboFileType.addItem('SPS 2.1')
        # self.ui.lblStatus.setText('')

        self.ui.actionOpen_DB_File.triggered.connect(self.open_db)
        self.ui.actionOpen_SPS_File.triggered.connect(self.open_sps)
        self.ui.actionProcess.triggered.connect(self.process)
        self.ui.actionAbout.triggered.connect(about)
        self.ui.actionHelp.triggered.connect(help)

        # status tips copied from tool tip ?
        # self.ui.actionOpen_DB_File.setStatusTip(self.ui.actionOpen_DB_File.toolTip())

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

    #
    # def clicked_btn_remove_sps(self):
    #     for i in self.ui.listSPS.selectedItems():
    #         self.ui.listSPS.takeItem(self.ui.listSPS.row(i))
    #
    # def clicked_btn_process(self):
    #     """
    #         Process
    #     """
    #     self.ui.lblStatus.setText('')
    #     self.ui.btnProcess.setDisabled(True)
    #     self.ui.btnDone.setDisabled(True)
    #     start_time = time.time()
    #     sps_files = [str(self.ui.listSPS.item(i).text()) for i in range(self.ui.listSPS.count())]
    #
    #     if self.db_file and len(sps_files) > 0:
    #         for sps_file in sps_files:
    #             result = dbupdate.process(self.db_file, sps_file)
    #             msg = "%s, %d, %.2fs" \
    #                   % (os.path.basename(sps_file), result, time.time() - start_time)
    #             self.ui.lblStatus.setText(msg)
    #
    #     self.ui.btnProcess.setEnabled(True)
    #     self.ui.btnDone.setEnabled(True)

    def process(self):
        sps_count = 10000
        self.ui.txtOutput.clear()

        self.print2output('Run')

        for i in range(20):
            self.print2output('Running :)')

        self.print2output('Finished')

        self.print2output('Number of points processed: %d' % sps_count)

    def print2output(self, text):
        self.ui.txtOutput.append(text)
