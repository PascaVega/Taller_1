#Taller 1 - Punto 4
#Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.
def introducir():
    num1 : float = float(input("Ingrese el primer número: "))
    num2 : float = float(input("Ingrese el segundo número: "))
    desarrollo(num1,num2)

def desarrollo(num1,num2):
    if num2!= 0 and num1 % num2 == 0:
        print(f"{num1} es múltiplo de {num2}.")
        return
    else:
        print(f"{num1} no es múltiplo de {num2}.")
        return

def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Ingrese dos números reales para derminar si el primero es múltiplo del segundo.")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/