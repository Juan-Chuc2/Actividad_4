# Ejercicio 01
print("Bienvenido al simulador de votacion cruzada ")
name_user= str(input("Ingrese su nombre completo ")).upper()
dpi1=input("Ingrese su numero de DPI(Documento Personal de Identificacion) ")
departamentos=str(input("Ingrese su departamento ")).upper()
year_of_birth= int(input("Ingrese su año de nacimiento (solo el año) "))
name= len(name_user)
dpi= len(dpi1)
if dpi <13 or name<=5:
    print("Su dpi o nombre es invalido")
elif departamentos== "ALTA VERAPAZ" or departamentos== "PETEN" :
    if (2025 - year_of_birth)==17 or (2025 - year_of_birth) >=18:
        print(f"Bienvenido {name_user}, su centro de votacion es {departamentos}")
    print("")
elif  (2025 - year_of_birth) >=18:
    print(f"Bienvenido {name_user}, su centro de votacion es {departamentos}")
else:
    print("no puede votar verifique si a su edad puede votar en su departamento ")