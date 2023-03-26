import Juego


class Base_Datos:

    Juegos = [Juego]

    def __init__(self):
        self.video_juegos: list = []

    def cargar_Juegos(self) -> Juegos:
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
