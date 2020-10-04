from PyQt5.QtWidgets import QApplication
import MainWindowOld
import MainWindow

def main():
    import sys
    app = QApplication(sys.argv)
    # window = MainWindowOld.MainWindow()
    window = MainWindow.MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
