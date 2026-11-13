from servicio import Servicio

class ReservaSala(Servicio):

    def calcular_costo(self,horas):
        return self.costo_hora * horas
    
    def descripcion(self):
        return "Reserva de sala"
    
class AlquilerEquipos(Servicio):
    def calcular_costo(self, horas):
        return self.costo_hora * horas * 1.10
    
    def descripcion(self):
        return "Alquiler de Equipos"
    
class AsesoriaEspecializada(Servicio):

    def calcular_costo(self,horas):
        return self.costo_hora * horas * 1.20
    
    def descripcion(self):
        return "Asesoria Especializada"
        