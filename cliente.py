from excepciones import ClienteInvalidoError

class Cliente:

    def __init__(self, nombre, identificacion, correo):
        self.nombre = nombre
        self.identificacion = identificacion
        self.correo = correo

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        if len(valor.strip())== 0:
            raise ClienteInvalidoError(
                "El nombre no puede estar vacio"
            )
        self.__nombre = valor

    def mostrar(self):
        return f"{self.nombre} - {self.identificacion}"
