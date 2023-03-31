from Juego import Juego
import Validaciones as validar
import Estante_Juegos as e
import Base_Datos as b_datos

v = validar.Validar_Datos()
estante = e.Estante_Juegos()
bd = b_datos.Base_Datos()


class Menu:
    def __init__(self) -> None:
        pass

    def controlador_menu(self, opcion: int) -> None:
        if (opcion == 1):  # * Mostrar todos los juegos
            return self.opcion_mostrar()
        elif (opcion == 2):  # * Agregar juego
            return self.opcion_agregar()
        elif (opcion == 3):  # * Buscar juego
            return self.opcion_buscar()
        elif (opcion == 4):  # * Alquilar juego
            return self.opcion_alquilar()
        elif (opcion == 5):  # * Devolver juego
            return self.opcion_devolver()
        elif (opcion == 6):  # * Eliminar juego
            return self.opcion_eliminar()
        elif (opcion == 7):  # * Solo guardar
            return self.opcion_guardar()
        else:  # * Guardar y salir
            return self.opcion_guardar_salir()

    def mostrar_bienvenida(self) -> None:
        return print('\n         ********** BIENVENIDO A RENT A GAME *********')

    def menu_opcion(self) -> int:
        opcion = input('''\nA continuación se muestra el menú de opciones para los juegos:
            
            1 --> Mostrar
            2 --> Agregar
            3 --> Buscar
            4 --> Alquilar
            5 --> Devolver
            6 --> Eliminar
            7 --> Guardar
            8 --> Guardar y salir
            
            >>> ''')
        if (v.validar_opcion(opcion)):
            return int(opcion)
        else:
            return self.menu_opcion()

    def menu_busqueda(self) -> int:
        opcion = input('''\nEspecifique el parámetro de búsqueda:
            
            1 --> Modelo
            2 --> Título
            3 --> Salir
            
            >>> ''')
        if (v.validar_opcion_busqueda(opcion)):
            return int(opcion)
        else:
            return self.menu_busqueda()

    def menu_accion(self) -> int:
        opcion = input('''
            1 --> Alquilar
            2 --> Devolver
            3 --> Eliminar
            4 --> Salir
            
            >>> ''')
        if (v.validar_opcion_accion(opcion)):
            return int(opcion)
        else:
            return self.menu_accion()

    def menu_decidir(self) -> int:
        opcion = input('''
                       
            1 --> Si
            2 --> No
            
            >>> ''')
        if (v.validar_opcion_decidir(opcion)):
            return int(opcion)
        else:
            return self.menu_decidir()

    def opcion_mostrar(self) -> None:
        estante.mostrar_juegos()
        return self.retornar_inicio()

    def opcion_agregar(self) -> None:
        modelo: str
        titulo: str
        precio: str
        print('\nA continuación se le pedirán los datos del nuevo juego: \n')
        while True:
            modelo = input('Ingrese el modelo: ')
            if (v.validar_modelo(modelo)):
                print('')
                break
            else:
                print('')
                continue

        while True:
            titulo = input('Ingrese el título: ')
            if (v.validar_titulo(titulo)):
                print('')
                break
            else:
                print('')
                continue

        while True:
            precio = input('Ingrese el precio en Bs.: ')
            if (v.validar_precio(precio)):
                print('')
                break
            else:
                print('')
                continue
        juego: Juego = Juego(modelo, titulo, int(precio))
        res = estante.insertar(juego)
        if (res is False):
            print('\nEl estante principal y overflow está lleno\n')
            return self.retornar_inicio()

        estante.almacenar_juego(juego)
        print('\n***** El juego fue agregado al estante *****\n')
        return self.retornar_inicio()

    def opcion_buscar(self) -> None:
        opcion: int = self.menu_busqueda()

        if (opcion == 1):
            modelo: str = input('\nIngrese el modelo: ')

            coincidencia: Juego or None = estante.buscar_modelo(modelo)

            if (coincidencia is None):
                print(
                    f'\nNo se consiguió ningún juego con este modelo: {modelo}')
                return self.opcion_buscar()
            else:
                print('\nResultado de la busqueda:')
                estante.mostrar_juego(coincidencia)
                print('\nAcciones que puede realizar: \n')
                accion: int = self.menu_accion()

                if (accion == 1):
                    res: bool or None = estante.alquilar(coincidencia)
                    if (res is None):
                        print(
                            '\nAcción inválida. El juegos ya se encuentra alquilado\n')
                        return self.opcion_buscar()
                    print('\n***** El juego ha sido alquilado *****\\n')
                elif (accion == 2):
                    res: bool or None = estante.devolver(coincidencia)
                    if (res is None):
                        print(
                            '\nAcción inválida. El juegos ya se encuentra en stock\n')
                        return self.opcion_buscar()
                    print('\n***** El juego ha sido devuelto *****\n')
                elif (accion == 3):
                    estante.eliminar(coincidencia)
                    print('\n***** El juego ha sido eliminado *****\n')

                return self.retornar_inicio()

        elif (opcion == 2):
            titulo: str = input('\nIngrese el título: ')

            coincidencia: Juego or None = estante.buscar_titulo(titulo)

            if (coincidencia is None):
                print(
                    f'\nNo se consiguió ningún juego con este título: {titulo}')
                return self.opcion_buscar()
            else:
                print('\nResultado de la busqueda:')
                estante.mostrar_juego(coincidencia)
                print('Acciones que puede realizar: \n')
                accion: int = self.menu_accion()

                if (accion == 1):
                    res: bool or None = estante.alquilar(coincidencia)
                    if (res is None):
                        print(
                            '\nAcción inválida. El juegos ya se encuentra alquilado\n')
                        return self.opcion_buscar()
                    print('\n***** El juego ha sido alquilado *****\n')
                elif (accion == 2):
                    res: bool or None = estante.devolver(coincidencia)
                    if (res is None):
                        print(
                            '\nAcción inválida. El juegos ya se encuentra en stock\n')
                        return self.opcion_buscar()
                    print('\n***** El juego ha sido devuelto *****\n')
                elif (accion == 3):
                    estante.eliminar(coincidencia)
                    print('\n***** El juego ha sido eliminado *****\n')

                return self.retornar_inicio()

        else:
            self.retornar_inicio()

    def opcion_alquilar(self) -> None:
        opcion = self.menu_busqueda()

        if (opcion == 1):
            modelo: str = input('\nIngrese el modelo: ')

            coincidencia: Juego or None = estante.buscar_modelo(modelo)

            if (coincidencia is None):
                print(
                    f'\nNo se consiguió ningún juego con este modelo: {modelo}\n')
                return self.opcion_alquilar()
            else:
                print('\nResultado de la busqueda:')
                estante.mostrar_juego(coincidencia)
                print('\n¿Desea alquilar este juego?')
                accion: int = self.menu_decidir()

                if (accion == 1):
                    res: bool or None = estante.alquilar(coincidencia)
                    if (res is None):
                        print(
                            '\nAcción inválida. El juegos ya se encuentra alquilado\n')
                        return self.opcion_alquilar()

                    print('\n***** El juego ha sido alquilado *****\n')

                return self.retornar_inicio()

        elif (opcion == 2):
            titulo: str = input('\nIngrese el título: ')

            coincidencia: Juego or None = estante.buscar_titulo(titulo)

            if (coincidencia is None):
                print(
                    f'\nNo se consiguió ningún juego con este título: {titulo}\n')
                return self.opcion_alquilar()
            else:
                print('\nResultado de la busqueda:')
                estante.mostrar_juego(coincidencia)
                print('\n¿Desea alquilar este juego?')
                accion: int = self.menu_decidir()

                if (accion == 1):
                    res: bool or None = estante.alquilar(coincidencia)
                    if (res is None):
                        print(
                            '\nAcción inválida. El juegos ya se encuentra alquilado\n')
                        return self.opcion_alquilar()
                    print('\n***** El juego ha sido alquilado *****\n')

                return self.retornar_inicio()

        else:
            self.retornar_inicio()

    def opcion_devolver(self):
        opcion = self.menu_busqueda()

        if (opcion == 1):
            modelo: str = input('\nIngrese el modelo: ')

            coincidencia: Juego or None = estante.buscar_modelo(modelo)

            if (coincidencia is None):
                print(
                    f'\nNo se consiguió ningún juego con este modelo: {modelo}\n')
                return self.opcion_devolver()
            else:
                print('\nResultado de la busqueda:')
                estante.mostrar_juego(coincidencia)
                print('\n¿Desea devolver este juego?')
                accion: int = self.menu_decidir()

                if (accion == 1):
                    res: bool or None = estante.devolver(coincidencia)
                    if (res is None):
                        print(
                            '\nAcción inválida. El juegos ya se encuentra en stock\n')
                        return self.opcion_devolver()
                    print('\n***** El juego ha sido devuelto *****\n')

                return self.retornar_inicio()

        elif (opcion == 2):
            titulo: str = input('\nIngrese el título: ')

            coincidencia: Juego or None = estante.buscar_titulo(titulo)

            if (coincidencia is None):
                print(
                    f'\nNo se consiguió ningún juego con este título: {titulo}\n')
                return self.opcion_devolver()
            else:
                print('\nResultado de la busqueda:')
                estante.mostrar_juego(coincidencia)
                print('\n¿Desea devolver este juego?')
                accion: int = self.menu_decidir()

                if (accion == 1):
                    res: bool or None = estante.devolver(coincidencia)
                    if (res is None):
                        print(
                            '\nAcción inválida. El juegos ya se encuentra en stock\n')
                        return self.opcion_alquilar()
                    print('\n***** El juego ha sido devuelto *****\n')

                return self.retornar_inicio()

        else:
            self.retornar_inicio()

    def opcion_eliminar(self):
        opcion = self.menu_busqueda()

        if (opcion == 1):
            modelo: str = input('\nIngrese el modelo: ')

            coincidencia: Juego or None = estante.buscar_modelo(modelo)

            if (coincidencia is None):
                print(
                    f'\nNo se consiguió ningún juego con este modelo: {modelo}\n')
                return self.opcion_eliminar()
            else:
                print('\nResultado de la busqueda:')
                estante.mostrar_juego(coincidencia)
                print('\n¿Desea eliminar este juego?')
                accion: int = self.menu_decidir()

                if (accion == 1):
                    estante.eliminar(coincidencia)
                    print('\n***** El juego ha sido eliminado *****\n')

                return self.retornar_inicio()

        elif (opcion == 2):
            titulo: str = input('\nIngrese el título: ')

            coincidencia: Juego or None = estante.buscar_titulo(titulo)

            if (coincidencia is None):
                print(
                    f'\nNo se consiguió ningún juego con este título: {titulo}\n')
                return self.opcion_eliminar()
            else:
                print('\nResultado de la busqueda:')
                estante.mostrar_juego(coincidencia)
                print('\n¿Desea eliminar este juego?')
                accion: int = self.menu_decidir()

                if (accion == 1):
                    estante.eliminar(coincidencia)
                    print('\n***** El juego ha sido eliminado *****\n')

                return self.retornar_inicio()

        else:
            self.retornar_inicio()

    def opcion_guardar(self) -> None:
        estante.guardar_juegos()
        print('\n***** Los datos de guardaron correctamente *****')
        return self.retornar_inicio()

    def opcion_guardar_salir(self) -> None:
        estante.guardar_juegos()
        print('\n  ***** Los datos de guardaron correctamente *****\n')
        print('\n***** Gracias por usar Rent A Game. Hasta pronto. *****\n')
        return None

    def retornar_inicio(self) -> None:
        opcion: int = self.menu_opcion()
        return self.controlador_menu(opcion)
