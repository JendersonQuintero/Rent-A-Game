class Indice:
    def __init__(self, titulo: str, ubicacion: tuple) -> None:
        self.titulo = titulo
        self.ubicacion = ubicacion

    def get_titulo(self) -> str:
        return self.titulo

    def get_ubicacion(self) -> tuple:
        return self.ubicacion

    def set_titulo(self, new_titulo) -> None:
        self.titulo = new_titulo

    def set_ubicacion(self, new_ubicacion) -> None:
        self.ubicacion = new_ubicacion
