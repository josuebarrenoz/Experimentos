menu = """Bienvenido al conversor de monedas

Ingresa el indice de la moneda que quieres convertir a  dolares, euros o bitcoin:
            
            [1] Moneda venezolana
            [2] Moneda colombiana 
            [3] Moneda argentida 
            [4] Moneda mexicana 

Selecciona: """


is_game = True


#Declaracion de valores
valor_dolar1 = 4.48071
valor_euro1 = 4.72458
valor_btc1 = 174133.833
valor_dolar2 = 3958
valor_euro2 = 4165.18
valor_btc2 = 153673703.8
valor_dolar3 = 115.32
valor_euro3 = 121.37
valor_btc3 = 4477406.44
valor_dolar4 = 20.4
valor_euro4 = 21.47
valor_btc4 = 792178.24


def seguir_jugando(respuesta):
  if respuesta == 'N':
    return False
  elif respuesta != "n":
    return True
  else:
    return False


def codigo(opcion):
    if opcion ==1:
        return conversor("Bolivares",valor_dolar1,valor_euro1,valor_btc1)
    elif opcion ==2:
        return conversor("pesos colombianos",valor_dolar2,valor_euro2,valor_btc2)
    elif opcion ==3:
        return conversor("pesos argentinos",valor_dolar3,valor_euro3,valor_btc3)    
    elif opcion ==4:
        return conversor("pesos mexicanos",valor_dolar4,valor_euro4,valor_btc4)
    else:
        print(f' ')
        print('* * * * * * E R R O R * * * * * *')
        print('Por favor, Ingresa solo valores validos')


def conversor(tipo_pesos,valor_dolar,valor_euro,valor_btc):
    print(f' ')
    print('*****************************************')
    cantidad = float(input("""Ingresa la cantidad que quieres convertir: """))
    print('*****************************************')
    result1 = round(cantidad / valor_dolar,2)
    result2 = round(cantidad / valor_euro,2)
    result3 = round(cantidad / valor_btc,9)
    print(f' ')
    print(f'Los {cantidad} {tipo_pesos} equivalen a:')
    print(f' ')
    print(f'{result1} dolares')
    print(f'{result2} euros')
    print(f'{result3} bitcoin')
    print(f' ')
    print('*****************************************')
    print(f' ')


if __name__ == '__main__':
    while is_game:
        opcion = int(input(menu))
        codigo(opcion)
        is_game = seguir_jugando(input("""Quieres seguir? (S/N): """))
else:
    print(f' ')
    print('* * * * * * E R R O R * * * * * *')
    print('Por favor, Ingresa solo valores numericos')

 

















