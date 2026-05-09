from abc import ABC, abstractmethod

# Clase abstracta Servicio
class Servicio(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass


# Clase derivada ReservaSala
class ReservaSala(Servicio):

    def calcular_costo(self, horas):
        return self.precio * horas


# Clase derivada AlquilerEquipo
class AlquilerEquipo(Servicio):

    def calcular_costo(self, dias):
        return self.precio * dias


# Clase derivada Asesoria
class Asesoria(Servicio):

    def calcular_costo(self, sesiones):
        return self.precio * sesiones


# ===== PRUEBAS =====

if __name__ == "__main__":

    sala = ReservaSala("Sala de reuniones", 10000)
    equipo = AlquilerEquipo("Computador", 5000)
    asesoria = Asesoria("Asesoría técnica", 20000)

    print("Costo sala:", sala.calcular_costo(2))
    print("Costo equipo:", equipo.calcular_costo(3))
    print("Costo asesoría:", asesoria.calcular_costo(1))
