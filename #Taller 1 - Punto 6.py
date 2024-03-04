#Taller 1 - Punto 6
#Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.
def introducir():
    letra = input("Ingrese una letra: ").lower()
    desarrollo(letra)

def desarrollo(letra):
    vocales = ["a","e","i","o","u"]
    if letra in vocales:
        print(f"La letra {letra} es una vocal.")
        return
    else:
        print(f"La letra {letra} es una consonante.")
        return

def continuar():
    opcion = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

print("Ingrese una letra para conocer si es una vocal o una consonante")

while True:
    introducir()
    opcion = continuar()
    if opcion == 2:
        break

# ! /\|=\/