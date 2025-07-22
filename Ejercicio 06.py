print("bienvenido Clasificador de envio con multiples condiciones ")
weight=float(input("ingrese el peso del paquete (kg) "))
distance = float(input("ingrese la distancia (km) "))
urgency =input("Ingrese si tiene urgencia por la entrega de su paquete ").lower()
size = input("El tamaño de su paquete es: Grande / Mediano / pequeño ").capitalize()
if urgency == "no" and weight < 5:
    costo_final =  (10 + (weight*2.5) + (distance*0.5)) - 20
    print("Por que su paquete no es urgente y el peso es menor a 5kg tiene un descuento de Q20")
    print("El costo final de su envio es: ", costo_final)
elif urgency == "si":
    costo_final2 = (10 + (weight*2.5) + (distance*0.5)) + 50
    print("Como el paquete es urgente su entrega tiene un recargo de Q50")
    print("El costo final de su envio es de: ", costo_final2)
elif size == "Grande":
    costo_final3 = (10 + (weight*2.5) + (distance * 0.5)) + 30
    print("Por que el paquete es Grande tiene un recargo de Q30")
    print("El costo final de su envio es de: ", costo_final3)
elif urgency == "si" and size == "Grande":
    costo_final4 = ( 10 + (weight*2.5) + (distance*0.5))+ 80
    print("Como el paquete es urgente de entregar y es Grande tiene un recargo de Q80")
    print()