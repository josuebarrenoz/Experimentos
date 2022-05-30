def run(a,b):
    l = []

    for i in range(a+1):
        if i%b != 0:
            l.append(i**2)

    print(l)


if __name__ == '__main__':
    a = int(input('cuanto numeros al cuadrado quieres que te genere la lista?: '))
    b = int(input("Con que numero divisible no se quiere generar los numeros cuadrados?: "))
    print("""
    ----------
    Imprimiendo lista:
    ----------
    """)
    run(a,b)