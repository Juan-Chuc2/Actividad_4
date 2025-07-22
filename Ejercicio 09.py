print("Bienvenido al simulador de entradas al cine con validacion multiple")
age = int(input("Ingrese su edad "))
day_of_the_week =str(input("Ingrese que dia de la semana es ")).strip().lower()
is_estudent = str(input("Usted es estudiante ")).strip().lower()
if age < 13:
    print("Usted es menor de edad, acceso al cine denegado")
elif  is_estudent!="no":
    if  day_of_the_week=="miercoles":
        print("acceso permitido usted debe cancelar Q50")
    elif is_estudent =="si":
        print("acceso permitido Usted por ser estudiante paga Q35")
    else:
        print("verifique que haya escrito todo bien.")
elif is_estudent=="no":
    if  day_of_the_week=="miercoles":
        print("acceso permitido por ser miercoles ud entra al 2x1 y paga solo Q50")
    elif  is_estudent =="si":
        print("Acceso permitido por ser miercoles entra al 2x1 y por ser estudiante solo paga Q35")
    else:
        print("verifique si escribio correctamente todo")
else:
    print("verifique sus datos")