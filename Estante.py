from Juego import Juego
import Hashing as h

# ***** ESTATUS PARA CONTROL DE COORDENADA *********
# ** V = VACIO
# ** B = BORRADO
# ** O = OCUPADO


class Estante_Juegos:

    estante_principal = [['V', 'V', 'V'],
                         ['V', 'V', 'V'],
                         ['V', 'V', 'V']]

    estante_overflow = [
        ['V', 'V', 'V'], ['V', 'V', 'V'], ['V', 'V', 'V'],
        ['V', 'V', 'V'], ['V', 'V', 'V'], ['V', 'V', 'V']]

    tiene_juegos_EP = False
    tiene_juegos_EO = False

    def __init__(self):
        self

    def mostrar_juegos(self):  # TODO: Acomodar forma de mostrar los juegos
        print(self.estante_principal)
        print('\n')
        print(self.estante_overflow)

    def insertar(self, juego: Juego):
        ubicacion: tuple = h.func_hash(
            juego.get_modelo(), self.estante_principal, self.estante_overflow)

        if (ubicacion[2] == 'P'):
            self.estante_principal[ubicacion[0]][ubicacion[1]] = juego
            self.tiene_juegos_EP = True
        else:
            self.estante_overflow[ubicacion[0]][ubicacion[1]] = juego
            self.tiene_juegos_EO = True


juego = Juego('SPACEI13', 'La Prueba', 999)
juego2 = Juego('ABCDEF99', 'El Cambio', 666)
estante = Estante_Juegos()
estante.insertar(juego)
estante.insertar(juego2)

estante.mostrar_juegos()
