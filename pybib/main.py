import logging
logging.basicConfig(level=logging.DEBUG)

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pybib.pupil_edit_dialog import PupilEditDialog, Ui_Dialog


def main():
    import sys
    app = QApplication(sys.argv)
    window = PupilEditDialog()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
