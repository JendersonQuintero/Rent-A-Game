class Hashing:

    def __init__(self) -> None:
        self

    def hash(self, clave: str, espacio: int) -> int:
        acumulador: int = 0
        suma_num: int = 0
        i = 0
        while True:
            for i in range(len(clave)):
                acumulador += ord(clave[i])
                try:
                    if (ord(clave[i]) >= 48 and ord(clave[i]) <= 57):
                        suma_num += int(clave[i])
                except:
                    pass

            if suma_num == 0:
                grupo: int = 0
                print("El modelo ingresado no es válido")
                break
            else:
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
        grupo_max = False

        if (grupo == (len(list_p) - 1)):
            grupo_max = True

        for i in range(len(list_p[grupo])):
            if (list_p[grupo][i].get_modelo() == clave):
                return grupo, i, 'P'
            else:
                continue

        # ***** BUSQUEDA EN OVERFLOW *****

        grupo_overflow: int = self.hash(clave, len(list_o))
        grupo_max = False

        if (grupo_overflow == (len(list_o) - 1)):
            grupo_max = True

        while True:
            for i in range(len(list_o[grupo_overflow])):
                if (list_o[grupo_overflow][i].get_modelo() == clave):
                    return grupo_overflow, i, 'O'
                else:
                    continue

            if (grupo_max):
                grupo_overflow = 0
                for i in range(len(list_o[grupo_overflow])):
                    if (list_o[grupo_overflow][i].get_modelo() == clave):
                        return grupo_overflow, i, 'O'
                    else:
                        grupo_overflow += 1
            elif (grupo_overflow < (len(list_o) - 1)):
                grupo_overflow += 1
            else:
                return grupo_overflow, i, 'N'
            break
