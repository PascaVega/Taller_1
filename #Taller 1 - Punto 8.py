#Taller 1 - Punto 8
#Escriba un programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra.

def introducir():
    frecuencia : float = float(input("Ingrese la frcuencia de una onda (en hz). Ejemplo: 50.75: "))
    desarrollo(frecuencia)
    parte_espectro : str = desarrollo(frecuencia)
    print(f"La frecuencia de onda {frecuencia} HZ se encuentra en la parte del espectro electromagnético {parte_espectro}")

def desarrollo(frecuencia):
    if frecuencia <3e9:
        return "Radiofrecuencia (RF)"
    elif 3e9 <= frecuencia < 3e11:
        return "Microondas"
    elif 3e11 <= frecuencia < 4e14:
        return "Infrarojo (IR)"
    elif 4e14 <= frecuencia < 7.9e14:
        return "Luz visible"
    elif 7.9e14 <= frecuencia < 3e17:
        return "Ultravioleta (UV)"
    elif 3e17 <= frecuencia < 3e19:
        return "Rayos X"
    else:
        return "Rayos Gamma"

def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Ingrese la frecuencia en hz de una onda para determinar en qué parte del espectro electromagnético se encuentra.")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/