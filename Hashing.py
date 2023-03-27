def func_hash(clave: str, list_p: list, list_o: list):
    acumulador: int = 0
    suma_num: int = 0
    for i in range(len(clave)):
        acumulador += ord(clave[i])
        if (ord(clave[i]) >= 48 and ord(clave[i]) <= 57):
            suma_num += int(clave[i])

    grupo: int = (acumulador // suma_num) % len(list_p)
    grupo_max = False

    if (grupo == (len(list_p) - 1)):
        grupo_max = True

    while True:
        for i in range(len(list_p[grupo])):
            if (list_p[grupo][i] == 'V'):
                return grupo, i, 'P'
            elif (list_p[grupo][i] == 'B'):
                return grupo, i, 'P'
            else:
                continue

        if (grupo_max):
            grupo = 0
            for i in range(len(list_p[grupo]) - 1):
                if (list_p[grupo][i] == 'V'):
                    return grupo, i, 'P'
                elif (list_p[grupo][i] == 'B'):
                    return grupo, i, 'P'
                else:
                    grupo += 1
        elif (grupo < (len(list_p) - 1)):
            grupo += 1
        else:
            break

    # ***** INICIO DEL OVERFLOW ******

    grupo_overflow: int = (acumulador // suma_num) % len(list_o)
    grupo_max = False

    if (grupo_overflow == (len(list_o) - 1)):
        grupo_max = True

    while True:
        for i in range(len(list_o[grupo_overflow])):
            if (list_o[grupo_overflow][i] == 'V'):
                return grupo_overflow, i, 'O'
            elif (list_o[grupo_overflow][i] == 'B'):
                return grupo_overflow, i, 'O'
            else:
                continue

        if (grupo_max):
            grupo_overflow = 0
            for i in range(len(list_o[grupo_overflow]) - 1):
                if (list_o[grupo_overflow][i] == 'V'):
                    return grupo_overflow, i, 'P'
                elif (list_o[grupo_overflow][i] == 'B'):
                    return grupo_overflow, i, 'P'
                else:
                    grupo_overflow += 1
        elif (grupo_overflow < (len(list_o) - 1)):
            grupo_overflow += 1
        else:
            break
