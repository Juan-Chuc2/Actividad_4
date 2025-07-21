#Ejercicio 03
print(" Sistema de autenticación avanzado con penalización")
users=["Juan15","pEdro25", "Pabl012" ]
passwords= [123, 456, 789]
logged_in= False
for i in range (3):
    user=input("ingrese su usuario ")
    password=int(input("ingrese su contraseña "))
    if user in users and password in passwords:
        user1 = users.index(user)
        if password == passwords[user1]:
             print("Boenvenido")
             print("1. Ver perfil")
             print("2. Cambiar contraseña")
             print("3. Cerras Sesión")
             logged_in= True
             break
        else:
            print("Usuario o Contraseña incorrecta")
            print("Vuelva a intentarlo ")
    else:
        print("Usuario o Contraseña incorrecta")
        print("Vuelva a intentarlo ")

if not logged_in:
    print("▲ Aceso Bloqueado ▲")