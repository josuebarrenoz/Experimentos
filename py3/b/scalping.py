import random

def menu():
    print("""
    -----------------------------------
    |Bienvenido al programa de scalping|
    -----------------------------------
    """)


def seguir(b):
    if b == 'N' or "n":
        return False
    elif b== "S" or "s":
        return True
    else:
        print("Escibre una opción valida")
        print(" ")
        seguir(b)


def run(v1,v2):
    m = 100
    c = 0
    while  150 > m > 50:
        comienza = random.randint(0, 1)
        if comienza == 0:
             m=m*(1+(v1/100))
             c+=1
        else:
            m=m*(1-(v2/100))
            c+=1
    m-=100
    print ("Se obtuvo un rendimiento del "+str(round(m,2))+"% en "+str(c)+" trades")


if __name__ == '__main__':
    menu()
    p = float(input("Ingrese porcentaje de ganancia en cada trade: "))
    n = float(input("Ingrese porcentaje de perdida en cada trade: "))
    while True:
        run(p,n)
        continuar = input('Desea continuar? S / N :')
        if continuar.lower() in "s si y yes":
            continue
        else:
            break