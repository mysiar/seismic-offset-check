from datetime import datetime
import time
import webbrowser
from UIMainWindowForm import Ui_MainWindowForm
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import QSettings
import AboutDialog
import DbUpdate
import app_info
import app_settings
import common
import db
from FixedWidthTextParser.Seismic.SpsParser import Sps21Parser, Point
from Warning import Warning

CHECK_CSV_HEADER = 'line,point,easting,northing,check_easting,check_northing,error_easting,error_northing'
CHECK_EXT = '.check.csv'
NOT_IN_DB_CSV_HEADER = 'line,point,easting,northing'
NOT_IN_DB_EXT = '.not-in-db.csv'
LOG_EXT = '.check.log'


def about():
    """
        Displays Application About Dialog
    """
    dlg = AboutDialog.AboutDialog()
    dlg.exec_()


def help():
    webbrowser.open(app_info.HELP_URL)


def license():
    webbrowser.open(app_info.LICENSE_URL)


def db_update():
    """
        Displays Dialog
    """
    dlg = DbUpdate.DbUpdate()
    dlg.exec_()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindowForm()
        self.ui.setupUi(self)

        self.ui.actionOpen_DB_File.triggered.connect(self.open_db)
        self.ui.actionOpen_SPS_File.triggered.connect(self.open_sps)
        self.ui.actionProcess.triggered.connect(self.process)
        self.ui.actionAbout.triggered.connect(about)
        self.ui.actionLicense.triggered.connect(license)
        self.ui.actionHelp.triggered.connect(help)
        self.ui.actionQuit.triggered.connect(self.close_application)
        self.ui.actionCreate_DB.triggered.connect(self.create_db_file)
        self.ui.actionUpdate_DB.triggered.connect(db_update)
        # status tips copied from tool tip ?
        # self.ui.actionOpen_DB_File.setStatusTip(self.ui.actionOpen_DB_File.toolTip())

        self.ui.lblDb.setText('')
        self.ui.lblSPS.setText('')

        self.db_file = None
        self.sps_file = None
        self.log_file = None

        self.settings = QSettings(app_settings.ORG, app_settings.APP)

        self.settings_read()

    def warning_nothing_to_process(self):
        dlg = Warning()
        dlg.set_label('Are you dumb ?\nWhat do you want to process ?\nSelect both DB & SPS files')
        dlg.exec_()

    def open_db(self):
        """
            Opens DB file
        """
        previous_db_file = self.db_file
        self.db_file, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "SQLite (*.sqlite );;All files (*.*)",
            # options=QFileDialog.DontUseNativeDialog
        )

        if not self.db_file:
            self.db_file = previous_db_file

        self.ui.lblDb.setText(self.db_file)

    def open_sps(self):
        """
            Opens SPS file
        """
        previous_sps_file = self.sps_file
        self.sps_file, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "SPS Source (*.S *.SPS *.s *.sps);;SPS Receiver (*.R *.RPS *.r *.rps);;All files (*.*)",
            # options=QFileDialog.DontUseNativeDialog
        )

        if not self.sps_file:
            self.sps_file = previous_sps_file

        self.ui.lblSPS.setText(self.sps_file)
        self.log_file = self.sps_file + LOG_EXT

    def process(self):
        if self.db_file and self.sps_file:
            self.runner()
        else:
            self.warning_nothing_to_process()

    def runner(self):
        common.log_file_create(self.log_file)
        start_time = time.time()
        if self.db_file and self.sps_file:
            line_numbers = common.count_file_line_number(self.sps_file)
            self.ui.progressBar.setMaximum(line_numbers)
            limit_x = float(self.ui.limitX.text())
            limit_y = float(self.ui.limitY.text())
            self.log(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
            self.log('DB: %s' % self.db_file)
            self.log('DB record count: %d' % db.count_db_records(self.db_file))
            self.log('SPS: %s' % self.sps_file)
            self.log('SPS record count: %d' % line_numbers)
            self.log('Limits: E: %.2f, N: %.2f' % (limit_x, limit_y))
            result = self.check(limit_x, limit_y)
            timing = time.time() - start_time
            point_count = result['PC']
            not_in_db_count = result['NDB']
            offset_count_x = result['OCX']
            offset_count_y = result['OCY']
            poffset_count_x = offset_count_x / point_count * 100
            poffset_count_y = offset_count_y / point_count * 100

            self.log('Number of points: %d' % point_count)
            self.log('Number of points not in DB: %d' % not_in_db_count)
            self.log('Errors Easting: %d points, %.2f%s' % (offset_count_x, poffset_count_x, '%'))
            self.log('Errors Nothing: %d points, %.2f%s' % (offset_count_y, poffset_count_y, '%'))
            self.log('Elapsed time: %d sec' % timing)
            self.print2output('-----------------------------------------------------------------')

    def print2output(self, text):
        self.ui.txtOutput.append(text)

    def log(self, text):
        self.print2output(text)
        common.log_file_record_add(self.log_file, text)

    def settings_save(self):
        self.settings.setValue(app_settings.LIMIT_X, self.ui.limitX.text())
        self.settings.setValue(app_settings.LIMIT_Y, self.ui.limitY.text())
        self.settings.setValue(app_settings.DB_PATH, self.db_file)

    def settings_read(self):
        self.ui.limitX.setText(self.settings.value(app_settings.LIMIT_X, '0.0', type=str))
        self.ui.limitY.setText(self.settings.value(app_settings.LIMIT_Y, '0.0', type=str))
        db_file = self.settings.value(app_settings.DB_PATH, '', type=str)
        if 0 == len(db_file):
            db_file = None
        self.db_file = db_file
        self.ui.lblDb.setText(db_file)

    def close_application(self):
        self.settings_save()
        self.close()

    def create_db_file(self):
        db_file, _ = QFileDialog.getSaveFileName(
            self,
            "Create DB",
            "",
            "SQLite files (*.sqlite);;All Files (*)",
            # options=QFileDialog.DontUseNativeDialog
        )

        if not db_file:
            return

        if not db_file.endswith(db.DB_FILE_EXT):
            db_file += db.DB_FILE_EXT
        db.create_db(db_file)
        db_log_file = db_file + common.DB_LOG_FILE_EXT
        common.log_file_create(db_log_file)
        common.log_file_record_add(db_log_file, f"Created: {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}")
        common.log_file_record_add(db_log_file, '-----------------------------------------------------------------')

    def check(self, limit_x, limit_y):
        connection = db.create_connection(self.db_file)
        parser = Sps21Parser()
        check_file = self.sps_file + CHECK_EXT
        not_in_db_file = self.sps_file + NOT_IN_DB_EXT

        common.csv_file_create(check_file, CHECK_CSV_HEADER)
        common.csv_file_create(not_in_db_file, NOT_IN_DB_CSV_HEADER)

        with open(self.sps_file) as sps:
            line = sps.readline()
            sps_counter = 0
            not_in_db_counter = 0
            offset_counter_x = 0
            offset_counter_y = 0
            while line:
                stats = parser.parse_point(line)
                if stats is not None:
                    point = Point(stats)

                    stats = db.get_record_for_point(connection, point)

                    if stats is None:
                        sps_counter += 1
                        not_in_db_counter += 1
                        record = "%.2f,%.2f,%.1f,%.1f" \
                                 % (
                                     point.line, point.point, point.easting, point.northing)
                        common.csv_file_record_add(not_in_db_file, record)
                        line = sps.readline()
                        continue
                    de = point.easting - stats[0]
                    dn = point.northing - stats[1]

                    error_easting = 0
                    if abs(de) > limit_x:
                        offset_counter_x += 1
                        error_easting = 1

                    error_northing = 0
                    if abs(dn) > limit_y:
                        offset_counter_y += 1
                        error_northing = 1

                    record = "%.2f,%.2f,%.1f,%.1f,%.1f,%.1f,%d,%d" \
                             % (
                                 point.line, point.point, point.easting, point.northing, de, dn, error_easting,
                                 error_northing)
                    common.csv_file_record_add(check_file, record)

                    sps_counter += 1
                    self.ui.progressBar.setValue(sps_counter)

                line = sps.readline()

            sps.close()

            stats = {
                'PC': sps_counter,
                'NDB': not_in_db_counter,
                'OCX': offset_counter_x,
                'OCY': offset_counter_y
            }

            connection.close()

            return stats
