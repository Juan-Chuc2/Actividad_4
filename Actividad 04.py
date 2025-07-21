# Ejercicio 01
#print("Bienvenido al simulador de votacion cruzada ")
#name_user= str(input("Ingrese su nombre completo ")).upper()
#dpi1=input("Ingrese su numero de DPI(Documento Personal de Identificacion) ")
#departamentos=str(input("Ingrese su departamento ")).upper()
#year_of_birth= int(input("Ingrese su año de nacimiento (solo el año) "))
#name= len(name_user)
#dpi= len(dpi1)
#if dpi <13 or name<=5:
 #   print("Su dpi o nombre es invalido")
#elif departamentos== "ALTA VERAPAZ" or departamentos== "PETEN" :
   # if (2025 - year_of_birth)==17 or (2025 - year_of_birth) >=18:
  #      print(f"Bienvenido {name_user}, su centro de votacion es {departamentos}")
 #   print("")
#elif  (2025 - year_of_birth) >=18:
 #   print(f"Bienvenido {name_user}, su centro de votacion es {departamentos}")
#else:
    #print("no puede votar verifique si a su edad puede votar en su departamento ")
#Ejercicio 02
#print("Calculadora de impuestos progresivos y deducciones")
#annual_income= int(input("Ingrese la Cantidad de su salariio anual "))
#dependents= int(input("Ingrese el numero de dependientes "))
#if annual_income>= 0 and annual_income <= 30000 and dependents <= 2:
  #  impuesto= (annual_income -(dependents*1000))* 0.05
 #   print("Usted debe pagar un impuesto de ", impuesto)
#elif annual_income < 40000 and dependents > 2:
 #   print("Ud no paga impuestos")
#elif annual_income>= 30001 and annual_income<=60000 and dependents >0:
  #  impuesto2= (annual_income -(dependents*1000))*0.10
 #   print("Usted debe pagar un impuesto de ", impuesto2)
#elif annual_income >= 60001 and annual_income <=100000:
  #  impuesto3=(annual_income-(dependents*1000))*0.15
 #   print("Usted debe pagar un impuesto de ", impuesto3)
#elif annual_income > 100000:
  #  impuesto4=(annual_income-(dependents*1000))*0.20
 #   print("Usted debe de pagar un impuesto de ", impuesto4)
#else :
  #  print("Datos invalidos")