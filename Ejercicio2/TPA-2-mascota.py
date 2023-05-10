import sys
from PyQt6 import QtWidgets, uic
from VentanaPrincipal import Ui_VentanaPrincipal
from VentanaSecundaria import Ui_VentanaSecundaria

class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, peso:float):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def __str__(self) -> str:
        return f"Mascota {self.nombre} de {self.edad} anios de la especie {self.especie} con {self.peso} Kg."


class Ventana(QtWidgets.QMainWindow, Ui_VentanaPrincipal):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)
        # Conexión del botón guardar con el método guardar_mascota
#implementacion guardar mascota
    def guardar_mascota(self):
        # Recuperación de la información de los componentes
        nombre = self.campo_nombre.text()
        especie = self.campo_especie.text()
        edad = int(self.campo_edad.text())
        peso = float(self.campo_peso.text())

        # Creación del objeto Mascota con los datos recuperados
        mascota = Mascota(nombre, especie, edad, peso)

        # Mostrar información de Mascota en ventana secundaria VentanaSecundaria.py a través del método str() de la clase Mascota
        ventana_secundaria = Ui_VentanaSecundaria(str(mascota))
        ventana_secundaria.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    vista = Ventana()
    vista.show()
    app.exec()