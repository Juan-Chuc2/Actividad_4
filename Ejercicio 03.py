#Ejercicio 03
print(" Sistema de autenticación avanzado con penalización")
users=["Juan15","pEdro25", "Pabl012" ]
passwords= [123, 456, 789]
for i in range (3):
    user=input("ingrese su usuario ")
    password=int(input("ingrese su contraseña "))
    if user == users and password==passwords:
        print("Boenvenido")
        print("1. Ver perfil")
        print("2. Cambiar contraseña")
        print("3. Cerras Sesión")
    elif i !=3:
        print("Usuario o Contraseña incorrecta")
        print("vuelva a intentarlo")
    else:
        print("▲ Acceso Bloqueado▲")