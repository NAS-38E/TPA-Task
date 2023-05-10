import sys
from ventana import Ventana
from PyQt6 import QtWidgets, QtCore
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
