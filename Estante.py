from Juego import Juego
from Indice import Indice
from Hashing import Hashing

# ***** ESTATUS PARA CONTROL DE COORDENADA *****
# * V = VACIO


class Estante_Juegos:

    estante_principal = [[] * 3]

    indice_titulo = []

    estante_overflow = [[] * 6]

    def __init__(self):
        self

    def mostrar_juegos(self) -> None:
        print('\n************** ESTANTE PRINCIPAL DE JUEGOS **************')
        for grupo in self.estante_principal:
            for juego in grupo:
                self.mostrar_juego(juego)

        print('\n************** ESTANTE OVERFLOW DE JUEGOS **************\n')
        for grupo in self.estante_overflow:
            for juego in grupo:
                self.mostrar_juego(juego)

    def mostrar_juego(self, juego: Juego) -> None:
        print(
            f'\nModelo: {juego.get_modelo()}\nTítulo: {juego.get_titulo()}\nPrecio: Bs. {juego.get_precio()}\nStatus: {juego.get_status()}')

    def insertar(self, juego: Juego) -> None:
        ubicacion: tuple = Hashing.func_hash(
            juego.get_modelo(), self.estante_principal, self.estante_overflow)

        if (ubicacion[1] == 'P'):
            self.estante_principal[ubicacion[0]].append(juego)
        else:
            self.estante_overflow[ubicacion[0]].append(juego)

        self.indice_titulo.append(Indice(juego.get_titulo(), ubicacion))

    def buscar_modelo(self, modelo: str) -> Juego:
        ubicacion: tuple = Hashing.buscar_hash(
            modelo, self.estante_principal, self.estante_overflow)
        if (ubicacion[2] == 'P'):
            return self.estante_principal[ubicacion[0]][ubicacion[1]]
        elif (ubicacion[2] == 'N'):
            return None
        return self.estante_overflow[ubicacion[0]][ubicacion[1]]

    def buscar_titulo(self, titulo: str) -> Juego:
        for i in self.indice_titulo:
            if (i.get_titulo() == titulo):
                ubicacion = i.get_ubicacion()
                if (ubicacion[2] == 'P'):
                    return self.estante_principal[ubicacion[0]][ubicacion[1]]

                return self.estante_overflow[ubicacion[0]][ubicacion[1]]
            else:
                continue
        return None

    def eliminar_modelo(self, modelo: str) -> None:
        ubicacion: tuple = Hashing.buscar_hash(
            modelo, self.estante_principal, self.estante_overflow)
        if (ubicacion[2] == 'P'):
            self.estante_principal[ubicacion[0]][ubicacion[1]] = 'V'
            return None
        self.estante_overflow[ubicacion[0]][ubicacion[1]] = 'V'
        return None

    def eliminar(self, juego: Juego) -> None:
        ubicacion: tuple = Hashing.buscar_hash(
            juego.get_modelo(), self.estante_principal, self.estante_overflow)
        if (ubicacion[2] == 'P'):
            self.estante_principal[ubicacion[0]][ubicacion[1]] = 'V'
            return None
        self.estante_overflow[ubicacion[0]][ubicacion[1]] = 'V'
        return None

    def alquilar(self, juego: Juego) -> None:
        juego.set_status('ALQUILADO')
        return None

    def devolver(self, juego: Juego) -> None:
        juego.set_status('EN STOCK')
        return None


# juego = Juego('SPACEI13', 'La Prueba', 999)
# juego2 = Juego('ABCDEF99', 'El Cambio', 666)
# estante = Estante_Juegos()
# estante.insertar(juego)
# estante.insertar(juego2)

# estante.mostrar_juegos()

# print(estante.buscar_titulo('La Prueba').get_modelo())
