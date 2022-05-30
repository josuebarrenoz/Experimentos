def run(a,b):
    b
    d = {i:i**3 for i in range(a+1)}
    print(d)

if __name__ == "__main__":
    a = int(input('cuanto numeros quieres que te genere el diccionario?: '))
    b = 0
    #b = int(input("Con que numero divisible se quiere generar estos numeros?: "))
    print("""
    ----------
    Imprimiendo lista:
    ----------
    """)
    run(a,b)