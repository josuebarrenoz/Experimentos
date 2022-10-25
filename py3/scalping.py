import random

def menu():
    print("""
    -----------------------------------
    |Bienvenido al programa de scalping|
    -----------------------------------
    """)

def progress_bar(part, total, length =30):
    frac = part/total
    completed = int(frac*length)
    missing = length - completed
    bar = f"[{'#'*completed}{'-'*missing}]{frac:.2%}"
    return bar

def calc(v1,v2):
    m = 100
    c = 0
    while  200 > m > 50:
        comienza = random.randint(0, 1)
        if comienza == 0:
             m=m*(1+(v1/100))
             c+=1
        else:
            m=m*(1-(v2/100))
            c+=1
    m-=100
    # print ("Se obtuvo un rendimiento del "+str(round(m,2))+"% en "+str(c)+" trades",end ="\r")
    return m

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
    p = float(input("Ingrese porcentaje de ganancia en cada trade: "))
    n = float(input("Ingrese porcentaje de perdida en cada trade: "))
    d = int(input("Ingrese cuantas repeticiones quiere: "))
    c1 = 0
    c2 = 0

    for i in range (0,d):
        m = calc(p,n)
        if m > 0:
            c1+=1
        else:
            c2+=1
        print(progress_bar(i,d), end='\r')
    print(f"De las {d} repeticiones hubo {c1} trades ganadores y {c2} trades perdedores")
    repit()


if __name__ == '__main__':
    menu()
    run()
