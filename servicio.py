from abc import ABC, abstractmethod
from excepciones import ServicioInvalidoError

class Servicio(ABC):

    def __init__(self, nombre, costo_hora):
        if costo_hora <= 0:
            raise ServicioInvalidoError(
                "El costo debe ser mayor que cero"
            )
        self.nombre = nombre
        self.costo_hora = costo_hora

    @abstractmethod
    def calcular_costo(self,horas):
        pass

    @abstractmethod
    def descripcion(self):
        pass
    