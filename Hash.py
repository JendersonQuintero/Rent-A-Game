# ord() Para transformar a ascii
# chr() Para transformar a su valor UNIX

def func_hash(clave: str) -> int:
    acumulador: int = 0
    suma_num: int = 0
    for i in range(len(clave)):
        acumulador += ord(clave[i])
        if (ord(clave[i]) >= 48 and ord(clave[i]) <= 57):
            suma_num += int(clave[i])

    # Cambiar 3 por el length del array primario
    grupo = (acumulador // suma_num) % 3
    return grupo


func_hash('JUMPER99')
func_hash('SPACEI12')
func_hash('JFHYXT35')
func_hash('ABCDEF30')
