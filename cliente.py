# =========================================================
# CLIENTE.PY
# Clase Cliente con Programación Orientada a Objetos
# =========================================================

# ---------------------------------------------------------
# EXCEPCIÓN PERSONALIZADA
# ---------------------------------------------------------

class ClienteError(Exception):
    """
    Excepción personalizada para errores de clientes
    """
    pass


# ---------------------------------------------------------
# CLASE CLIENTE
# ---------------------------------------------------------

class Cliente:

    # -----------------------------------------------------
    # CONSTRUCTOR
    # -----------------------------------------------------

    def __init__(self, nombre, documento):

        """
        Constructor de la clase Cliente
        """

        # VALIDACIÓN DEL NOMBRE
        if not nombre.strip():
            raise ClienteError(
                "El nombre no puede estar vacío"
            )

        # VALIDACIÓN DEL DOCUMENTO
        if not documento.isdigit():
            raise ClienteError(
                "El documento debe contener solo números"
            )

        # ENCAPSULACIÓN
        self.__nombre = nombre
        self.__documento = documento

    # -----------------------------------------------------
    # MÉTODO GET NOMBRE
    # -----------------------------------------------------

    def get_nombre(self):

        """
        Retorna el nombre del cliente
        """

        return self.__nombre

    # -----------------------------------------------------
    # MÉTODO GET DOCUMENTO
    # -----------------------------------------------------

    def get_documento(self):

        """
        Retorna el documento del cliente
        """

        return self.__documento

    # -----------------------------------------------------
    # MÉTODO SET NOMBRE
    # -----------------------------------------------------

    def set_nombre(self, nuevo_nombre):

        """
        Modifica el nombre del cliente
        """

        if not nuevo_nombre.strip():
            raise ClienteError(
                "El nuevo nombre no puede estar vacío"
            )

        self.__nombre = nuevo_nombre

    # -----------------------------------------------------
    # MÉTODO SET DOCUMENTO
    # -----------------------------------------------------

    def set_documento(self, nuevo_documento):

        """
        Modifica el documento del cliente
        """

        if not nuevo_documento.isdigit():
            raise ClienteError(
                "El documento debe contener números"
            )

        self.__documento = nuevo_documento

    # -----------------------------------------------------
    # MOSTRAR DATOS
    # -----------------------------------------------------

    def mostrar_datos(self):

        """
        Muestra los datos del cliente
        """

        return (
            f"Cliente: {self.__nombre} "
            f"- Documento: {self.__documento}"
        )


# =========================================================
# PRUEBAS DEL SISTEMA
# =========================================================

try:

    # CLIENTE VÁLIDO
    cliente1 = Cliente(
        "Maribel Ruiz Dueñas",
        "1077854372"
    )

    print(cliente1.mostrar_datos())

    # CAMBIO DE NOMBRE
    cliente1.set_nombre("Maribel Dueñas")

    print(cliente1.get_nombre())

except ClienteError as error:

    print("Error:", error)


# ---------------------------------------------------------
# CLIENTE INVÁLIDO
# ---------------------------------------------------------

try:

    cliente2 = Cliente(
        "",
        "ABC123"
    )

except ClienteError as error:

    print("Error detectado:", error)