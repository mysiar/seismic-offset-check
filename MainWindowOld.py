"""
    Application Main Window
"""
import os
import time
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QKeySequence
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
import check
import db
from DbUpdate import DbUpdate

QApplication.setApplicationName(app_info.TITLE)
QApplication.setApplicationDisplayName(app_info.TITLE)
QApplication.setApplicationVersion(app_info.VERSION)


def about():
    """
        Displays Application About Dialog
    """
    dlg = AboutDialog.AboutDialog()
    dlg.exec_()


def db_update():
    """
        Displays Dialog
    """
    dlg = DbUpdate()
    dlg.exec_()


class MainWindow(QMainWindow):
    """
        MainWindow
    """

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle(app_info.TITLE)
        self.setFixedSize(QSize(app_info.MAIN_WINDOWS_WIDTH, app_info.MAIN_WINDOW_HEIGHT))

        self.db_file = None
        self.sps_source_file = None
        self.window_layout = None
        self.label_no_source_points = None
        self.label_no_easting_offsets = None
        self.label_no_northing_offsets = None
        self.label_db_file = None
        self.label_sps_source_file = None
        self.label_check_file = None

        # TOOLBAR
        toolbar = QToolBar()
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        action_db_open = QAction(QIcon(os.path.join("icons", "tree.png")), "Open DB", self)
        action_db_open.setShortcut(QKeySequence("Ctrl+o"))
        action_db_open.triggered.connect(self.open_db_file)
        action_db_open.setStatusTip("Open DB with preplan")
        toolbar.addAction(action_db_open)

        action_db_create = QAction(QIcon(os.path.join("icons", "tree--plus.png")), "Create DB", self)
        action_db_create.triggered.connect(self.create_db_file)
        action_db_create.setStatusTip("Create SQLite DB")

        action_db_update = QAction(QIcon(os.path.join("icons", "tree--pencil.png")), "Update DB", self)
        action_db_update.triggered.connect(db_update)
        action_db_update.setStatusTip("Update SQLite DB with plan from SPS")

        action_sps_source_open = QAction(QIcon(os.path.join("icons", "folder-open-document.png")),
                                         "Open SPS Source file", self)
        action_sps_source_open.setShortcut(QKeySequence("Ctrl+o"))
        action_sps_source_open.triggered.connect(self.open_sps_source_file)
        action_sps_source_open.setStatusTip("Open daily SPS source point for check")
        toolbar.addAction(action_sps_source_open)

        toolbar.addSeparator()

        action_run = QAction(QIcon(os.path.join("icons", "burn.png")), "Run", self)
        action_run.setShortcut(QKeySequence("Ctrl+r"))
        action_run.triggered.connect(self.run)
        action_run.setStatusTip("Run check")
        toolbar.addAction(action_run)

        toolbar.addSeparator()

        action_about = QAction(QIcon(os.path.join("icons", "information-button.png")), "About", self)
        action_about.setShortcut(QKeySequence("Ctrl+i"))
        action_about.triggered.connect(about)
        action_about.setStatusTip("About application")
        toolbar.addAction(action_about)

        toolbar.addSeparator()
        toolbar.addSeparator()
        toolbar.addSeparator()
        toolbar.addSeparator()

        action_quit = QAction(QIcon(os.path.join("icons", "cross.png")), "Quit", self)
        action_quit.setShortcut(QKeySequence("Ctrl+q"))
        action_quit.triggered.connect(qApp.quit)
        action_quit.setStatusTip("Quit the application")
        toolbar.addAction(action_quit)

        # MENU
        menu = self.menuBar()
        menu_file = menu.addMenu("&File")
        menu_file.addAction(action_db_open)
        menu_file.addAction(action_sps_source_open)
        menu_file.addSeparator()
        menu_file.addAction(action_quit)

        menu_run = menu.addMenu("&Run")
        menu_run.addAction(action_run)

        menu_db = menu.addMenu("&DB")
        menu_db.addAction(action_db_create)
        menu_db.addAction(action_db_update)

        menu_help = menu.addMenu("&Help")
        menu_help.addAction(action_about)

        self.setStatusBar(QStatusBar(self))

        # LAYOUT
        self.window_layout = QGridLayout()
        self.window_layout.setSpacing(5)
        self.window_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.window_layout.addWidget(QLabel('DB'), 0, 0)
        self.window_layout.addWidget(QLabel('SPS Source'), 1, 0)
        self.window_layout.addWidget(QLabel('Check'), 2, 0)

        self.window_layout.addWidget(QLabel(''), 3, 0)
        self.window_layout.addWidget(QLabel('Limit Easting'), 4, 0)
        self.window_layout.addWidget(QLabel('Limit Northing'), 5, 0)

        self.label_db_file = QLabel('')
        self.label_sps_source_file = QLabel('')
        self.label_check_file = QLabel('')

        self.window_layout.addWidget(self.label_db_file, 0, 1)
        self.window_layout.addWidget(self.label_sps_source_file, 1, 1)
        self.window_layout.addWidget(self.label_check_file, 2, 1)

        self.widget_limit_easting = QLineEdit()
        self.widget_limit_easting.setMaxLength(5)
        self.widget_limit_easting.setText(str(app_info.LIMIT_INLINE))
        self.window_layout.addWidget(self.widget_limit_easting, 4, 1)

        self.widget_limit_northing = QLineEdit()
        self.widget_limit_northing.setMaxLength(5)
        self.widget_limit_northing.setText(str(app_info.LIMIT_XLINE))
        self.window_layout.addWidget(self.widget_limit_northing, 5, 1)
        self.window_layout.addWidget(QLabel(''), 6, 0)
        self.window_layout.addWidget(QLabel('No of Source Points'), 7, 0)
        self.window_layout.addWidget(QLabel('No of Easting offsets'), 8, 0)
        self.window_layout.addWidget(QLabel('No of Northing offsets'), 9, 0)

        self.label_no_source_points = QLabel('')
        self.label_no_easting_offsets = QLabel('')
        self.label_no_northing_offsets = QLabel('')

        self.window_layout.addWidget(self.label_no_source_points, 7, 1)
        self.window_layout.addWidget(self.label_no_easting_offsets, 8, 1)
        self.window_layout.addWidget(self.label_no_northing_offsets, 9, 1)

        widget = QWidget(self)
        widget.setLayout(self.window_layout)

        self.setCentralWidget(widget)

    def open_db_file(self):
        """
            Opens DB file
        """
        self.db_file, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "SQLite (*.sqlite );;" "All files (*.*)",
            # options=QFileDialog.DontUseNativeDialog
        )

        if not self.db_file:
            return

        self.label_db_file.setText(os.path.basename(self.db_file))

    def open_sps_source_file(self):
        """
            Opens SPS Source file
        """
        self.sps_source_file, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "SPS Source (*.S *.SPS *.s *.sps);;" "All files (*.*)",
            # options=QFileDialog.DontUseNativeDialog
        )

        if not self.sps_source_file:
            return

        self.label_sps_source_file.setText(os.path.basename(self.sps_source_file))
        self.label_check_file.setText(os.path.basename(os.path.basename(self.sps_source_file) + check.CHECK_EXT))

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

        db.create_db(db_file)

    def run(self):
        """
            Runs
        """
        start_time = time.time()
        if self.db_file and self.sps_source_file:
            limit_easting = float(self.widget_limit_easting.text())
            limit_northing = float(self.widget_limit_northing.text())
            result = check.process(self.db_file, self.sps_source_file, limit_easting, limit_northing)
            self.print_stats(result)

    def print_stats(self, result):
        sp = result['SP']
        oce = result['OCE']
        ocn = result['OCN']

        poce = oce / sp * 100
        pocn = ocn / sp * 100

        s_oce = "%d (%.2f%s)" % (oce, poce, '%')
        s_ocn = "%d (%.2f%s)" % (ocn, pocn, '%')

        self.label_no_source_points.setText(str(sp))
        self.label_no_easting_offsets.setText(s_oce)
        self.label_no_northing_offsets.setText(s_ocn)
