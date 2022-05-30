from re import L


def run(a,b):
    l = [i for i in range(a+1) if i%b ==0]
    print(l)

if __name__ == "__main__":
    a = int(input('cuanto numeros quieres que te genere la lista?: '))
    b = int(input("Con que numero divisible se quiere generar estos numeros?: "))
    print("""
    ----------
    Imprimiendo lista:
    ----------
    """)
    run(a,b)
