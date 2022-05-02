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

def exchanges(moneda,cantidad):
    result = 0
    # Moneda venezolana
    if moneda == 1:
        result = round (cantidad / valor_dolar1,2)
        result1 = round(cantidad / valor_euro1,2)
        result2 = round(cantidad / valor_btc1,9)
        print(f' ')
        print(f'Los {cantidad} Bolivares equivalen a:')
        print(f' ')
        print(f'{result} dolares')
        print(f'{result1} euros')
        print(f'{result2} bitcoin')
    # Moneda colombiana
    elif moneda == 2:
        result = round (cantidad / valor_dolar2,2)
        result1 = round(cantidad / valor_euro2,2)
        result2 = round(cantidad / valor_btc2,9)
        print(f' ')
        print(f'Los {cantidad} pesos colombianos equivalen a:')
        print(f' ')
        print(f'{result} dolares')
        print(f'{result1} euros')
        print(f'{result2} bitcoin')
    # Moneda Argentina
    elif moneda == 3:
        result = round (cantidad / valor_dolar3,2)
        result1 = round(cantidad / valor_euro3,2)
        result2 = round(cantidad / valor_btc3,9)
        print(f' ')
        print(f'Los {cantidad} pesos argentinos equivalen a:')
        print(f' ')
        print(f'{result} dolares')
        print(f'{result1} euros')
        print(f'{result2} bitcoin')
    # Moneda mexicana
    elif moneda == 4:
        result = round (cantidad / valor_dolar4,2)
        result1 = round(cantidad / valor_euro4,2)
        result2 = round(cantidad / valor_btc4,9)
        print(f' ')
        print(f'Los {cantidad} pesos mexicanos equivalen a:')
        print(f' ')
        print(f'{result} dolares')
        print(f'{result1} euros')
        print(f'{result2} bitcoin')
    # Otro
    else:
        print(f' ')
        print('Ingresa solo un numero de la lista')


if __name__ == '__main__':
    try:
        moneda = int(input('''
        Ingresa el indice de la moneda que quieres convertir a  dolares, euros o bitcoin:
            [1] Moneda venezolana
            [2] Moneda colombiana 
            [3] Moneda argentida 
            [4] Moneda mexicana 
        Selecciona: '''))
        print('********************************')
        cantidad = int(input('Ingresa la cantidad que quieres convertir: '))
        exchanges(moneda,cantidad)
    except:
        print(f' ')
        print('* * * * * * E R R O R * * * * * *')
        print('Por favor, Ingresa solo valores numericos')