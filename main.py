from Juego import Juego as j
import Estante as e


def mostrarJuegos():
    print('Aquí se muestran los juegos')


def agregarJuego():
    # print('Aquí se agrega el juego')

    modelo = "hola"
    titulo = "holaaa"
    precio = 2

    juego = juego(modelo, titulo, precio)
    with open("db_juegos.txt", "a") as j:
        j.write(
            f"Modelo: {modelo}, Titulo: {titulo}, Precio: {precio}\n")
        
        return juego

# letras_modelo = input(
#     "Ingrese los primeros 6 dígitos del título del videojuego (letras): ", maxlength=6)
# while not letras_modelo.isalpha:
#     letras_modelo = input(
#         "Ingrese los primeros 6 dígitos del título del videojuego (letras): ")


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
