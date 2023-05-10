import sys
from PyQt6 import QtWidgets, QtGui, QtCore

class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configurar ventana principal
        self.setWindowTitle("Sección práctica")
        self.resize(600, 400)
        
        # Crear layout horizontal principal
        layout_principal = QtWidgets.QHBoxLayout()
        
        # Crear widget de imagen
        imagen = QtGui.QPixmap("ruta_de_la_imagen.jpg") # Cambiar "ruta_de_la_imagen.jpg" por la ruta de la imagen que desees utilizar
        label_imagen = QtWidgets.QLabel()
        label_imagen.setPixmap(imagen)
        layout_principal.addWidget(label_imagen)
        
        # Crear layout vertical para el nombre de usuario y la descripción
        layout_usuario_descripcion = QtWidgets.QVBoxLayout()
        
        # Crear widget de nombre de usuario
        label_usuario = QtWidgets.QLabel("Nombre de usuario")
        label_usuario.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout_usuario_descripcion.addWidget(label_usuario)
        
        # Crear widget de descripción
        label_descripcion = QtWidgets.QLabel("Descripción de la imagen")
        label_descripcion.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout_usuario_descripcion.addWidget(label_descripcion)
        
        # Agregar layout vertical de usuario y descripción al layout principal
        layout_principal.addLayout(layout_usuario_descripcion)
        
        # Crear layout horizontal para los atributos y los valores
        layout_atributos_valores = QtWidgets.QHBoxLayout()
        
        # Crear widget de atributos
        list_atributos = QtWidgets.QListWidget()
        list_atributos.addItems(["Atributo 1", "Atributo 2", "Atributo 3", "Atributo 4", "Atributo 5", "Atributo 6"])
        layout_atributos_valores.addWidget(list_atributos)
        
        # Crear widget de valores
        list_valores = QtWidgets.QListWidget()
        list_valores.addItems(["Valor 1", "Valor 2", "Valor 3", "Valor 4", "Valor 5", "Valor 6"])
        layout_atributos_valores.addWidget(list_valores)
        
        # Agregar layout horizontal de atributos y valores al layout principal
        layout_principal.addLayout(layout_atributos_valores)
        
        # Crear widget de botón OK
        boton_ok = QtWidgets.QPushButton("OK")
        boton_ok.setMaximumWidth(75)
        boton_ok.setMaximumHeight(25)
        boton_ok.clicked.connect(self.ok_presionado)
        
        # Agregar botón OK al layout principal en la esquina inferior derecha
        layout_principal.addWidget(boton_ok, 0, QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignBottom)
        
        # Agregar layout principal a la ventana
        widget_principal = QtWidgets.QWidget()
        widget_principal.setLayout(layout_principal)
        self.setCentralWidget(widget_principal)
    
    def ok_presionado(self):
        print("Botón OK presionado")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
    
    

