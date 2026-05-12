# --------------------------------------------------
# EXCEPCIONES PERSONALIZADAS DEL SISTEMA
# --------------------------------------------------


# EXCEPCION PARA ERRORES RELACIONADOS CON CLIENTES

class ClienteError(Exception):

    pass


# EXCEPCION PARA ERRORES RELACIONADOS CON SERVICIOS

class ServicioError(Exception):

    pass


# EXCEPCION PARA ERRORES RELACIONADOS CON RESERVAS

class ReservaError(Exception):

    pass
