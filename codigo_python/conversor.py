menu = """
Bienvenido al conversor de monedas 

1 - Bolivares
2 - Pesos colombianos
3 - Peso argentinos
4 - Peso mexicanos

Elige una opción: """
print("")

opcion = int (input(menu))

if opcion ==1:
    pesos = input("¿Cuantos Bolivares tienes?: ")
    pesos= float(pesos)
    valor_dolar=4.4
    dolares=pesos/valor_dolar
    dolares=round(dolares,2)
    dolares =str(dolares)
    print("Tienes $"+dolares+" dólares")
elif opcion ==2:
    pesos = input("¿Cuantos pesos colombianos tienes?: ")
    pesos= float(pesos)
    valor_dolar=3875
    dolares=pesos/valor_dolar
    dolares=round(dolares,2)
    dolares =str(dolares)
    print("Tienes $"+dolares+" dólares")
elif opcion ==3:
    pesos = input("¿Cuantos pesos argentinos tienes?: ")
    pesos= float(pesos)
    valor_dolar=65
    dolares=pesos/valor_dolar
    dolares=round(dolares,2)
    dolares =str(dolares)
    print("Tienes $"+dolares+" dólares")
elif opcion ==4:
    pesos = input("¿Cuantos pesos mexicanos tienes?: ")
    pesos= float(pesos)
    valor_dolar=24
    dolares=pesos/valor_dolar
    dolares=round(dolares,2)
    dolares =str(dolares)
    print("Tienes $"+dolares+" dólares")
else:
    print(" Ingresa una opción correcta por favor")







