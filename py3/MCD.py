#import

def menu():
    print("""
    -------------------------------------------------------
    |Bienvenido al programa para calcular MCD de un numero|
    |        traves del algoritmo de Euclides             |
    -------------------------------------------------------
    """)

def repit():
    b = input('Repetimos? S / N :')
    b = b.lower()

    if b == "s":
        run()
    elif b == "n":
        print("Gracias por usar el programa")
    else:
        print("Escribe una opción valida")
        print(" ")
        repit()


def run():
    a = int(input("Ingrese el primer numero (numero a): "))
    b = int(input("Ingrese el segundo numero (numero b): "))
    r = 1

    if a > b:
        a1 = a
        b1 = b
    else:
        a1 = b
        b1 = a

    while r != 0:
        r = a1 % b1
        aux = b1
        a1 = aux
        b1 = r

    print(f"El mcd({a},{b}) = {a1}")
    repit()

if __name__ == "__main__":
    menu()
    run ()
