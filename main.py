from Juego import Juego
from validaciones import Validar_Datos
import Estante as e
import Base_Datos as b_datos


if __name__ == '__main__':
    bd = b_datos.Base_Datos()
    estante = e.Estante_Juegos()

    print('\n         ********** BIENVENIDO A RENT A GAME *********\n')

    opcion: int

    while True:
        try:
            opcion = int(input('''A continuación se muestra el menú de opciones para los juegos:
            
            1 --> Mostrar
            2 --> Agregar
            3 --> Buscar
            4 --> Alquilar
            5 --> Devolver
            6 --> Eliminar
            7 --> Guardar y salir
            
            >>> '''))
        except ValueError:
            print('\nLa opción ingresada no es válida\n')
            continue

        if (opcion < 1 or opcion > 7):
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
