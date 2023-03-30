class Hashing:

    def __init__(self) -> None:
        self

    def hash(self, clave: str, espacio: int) -> int:
        acumulador: int = 0
        suma_num: int = 0
        for i in range(len(clave)):
            acumulador += ord(clave[i])
            if (ord(clave[i]) >= 48 and ord(clave[i]) <= 57):
                suma_num += int(clave[i])
        if (suma_num == 0):
            suma_num = 1
        grupo: int = (acumulador // suma_num) % espacio

        return grupo

    def func_hash(self, clave: str, list_p: list, list_o: list) -> tuple:
        capacidad_max_gp: int = 2
        capacidad_max_go: int = 2

        grupo: int = self.hash(clave, len(list_p))

        if (len(list_p[grupo]) <= capacidad_max_gp):
            return grupo, 'P'

        # ***** INICIO DEL OVERFLOW *****

        for grupo in range(len(list_o)):
            if (len(grupo) <= capacidad_max_go):
                return grupo, 'O'

        return None

    def buscar_hash(self, clave: str, list_p: list, list_o: list) -> tuple:

        grupo: int = self.hash(clave, len(list_p))

        for juego in list_p[grupo]:
            if (juego.get_modelo() == clave):
                return grupo, 'P'
            else:
                continue

        # ***** BUSQUEDA EN OVERFLOW *****

        for g in range(len(list_o)):
            for juego in range(len(g)):
                if (list_o[grupo].get_modelo() == clave):
                    return juego, 'O'

        return 0, 'N'
