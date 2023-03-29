from Juego import Juego


class Base_Datos:

    def __init__(self) -> None:
        self.video_juegos: list[Juego] = []

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

    def guardar_juego(self, juego: Juego) -> None:
        try:
            with open("db_juegos.txt", "a+") as dbe:
                dbe.write(
                    f"{juego.get_modelo()}//{juego.get_titulo()}//{juego.get_precio()}//{juego.get_status()}\n")
            return None
        except FileNotFoundError:
            return False
