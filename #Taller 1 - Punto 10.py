#Taller 1 - Punto 10
#Escriba un programa que dada una distancia calcule:
#El tiempo que le tomaría a la luz recorrer la distancia, el tiempo que le tomaría al sonido (en el aire) recorrer la distancia, el tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia, el tiempo que le tomaría a Bolt recorrer la distancia.
def introducir():
    distancia = float(input("Ingrese una distancia en metros. Ejemplo: 5: "))
    desarrollo(distancia)
    return distancia

def desarrollo(distancia):
    tiempo1 = distancia/2.998e+8
    print(f"El tiempo que tarda la luz en recorrer {distancia} metros en el vacio es de: {tiempo1} segundos.")

    tiempo2 = distancia/343
    print(f"El tiempo que tarda el sonido en recorrer {distancia} metros en el aire (20°C) es de: {tiempo2} segundos.")

    tiempo3 = distancia/136.2444
    print(f"El tiempo que tarda el Bugatti Vhiron Super Sport 300+ en recorrer {distancia} metros en el aire es de: {tiempo3} segundos.")

    tiempo4 = distancia/11.666
    print(f"El tiempo que tarda Bolt en recorrer {distancia} metros en el aire es de: {tiempo4} segundos.")
    return
    
def continuar():
    opcion = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

print("Programa para conocer la capital de un país de América")

while True:
    pais = introducir()
    opcion = continuar()
    if opcion == 2:
        break

# ! /\|=\/