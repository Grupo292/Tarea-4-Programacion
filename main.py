# IMPORTACION DE CLASES Y LIBRERIAS

from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from datetime import datetime


# FUNCION PARA GUARDAR ERRORES EN EL ARCHIVO logs.txt

def guardar_log(error):

    # Se abre el archivo en modo agregar ("a")
    with open("logs.txt", "a") as archivo:

        # Obtiene la fecha y hora actual
        fecha = datetime.now()

        # Guarda el error en el archivo
        archivo.write(f"{fecha} - {error}\n")


# TITULO PRINCIPAL DEL SISTEMA

print("===== SISTEMA DE RESERVAS =====")


# --------------------------------------------------
# OPERACION 1
# RESERVA VALIDA
# --------------------------------------------------

try:

    # Creacion del cliente
    cliente1 = Cliente("Juan", "12345")

    # Creacion del servicio
    servicio1 = ReservaSala("Sala Premium", 50000)

    # Creacion de la reserva
    reserva1 = Reserva(cliente1, servicio1, 2)

    # Confirmar reserva
    reserva1.confirmar()

    # Mostrar informacion
    print(reserva1.mostrar_reserva())

# Captura errores
except Exception as e:

    print("Error:", e)

    # Guarda el error en logs.txt
    guardar_log(e)


# --------------------------------------------------
# OPERACION 2
# CLIENTE INVALIDO
# --------------------------------------------------

try:

    # Nombre vacio (genera error)
    cliente2 = Cliente("", "99999")

except Exception as e:

    print("Error:", e)

    guardar_log(e)


# --------------------------------------------------
# OPERACION 3
# RESERVA VALIDA
# --------------------------------------------------

try:

    cliente3 = Cliente("Maria", "45678")

    servicio2 = AlquilerEquipo("Computador Gamer", 80000)

    reserva2 = Reserva(cliente3, servicio2, 3)

    print(reserva2.mostrar_reserva())

except Exception as e:

    print("Error:", e)

    guardar_log(e)


# --------------------------------------------------
# OPERACION 4
# DOCUMENTO INVALIDO
# --------------------------------------------------

try:

    # Documento incorrecto
    cliente4 = Cliente("Carlos", "abc")

except Exception as e:

    print("Error:", e)

    guardar_log(e)


# --------------------------------------------------
# OPERACION 5
# RESERVA VALIDA
# --------------------------------------------------

try:

    cliente5 = Cliente("Ana", "77777")

    servicio3 = Asesoria("Asesoria Programacion", 100000)

    reserva3 = Reserva(cliente5, servicio3, 1)

    reserva3.confirmar()

    print(reserva3.mostrar_reserva())

except Exception as e:

    print("Error:", e)

    guardar_log(e)


# --------------------------------------------------
# OPERACION 6
# DURACION INVALIDA
# --------------------------------------------------

try:

    # Duracion negativa (genera error)
    reserva_error = Reserva(cliente5, servicio3, -4)

except Exception as e:

    print("Error:", e)

    guardar_log(e)
# --------------------------------------------------
# OPERACION 7
# CANCELAR RESERVA
# --------------------------------------------------

try:

    cliente6 = Cliente("Pedro", "88888")

    servicio4 = ReservaSala("Sala Empresarial", 70000)

    reserva4 = Reserva(cliente6, servicio4, 2)

    reserva4.cancelar()

    print(reserva4.mostrar_reserva())

except Exception as e:

    print("Error:", e)

    guardar_log(e)
    
# --------------------------------------------------
# OPERACION 8
# DOCUMENTO VACIO
# --------------------------------------------------

try:

    cliente7 = Cliente("Laura", "")

except Exception as e:

    print("Error:", e)

    guardar_log(e)
    
# --------------------------------------------------
# OPERACION 9
# RESERVA VALIDA
# --------------------------------------------------

try:

    cliente8 = Cliente("Sofia", "11111")

    servicio5 = Asesoria("Asesoria Redes", 120000)

    reserva5 = Reserva(cliente8, servicio5, 4)

    reserva5.confirmar()

    print(reserva5.mostrar_reserva())

except Exception as e:

    print("Error:", e)

    guardar_log(e)
    
# --------------------------------------------------
# OPERACION 10
# DURACION EN CERO
# --------------------------------------------------

try:

    reserva6 = Reserva(cliente8, servicio5, 0)

except Exception as e:

    print("Error:", e)

    guardar_log(e)

# MENSAJE FINAL DEL SISTEMA

print("===== FIN DEL SISTEMA =====")
