from PyQt5.QtWidgets import QApplication
from interface import TInterface

import sys

def main():
    application = QApplication(sys.argv)
    interface = TInterface()
    interface.show()
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()