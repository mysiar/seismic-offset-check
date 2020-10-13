import os
import time
from datetime import datetime
from PyQt5.QtWidgets import QDialog, QFileDialog
from UIDbUpdateForm import Ui_DbUpdateForm
from Warning import Warning
import dbupdate
import check
import db


class DbUpdate(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_DbUpdateForm()
        self.ui.setupUi(self)

        self.ui.btnOpenDb.clicked.connect(self.clicked_btn_open_db)
        self.ui.btnOpenSPS.clicked.connect(self.clicked_btn_open_sps)
        self.ui.btnProcess.clicked.connect(self.clicked_btn_process)
        self.ui.btnProcessFast.clicked.connect(self.clicked_btn_process_fast)
        self.ui.btnRemoveSPS.clicked.connect(self.clicked_btn_remove_sps)
        self.ui.comboFileType.addItem('SPS 2.1')
        self.ui.lblStatus.setText('')

        self.db_file = None

    def warning_process(self):
        dlg = Warning()
        dlg.set_label('Duplicated points\n You can not use "Process Fast"\n Use "Process" instead')
        dlg.exec_()

    def warning_nothing_to_update(self):
        dlg = Warning()
        dlg.set_label('Are you dumb ?\nWhat do you want to update ?\nNo files selected')
        dlg.exec_()

    def clicked_btn_open_db(self):
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

        self.ui.listDb.clear()
        self.ui.listDb.addItem(self.db_file)

    def clicked_btn_open_sps(self):
        """
            Opens SPS file
        """
        sps_file, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "SPS Source (*.S *.SPS *.s *.sps);;SPS Receiver (*.R *.RPS *.r *.rps);;All files (*.*)",
            # options=QFileDialog.DontUseNativeDialog
        )

        if not sps_file:
            return

        self.ui.listSPS.addItem(sps_file)

    def clicked_btn_remove_sps(self):
        for i in self.ui.listSPS.selectedItems():
            self.ui.listSPS.takeItem(self.ui.listSPS.row(i))

    def clicked_btn_process_fast(self):
        self.clicked_btn_process(fast=True)

    def clicked_btn_process(self, fast=False):
        """
            Process
        """
        sps_files = [str(self.ui.listSPS.item(i).text()) for i in range(self.ui.listSPS.count())]

        if self.db_file and len(sps_files) > 0:
            self.ui.lblStatus.setText('')
            self.ui.btnProcess.setDisabled(True)
            self.ui.btnDone.setDisabled(True)
            start_time = time.time()

            db_log_file = self.db_file + db.DB_LOG_FILE_EXT

            if self.db_file and len(sps_files) > 0:

                for sps_file in sps_files:
                    line_numbers = check.count_file_line_number(sps_file)
                    self.ui.progressBar.setMaximum(line_numbers)

                    result = dbupdate.process(self.ui.progressBar, self.db_file, sps_file, fast, self)
                    msg = "%s, %d, %.2fs" \
                          % (os.path.basename(sps_file), result, time.time() - start_time)
                    self.ui.lblStatus.setText(msg)
                    check.log_file_record_add(db_log_file, f"Updated: {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}")
                    check.log_file_record_add(db_log_file, 'Input file: %s' % sps_file)
                    check.log_file_record_add(db_log_file, 'No of records processed: %d' % result)
                    check.log_file_record_add(db_log_file, 'Elapsed time %.2f sec' % (time.time() - start_time))
                    check.log_file_record_add(db_log_file,
                                              '-----------------------------------------------------------------')

            self.ui.btnProcess.setEnabled(True)
            self.ui.btnDone.setEnabled(True)
        else:
            self.warning_nothing_to_update()

    def clicked_btn_process_old(self, fast=False):
        """
            Process
        """
        sps_files = [str(self.ui.listSPS.item(i).text()) for i in range(self.ui.listSPS.count())]

        if self.db_file and len(sps_files) > 0:
            self.ui.lblStatus.setText('')
            self.ui.btnProcess.setDisabled(True)
            self.ui.btnDone.setDisabled(True)
            start_time = time.time()

            db_log_file = self.db_file + db.DB_LOG_FILE_EXT

            if self.db_file and len(sps_files) > 0:

                for sps_file in sps_files:
                    line_numbers = check.count_file_line_number(sps_file)
                    self.ui.progressBar.setMaximum(line_numbers)
                    result = dbupdate.process_old(self.ui.progressBar, self.db_file, sps_file)
                    msg = "%s, %d, %.2fs" \
                          % (os.path.basename(sps_file), result, time.time() - start_time)
                    self.ui.lblStatus.setText(msg)
                    check.log_file_record_add(db_log_file, f"Updated: {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}")
                    check.log_file_record_add(db_log_file, 'Input file: %s' % sps_file)
                    check.log_file_record_add(db_log_file, 'No of records processed: %d' % result)
                    check.log_file_record_add(db_log_file, 'Elapsed time %.2f sec' % (time.time() - start_time))
                    check.log_file_record_add(db_log_file,
                                              '-----------------------------------------------------------------')

            self.ui.btnProcess.setEnabled(True)
            self.ui.btnDone.setEnabled(True)
