#Taller 1 - Punto 2
#Realice un programa que lea tres números reales y determine cuál es el mayor.

def introducir():
    num1 : float = float(input("Ingrese el primer número. Ejemplo: 1.5: "))
    num2 : float = float(input("Ingrese el primer número. Ejemplo: 2: "))
    num3 : float = float(input("Ingrese el primer número. Ejemplo: 3.75: "))
    desarrollo(num1,num2,num3)

def desarrollo(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            print(f"El {num1} es el número mayor.")            
            return
        else:
            print(f"El {num3} es el número mayor.")            
            return
    elif num2>num1:
        if num2>num3:
            print(f"El {num2} es el número mayor.")            
            return
        else:
            print(f"El {num3} es el número mayor.")            
            return
    else:
            print(f"El {num3} es el número mayor.")            
            return


def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Ingrese tres números reales para determinar cuál es el número mayor.")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/