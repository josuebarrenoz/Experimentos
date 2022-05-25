def conversor(tipo_pesos,valor_dolar):
    pesos = input("¿Cuantos "  + tipo_pesos + " tienes?: ")
    pesos= float(pesos)
    dolares=pesos/valor_dolar
    dolares=round(dolares,2)
    dolares =str(dolares)
    print("Tienes $ "+dolares+" dólares")

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
    conversor("Bolivares",4.4)
elif opcion ==2:
    conversor("pesos colombianos",3875)
elif opcion ==3:
    conversor("pesos argentinos",65)    
elif opcion ==4:
    conversor("pesos mexicanos",24)
else:
    print(" Ingresa una opción correcta por favor")



