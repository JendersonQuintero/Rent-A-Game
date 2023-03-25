from Juego import Juego
import Estante as e

import re

status = ["EN STOCK ", "AGOTADO"]


def validar_input(string):
    pattern = re.compile("^[a-zA-Z]{6}[0-9]{2}$")
    if pattern.match(string):
        print("El modelo del videojuego es válido.")
    else:
        print("El modelo debe contener 6 letras y 2 números: ")


def mostrarJuegos():
    video_juegos = []
    try:
        with open("db_juegos.txt") as dbe:
            datos = dbe.readlines()
        if len(datos) == 0:
            print("\nTodavía no hay ningún juego registrado.\n")
        else:
            for dato in datos:
                juego = dato[:-1].split("//")
                video_juegos.append(Juego(juego[0],juego[1],juego[2]))

            print("\n********** JUEGOS REGISTRADOS ********** ")
            for i,vid1 in enumerate(video_juegos):
                print("\n")
                print("-"*6,str(i+1),"-"*6)
                print(vid1.mostrar_juego())
            return True

    except FileNotFoundError:
        print("\nTodavía no hay ningún juego registrado.\n")
        return False


def agregarJuego():
    while True:
        modelo = input(
            "Ingrese los primeros dígitos del título del videojuego (6 letras) y los dígitos de la cota (2 números): ").upper()
        try:
            validar_input(modelo)
            break
        except (ValueError):
            print("error")

    titulo = input("Ingrese el título del videojuego: ").capitalize()

    while not titulo.isalpha() or len(titulo) > 10:
        titulo = input(
            "El título debe contener máximo 10 caracteres: ").capitalize()

    precio = input("Ingrese el precio del videojuego: ")
    while not precio.isalnum() or int(precio) not in range(1, 999):
        precio = input("Ingreso inválido. Ingrese el precio del videojuego: ")

    video_juego = Juego(modelo, titulo, precio, status)
    with open("db_juegos.txt", "a+") as dbe:
        dbe.write(f"{modelo}//{titulo}//{precio}//{status[0]}\n")

    print("\nVideojuego guardado con éxito.")
    return video_juego


def buscarJuegoModelo():
    print('Aquí se busca el juego por modelo')


def buscarJuegoTitulo():
    print('Aquí se busca el juego por título')


def alquilarJuego():
    print('Aquí se alquila un juego')


def devolverJuego():
    print('Aquí se devuleve un juego')


def eliminarJuego():
    print('Aquí se elimina un juego de forma FÍSICA')


if __name__ == '__main__':
    print("\n")
    print('         ********** BIENVENIDO A RENT A GAME *********\n')

    opcion: int

    while True:
        try:
            opcion = int(input('''A continuación se muestra el menú de opciones para los juegos:
            
            1 --> Mostrar
            2 --> Agregar
            3 --> Buscar
            4 --> Alquilar
            5 --> Devolver
            6 --> Eliminar físicamente
            
            >>> '''))
        except ValueError:
            print('\nLa opción ingresada no es válida\n')
            continue

        if (opcion < 1 or opcion > 6):
            print('\nLa opción ingresada no existe en el rango de opciones\n')
            continue
        else:
            if (opcion == 1):
                mostrarJuegos()
                break
            elif (opcion == 2):
                agregarJuego()
                break
            elif (opcion == 3):
                while True:
                    try:
                        opcion = int(input('''\nSeleccione su tipo de búsqueda:
                        
                            1 --> Por Modelo
                            2 --> Por título
                        
                        >>> '''))
                    except ValueError:
                        print('\nLa opción ingresada no es válida\n')
                        continue

                    if (opcion < 1 or opcion > 2):
                        print(
                            '\nLa opción ingresada no existe en el rango de opciones\n')
                        continue
                    else:
                        if (opcion == 1):
                            buscarJuegoModelo()
                            break
                        elif (opcion == 2):
                            buscarJuegoTitulo()
                            break
            elif (opcion == 4):
                alquilarJuego()
                break
            elif (opcion == 5):
                devolverJuego()
                break
            elif (opcion == 6):
                eliminarJuego()
                break
