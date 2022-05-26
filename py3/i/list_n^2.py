def run(a):
    l = []

    for i in range(a+1):
        l.append(i**2)

    print(l)


if __name__ == '__main__':
    a = int(input('cuanto numeros al cuadrado quieres que te genere la lista?: '))
    print("""
    ----------
    Imprimiendo lista:
    ----------
    """)
    run(a)