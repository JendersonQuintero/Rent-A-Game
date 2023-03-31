from Juego import Juego
import Base_Datos as b_datos
import Estante_Juegos as e
import Menu as m

if __name__ == '__main__':
    bd = b_datos.Base_Datos()
    estante: e = e.Estante_Juegos()
    menu = m.Menu()

    juegos: list[Juego] = bd.cargar_Juegos()

    for juego in juegos:
        estante.insertar(juego)

    menu.mostrar_bienvenida()

    opcion: int = menu.menu_opcion()

    menu.controlador_menu(opcion)
