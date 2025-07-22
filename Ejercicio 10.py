print("Bienvemido al comparador de fechas")
print("Primera fecha:")
day1 = int(input("Día: "))
month1 = int(input("Mes: "))
year1 = int(input("Año: "))
print("Segunda fecha:")
day2 = int(input("Día: "))
month2 = int(input("Mes: "))
year2 = int(input("Año: "))
if year1 > year2:
    print("La primera fecha es mayor.")
elif year1 < year2:
    print("La segunda fecha es mayor.")
else:
    if month1 > month2:
        print("La primera fecha es mayor.")
    elif month1 < month2:
        print("La segunda fecha es mayor.")
    else:
        if day1 > day2:
            print("La primera fecha es mayor.")
        elif day1 < day2:
            print("La segunda fecha es mayor.")
        else:
            print("Ambas fechas son iguales.")