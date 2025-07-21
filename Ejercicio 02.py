#Ejercicio 02
print("Calculadora de impuestos progresivos y deducciones")
annual_income= int(input("Ingrese la Cantidad de su salariio anual "))
dependents= int(input("Ingrese el numero de dependientes "))
if annual_income>= 0 and annual_income <= 30000 and dependents <= 2:
    impuesto= (annual_income -(dependents*1000))* 0.05
    print("Usted debe pagar un impuesto de ", impuesto)
elif annual_income < 40000 and dependents > 2:
    print("Ud no paga impuestos")
elif annual_income>= 30001 and annual_income<=60000 and dependents >0:
    impuesto2= (annual_income -(dependents*1000))*0.10
    print("Usted debe pagar un impuesto de ", impuesto2)
elif annual_income >= 60001 and annual_income <=100000:
    impuesto3=(annual_income-(dependents*1000))*0.15
    print("Usted debe pagar un impuesto de ", impuesto3)
elif annual_income > 100000:
    impuesto4=(annual_income-(dependents*1000))*0.20
    print("Usted debe de pagar un impuesto de ", impuesto4)
else :
    print("Datos invalidos")