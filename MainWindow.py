"""
    Application Main Window
"""
import os
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

QApplication.setApplicationName(app_info.TITLE)
QApplication.setApplicationDisplayName(app_info.TITLE)
QApplication.setApplicationVersion(app_info.VERSION)


def about():
    """
        Displays Application About Dialog
    """
    dlg = AboutDialog.AboutDialog()
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

        # TOOLBAR
        toolbar = QToolBar()
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        open_db_action = QAction(QIcon(os.path.join("icons", "tree.png")), "Open DB", self)
        open_db_action.setShortcut(QKeySequence("Ctrl+o"))
        open_db_action.triggered.connect(self.open_db_file)
        open_db_action.setStatusTip("Open DB with preplan")
        toolbar.addAction(open_db_action)

        open_sps_source_action = QAction(QIcon(os.path.join("icons", "folder-open-document.png")),
                                         "Open SPS Source file", self)
        open_sps_source_action.setShortcut(QKeySequence("Ctrl+o"))
        open_sps_source_action.triggered.connect(self.open_sps_source_file)
        open_sps_source_action.setStatusTip("Open daily SPS source point for check")
        toolbar.addAction(open_sps_source_action)

        toolbar.addSeparator()

        run_action = QAction(QIcon(os.path.join("icons", "burn.png")), "Run", self)
        run_action.setShortcut(QKeySequence("Ctrl+r"))
        run_action.triggered.connect(self.run)
        run_action.setStatusTip("Run check")
        toolbar.addAction(run_action)

        toolbar.addSeparator()

        about_action = QAction(QIcon(os.path.join("icons", "information-button.png")), "About", self)
        about_action.setShortcut(QKeySequence("Ctrl+i"))
        about_action.triggered.connect(about)
        about_action.setStatusTip("About application")
        toolbar.addAction(about_action)

        toolbar.addSeparator()
        toolbar.addSeparator()
        toolbar.addSeparator()
        toolbar.addSeparator()

        quit_action = QAction(QIcon(os.path.join("icons", "cross.png")), "Quit", self)
        quit_action.setShortcut(QKeySequence("Ctrl+q"))
        quit_action.triggered.connect(qApp.quit)
        quit_action.setStatusTip("Quit the application")
        toolbar.addAction(quit_action)

        # MENU
        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(open_db_action)
        file_menu.addAction(open_sps_source_action)
        file_menu.addSeparator()
        file_menu.addAction(quit_action)

        run_menu = menu.addMenu("&Run")
        run_menu.addAction(run_action)

        help_menu = menu.addMenu("&Help")
        help_menu.addAction(about_action)

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
        )

        if not self.db_file:
            return

        self.window_layout.addWidget(QLabel(os.path.basename(self.db_file)), 0, 1, Qt.AlignTop)

    def open_sps_source_file(self):
        """
            Opens SPS Source file
        """
        self.sps_source_file, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "SPS Source (*.S *.SPS *.s *.sps);;" "All files (*.*)",
        )

        if not self.sps_source_file:
            return

        self.window_layout.addWidget(QLabel(os.path.basename(self.sps_source_file)), 1, 1)
        self.window_layout.addWidget(QLabel(os.path.basename(self.sps_source_file) + check.CHECK_EXT), 2, 1)

    def run(self):
        """
            Runs
        """
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
