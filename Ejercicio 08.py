print("Bienvenido a la Calculadora de rumbo entre puntos cardinales")
first_chord =str(input("Ingrese la pimera cordenada")).capitalize()
second_chord = str(input("Ingrese la segunda cordenada")).capitalize()
if first_chord == "Norte" and second_chord == "Sur ":
    print("Rectpo hacia abajo, llega al sur")
elif first_chord == "Sur" and second_chord == "Norte":
    print("recto hacia arriba, llega al norte ")
elif  first_chord == "Este" and second_chord == "Oeste ":
    print("recto hacia la izquierda, llega al oeste")
elif  first_chord == "Oeste" and second_chord == "Este ":
    print("recto hacia la derecha, llega al este")
