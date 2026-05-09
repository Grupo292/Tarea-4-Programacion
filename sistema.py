import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class ErrorSistema(Exception):
    pass

class ErrorValidacion(ErrorSistema):
    pass

class ErrorReserva(ErrorSistema):
    pass


class Entidad(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass


class Cliente(Entidad):
    def __init__(self, nombre, cedula):
        try:
            if not nombre:
                raise ErrorValidacion("Nombre vacío")

            if not cedula.isdigit():
                raise ErrorValidacion("Cédula inválida")

            self.__nombre = nombre
            self.__cedula = cedula

        except Exception as e:
            logging.error(e)
            raise

    def mostrar_info(self):
        return f"{self.__nombre} - {self.__cedula}"

    def get_nombre(self):
        return self.__nombre


class Servicio(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass


class ServicioSala(Servicio):
    def calcular_costo(self, horas):
        return self.precio * horas


class ServicioEquipo(Servicio):
    def calcular_costo(self, dias):
        return self.precio * dias


class ServicioAsesoria(Servicio):
    def calcular_costo(self, sesiones):
        return self.precio * sesiones


class Reserva:
    def __init__(self, cliente, servicio, cantidad):
        try:
            if cantidad <= 0:
                raise ErrorReserva("Cantidad inválida")

            self.cliente = cliente
            self.servicio = servicio
            self.cantidad = cantidad
            self.estado = "Pendiente"

        except Exception as e:
            logging.error(e)
            raise

    def procesar(self):
        try:
            costo = self.servicio.calcular_costo(self.cantidad)
            self.estado = "Confirmada"
            return costo
        except Exception as e:
            logging.error(e)
            self.estado = "Error"

    def mostrar(self):
        return f"{self.cliente.get_nombre()} - {self.servicio.nombre} - {self.estado}"


class Sistema:
    def __init__(self):
        self.clientes = []
        self.reservas = []

    def registrar_cliente(self, nombre, cedula):
        try:
            cliente = Cliente(nombre, cedula)
            self.clientes.append(cliente)
            print("Cliente registrado")
        except:
            print("Error cliente")

    def crear_reserva(self, cliente, servicio, cantidad):
        try:
            reserva = Reserva(cliente, servicio, cantidad)
            costo = reserva.procesar()
            self.reservas.append(reserva)
            print("Reserva OK:", costo)
        except:
            print("Error reserva")

    def mostrar_reservas(self):
        for r in self.reservas:
            print(r.mostrar())


if __name__ == "__main__":

    sistema = Sistema()

    sistema.registrar_cliente("Juan", "12345")
    sistema.registrar_cliente("", "abc")

    sala = ServicioSala("Sala", 10000)
    equipo = ServicioEquipo("Equipo", 5000)

    cliente1 = sistema.clientes[0]

    sistema.crear_reserva(cliente1, sala, 2)
    sistema.crear_reserva(cliente1, equipo, -1)

    sistema.mostrar_reservas()
