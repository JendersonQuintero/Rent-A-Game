import re
import Estante as e
from Juego import Juego

estante = e.Estante_Juegos()


class Validar_Datos:

    pattern_modelo: str = "^[a-zA-Z]{6}[0-9]{2}$"

    def __init__(self) -> None:
        self

    def validar_opcion(self, opcion: str) -> bool:
        try:
            v_opcion = int(opcion)

            if (v_opcion >= 1 and v_opcion <= 8):
                return True
            print('\nLa opción ingresada no está dentro del rango de opciones\n')
            return False
        except ValueError:
            print('\nLa opción ingresada es inválida\n')
            return False

    def validar_opcion_busqueda(self, opcion: str) -> bool:
        try:
            v_opcion = int(opcion)

            if (v_opcion >= 1 and v_opcion <= 3):
                return True
            print('\nLa opción ingresada no está dentro del rango de opciones\n')
            return False
        except ValueError:
            print('\nLa opción ingresada es inválida\n')
            return False

    def validar_opcion_accion(self, opcion: str) -> bool:
        try:
            v_opcion = int(opcion)

            if (v_opcion >= 1 and v_opcion <= 4):
                return True
            print('\nLa opción ingresada no está dentro del rango de opciones\n')
            return False
        except ValueError:
            print('\nLa opción ingresada es inválida\n')
            return False

    def validar_opcion_decidir(self, opcion: str) -> bool:
        try:
            v_opcion = int(opcion)

            if (v_opcion >= 1 and v_opcion <= 2):
                return True
            print('\nLa opción ingresada no está dentro del rango de opciones\n')
            return False
        except ValueError:
            print('\nLa opción ingresada es inválida\n')
            return False

    def validar_modelo(self, modelo: str) -> bool:
        pattern = re.compile(self.pattern_modelo)
        if pattern.match(modelo):
            coincidencia: Juego or None = estante.buscar_modelo(estante)
            if (coincidencia is None):
                return True
            else:
                print('\nEl modelo ingresado ya existe\n')
                False
        else:
            print(
                '\nEl modelo de contener 6 letras y 2 números respectivamente. Ejem: "ABCDEF12"\n')
            return False

    def validar_titulo(self, titulo: str) -> bool:
        if (len(titulo) > 10):
            print('\nEl título no debe exceder los 10 caracteres\n')
            return False
        else:
            coincidencia: Juego = estante.buscar_titulo(titulo)
            if (coincidencia is None):
                return True
            else:
                print('\nEl título ingresado ya existe\n')
                return False

    def validar_precio(self, precio: str) -> bool:
        try:
            v_precio: int = int(precio)

            if (v_precio >= 1 and v_precio <= 999):
                return True
            print('\nEl precio debe estar entre 1 y 999 bolivares\n')
            return False
        except ValueError:
            print('\nEl precio ingresado no es válido\n')
            return False
