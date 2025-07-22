#Ejercicio 05
fecha = int(input("Ingrese la fecha en formato ddmmaaaa (ej: 15082023): "))
año = fecha % 10000
resto = fecha // 10000
mes = resto % 100
dia = resto // 100
fecha_valida = True
if mes < 1 or mes > 12:
    fecha_valida = False
else:
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        bisiesto = True
    else:
        bisiesto = False
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias_del_mes = 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias_del_mes = 30
    elif mes == 2:
        if bisiesto:
            dias_del_mes = 29
        else:
            dias_del_mes = 28
    if dia < 1 or dia > dias_del_mes:
        fecha_valida = False
if fecha_valida:
    mes_original = mes
    año_original = año
    if mes == 1 or mes == 2:
        mes += 12
        año -= 1
    q = dia
    m = mes
    K = año % 100
    J = año // 100
    h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7
    if h == 0:
        dia_nombre = "sábado"
    elif h == 1:
        dia_nombre = "domingo"
    elif h == 2:
        dia_nombre = "lunes"
    elif h == 3:
        dia_nombre = "martes"
    elif h == 4:
        dia_nombre = "miércoles"
    elif h == 5:
        dia_nombre = "jueves"
    elif h == 6:
        dia_nombre = "viernes"
    print("La fecha {:02d}/{:02d}/{} fue un {}".format(dia, mes_original, año_original, dia_nombre))
else:
    print("La fecha ingresada no es válida.")