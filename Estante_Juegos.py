from Juego import Juego
from Indice import Indice
import Hashing as h
import Base_Datos as b_datos

bd = b_datos.Base_Datos()
hashing = h.Hashing()


class Estante_Juegos:

    estante_principal: list = [[] for i in range(3)]
    estante_overflow: list = [[] for i in range(6)]

    indice_titulo: list[Indice] = []

    def __init__(self) -> None:
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
        ubicacion: tuple = hashing.func_hash(
            juego.get_modelo(), self.estante_principal, self.estante_overflow)

        if (ubicacion[1] == 'P'):
            self.estante_principal[ubicacion[0]].append(juego)
        else:
            self.estante_overflow[ubicacion[0]].append(juego)

        self.indice_titulo.append(Indice(juego.get_titulo(), ubicacion))

    def buscar_modelo(self, modelo: str) -> Juego:
        ubicacion: tuple = hashing.buscar_hash(
            modelo, self.estante_principal, self.estante_overflow)
        if (ubicacion[1] == 'P'):
            for juego in self.estante_principal[ubicacion[0]]:
                if (juego.get_modelo() == modelo):
                    return juego
            return None
        elif (ubicacion[1] == 'N'):
            return None
        for juego in self.estante_overflow[ubicacion[0]]:
            if (juego.get_modelo() == modelo):
                return juego
        return None

    def buscar_titulo(self, titulo: str) -> Juego:
        for indice in self.indice_titulo:
            if (indice.get_titulo().upper() == titulo.upper()):
                ubicacion = indice.get_ubicacion()
                if (ubicacion[1] == 'P'):
                    for juego in self.estante_principal[ubicacion[0]]:
                        if (juego.get_titulo().upper() == titulo.upper()):
                            return juego
                    return None
                else:
                    for juego in self.estante_overflow[ubicacion[0]]:
                        if (juego.get_titulo().upper() == titulo.upper()):
                            return juego
            else:
                continue
        return None

    def eliminar(self, juego: Juego) -> None:
        ubicacion: tuple = hashing.buscar_hash(
            juego.get_modelo(), self.estante_principal, self.estante_overflow)
        if (ubicacion[1] == 'P'):
            for j in range(len(self.estante_principal[ubicacion[0]])):
                if (self.estante_principal[ubicacion[0]][j].get_modelo() == juego.get_modelo()):
                    self.estante_principal[ubicacion[0]].pop(j)
                    return None
        for j in range(len(self.estante_overflow[ubicacion[0]])):
            if (self.estante_overflow[ubicacion[0]][j].get_modelo() == juego.get_modelo()):
                self.estante_overflow[ubicacion[0]].pop(j)
                return None
        bd.eliminar_juego(juego)
        for i in range(len(self.indice_titulo)):
            if (self.indice_titulo[i].get_titulo() == juego.get_titulo()):
                self.indice_titulo.pop(i)
                return None
        return None

    def alquilar(self, juego: Juego) -> bool or None:
        if (juego.get_status() == 'ALQUILADO'):
            return None

        juego_actualizado: Juego = juego
        juego_actualizado.set_status('ALQUILADO')

        ubicacion: tuple = hashing.buscar_hash(
            juego.get_modelo(), self.estante_principal, self.estante_overflow)
        if (ubicacion[1] == 'P'):
            for j in range(len(self.estante_principal[ubicacion[0]])):
                if (self.estante_principal[ubicacion[0]][j].get_modelo() == juego.get_modelo()):
                    self.estante_principal[ubicacion[0]][j] = juego_actualizado
                    bd.actualizar_juego(juego_actualizado)
                    return True
            return None

        for j in range(len(self.estante_overflow[ubicacion[0]])):
            if (self.estante_overflow[ubicacion[0]][j].get_modelo() == juego.get_modelo()):
                self.estante_overflow[ubicacion[0]][j] = juego_actualizado
                bd.actualizar_juego(juego_actualizado)
                return True
        return None

    def devolver(self, juego: Juego) -> bool or None:
        if (juego.get_status() == 'ES STOCK'):
            return None

        juego_actualizado: Juego = juego
        juego_actualizado.set_status('EN STOCK')

        ubicacion: tuple = hashing.buscar_hash(
            juego.get_modelo(), self.estante_principal, self.estante_overflow)
        if (ubicacion[1] == 'P'):
            for j in range(len(self.estante_principal[ubicacion[0]])):
                if (self.estante_principal[ubicacion[0]][j].get_modelo() == juego.get_modelo()):
                    self.estante_principal[ubicacion[0]][j] = juego_actualizado
                    bd.actualizar_juego(juego_actualizado)
                    return True
            return None

        for j in range(len(self.estante_overflow[ubicacion[0]])):
            if (self.estante_overflow[ubicacion[0]][j].get_modelo() == juego.get_modelo()):
                self.estante_overflow[ubicacion[0]][j] = juego_actualizado
                bd.actualizar_juego(juego_actualizado)
                return True
        return None

    def guardar_juegos(self) -> None:
        juegos_txt: str = ''

        for grupo in self.estante_principal:
            for juego in grupo:
                juegos_txt += f"{juego.get_modelo()}//{juego.get_titulo()}//{juego.get_precio()}//{juego.get_status()}\n"

        for grupo in self.estante_overflow:
            for juego in grupo:
                f"{juego.get_modelo()}//{juego.get_titulo()}//{juego.get_precio()}//{juego.get_status()}\n"

        bd.guardar_juegos(juegos_txt)
        return None

    def almacenar_juego(self, juego: Juego) -> None:
        bd.guardar_juego(juego)
        return None
