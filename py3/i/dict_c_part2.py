def run(a,b):
    d = {i:round(i**b,2) for i in range(a+1)}
    print(d)

if __name__ == "__main__":
    a = int(input('Cuanto numeros quieres que te genere el diccionario?: '))
    b = float(input("Elevado a: "))
    print("""
    ----------
    Imprimiendo lista:
    ----------
    """)
    run(a,b)