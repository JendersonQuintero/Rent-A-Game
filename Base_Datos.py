from Juego import Juego


class Base_Datos:
    video_juegos: list[Juego] = []

    def __init__(self) -> None:
        self

    def cargar_Juegos(self) -> list[Juego]:
        try:
            with open("db_juegos.txt") as dbe:
                datos = dbe.readlines()

            if len(datos) == 0:
                return self.video_juegos
            else:
                for dato in datos:
                    juego = dato[:-1].split("//")
                    self.video_juegos.append(
                        Juego(juego[0], juego[1], juego[2]))

                return self.video_juegos

        except FileNotFoundError:
            return False

    def guardar_juegos(self, juegos_txt: str) -> None:
        try:
            with open("db_juegos.txt", "w") as dbe:
                dbe.write(juegos_txt)
        except FileNotFoundError:
            return False

    def guardar_juego(self, juego: Juego) -> None:
        try:
            with open("db_juegos.txt", "a+") as dbe:
                dbe.write(
                    f"{juego.get_modelo()}//{juego.get_titulo()}//{juego.get_precio()}//{juego.get_status()}\n")
            return None
        except FileNotFoundError:
            return False

    def actualizar_juego(self, nuevo_juego: Juego) -> None:
        try:
            juegos_txt: str = ''

            with open("db_juegos.txt") as dbe:
                datos = dbe.readlines()

            if len(datos) == 0:
                return None
            else:
                for dato in datos:
                    juego = dato[:-1].split("//")

                    if (juego[0] == nuevo_juego.get_modelo()):
                        juegos_txt += f"{nuevo_juego.get_modelo()}//{nuevo_juego.get_titulo()}//{nuevo_juego.get_precio()}//{nuevo_juego.get_status()}\n"
                    else:
                        juegos_txt += f"{juego[0]}//{juego[1]}//{juego[2]}//{juego[3]}\n"
                with open("db_juegos.txt", 'w') as dbe:
                    dbe.write(juegos_txt)
        except FileNotFoundError:
            return None

    def eliminar_juego(self, juego: Juego) -> None:
        try:
            juegos_txt: str = ''

            with open("db_juegos.txt") as dbe:
                datos = dbe.readlines()

            if len(datos) == 0:
                return None
            else:
                for dato in datos:
                    juego = dato[:-1].split("//")

                    if (juego[0] != juego.get_modelo()):
                        juegos_txt += f"{juego[0]}//{juego[1]}//{juego[2]}//{juego[3]}\n"

                with open("db_juegos.txt", 'w') as dbe:
                    dbe.write(juegos_txt)
        except FileNotFoundError:
            return None
