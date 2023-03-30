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

        grupo: int = (acumulador // suma_num) % espacio

        return grupo

    def func_hash(self, clave: str, list_p: list, list_o: list) -> tuple:
        capacidad_max_gp: int = 3
        capacidad_max_go: int = 3

        grupo: int = self.hash(clave, len(list_p))

        if (len(list_p[grupo]) <= capacidad_max_gp):
            return grupo, 'P'

        # ***** INICIO DEL OVERFLOW *****

        grupo_overflow: int = self.hash(clave, len(list_o))
        grupo_max: bool = False

        if (grupo_overflow == (len(list_o) - 1)):
            grupo_max = True

        while True:

            if (len(list_o[grupo_overflow]) <= capacidad_max_go):
                return grupo_overflow, 'O'

            if (grupo_max):
                grupo_overflow = 0

                while True:
                    if (len(list_o[grupo_overflow]) <= capacidad_max_go):
                        return grupo_overflow, 'O'
                    elif (grupo_overflow < (len(list_o) - 1)):
                        grupo_overflow += 1
                    else:
                        break

    def buscar_hash(self, clave: str, list_p: list, list_o: list) -> tuple:

        grupo: int = self.hash(clave, len(list_p))

        for juego in list_p[grupo]:
            if (juego.get_modelo() == clave):
                return grupo, 'P'
            else:
                continue

        # ***** BUSQUEDA EN OVERFLOW *****

        grupo_overflow: int = self.hash(clave, len(list_o))
        grupo_max = False

        if (grupo_overflow == (len(list_o) - 1)):
            grupo_max = True

        while True:
            for juego in list_o[grupo_overflow]:
                if (juego.get_modelo() == clave):
                    return grupo_overflow, 'O'
                else:
                    continue

            if (grupo_max):
                grupo_overflow = 0
                grupo_max = False
            elif (grupo_overflow < (len(list_o) - 1)):
                grupo_overflow += 1
            else:
                return grupo_overflow, 'N'
