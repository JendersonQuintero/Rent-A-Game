import re


class Validar_Datos:

    pattern_modelo: str = "^[a-zA-Z]{6}[0-9]{2}$"

    def __init__(self) -> None:
        self

    def validar_modelo(self, modelo: str) -> bool:
        pattern = re.compile(self.pattern_modelo)
        if pattern.match(modelo):
            return True
        else:
            return False
