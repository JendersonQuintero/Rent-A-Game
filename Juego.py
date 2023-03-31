class Juego:

    def __init__(self, modelo: str, titulo: str, precio: int, status: str = 'EN STOCK'):
        self.modelo = modelo
        self.titulo = titulo
        self.precio = precio
        self.status = status

    def get_modelo(self) -> str:
        return self.modelo

    def get_titulo(self) -> str:
        return self.titulo

    def get_precio(self) -> int:
        return self.precio

    def get_status(self) -> str:
        return self.status

    def set_modelo(self, new_modelo) -> None:
        self.modelo = new_modelo

    def set_titulo(self, new_titulo) -> None:
        self.titulo = new_titulo

    def set_precio(self, new_precio) -> None:
        self.precio = new_precio

    def set_status(self, new_status) -> None:
        self.status = new_status
