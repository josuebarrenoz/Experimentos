import random

is_game = True

def conversacion(mensaje):
  if mensaje == 'piedra':
    return 1
  elif mensaje == 'papel':
    return 2
  elif mensaje == 'tijera':
    return 3
  else:
    return 0

def quien_gano(oponente, usuario):
  if oponente == 1 and usuario == 2:
    return 'YASSSSS GANASTEEEEE 🎉🎉'
  elif oponente == 2 and usuario == 1:
    return 'NOOOO PANAAAA PERDISTEEEE'
  elif oponente == 1 and usuario == 3:
    return 'NOOOO PANAAAA PERDISTEEEE'
  elif oponente == 3 and usuario == 1:
    return 'YASSSSS GANASTEEEEE 🎉🎉'
  elif oponente == 2 and usuario == 3:
    return 'YASSSSS GANASTEEEEE 🎉🎉'
  elif oponente == 3 and usuario == 1:
    return 'NOOOO PANAAAA PERDISTEEEE'
  elif oponente == usuario:
    return 'lol fue un empate equisde'
  elif oponente == 0 or usuario == 0:
    return 'Error watafak ???????'
  else:
    return 'Error???????'

def seguir_jugando(respuesta):
  if respuesta == 'N':
    return False
  elif respuesta != "n":
    return True
  else:
    return False


bienvenida = """ 
B I E N V E N I D O S

            T O D O S . . . 


    AQUÍ SE DESAFÍA...

                  AQUÍ HAY SANGRE...

        LA MUERTE ES INEVITABLE...


      ESTÁS PREPARADO ?

                ENTONCES...


          B I E N V E N I D O... 
                  A . . . 

██████╗ ██╗███████╗██████╗ ██████╗  █████╗ 
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗
██████╔╝██║█████╗  ██║  ██║██████╔╝███████║
██╔═══╝ ██║██╔══╝  ██║  ██║██╔══██╗██╔══██║
██║     ██║███████╗██████╔╝██║  ██║██║  ██║
╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

  ██████╗  █████╗ ██████╗ ███████╗██╗     
  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║     
  ██████╔╝███████║██████╔╝█████╗  ██║     
  ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██║     
  ██║     ██║  ██║██║     ███████╗███████╗
  ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚══════╝

                   ██████╗ 
                  ██╔═══██╗
                  ██║   ██║
                  ██║   ██║
                  ╚██████╔╝

████████╗██╗     ██╗███████╗██████╗  █████╗ 
╚══██╔══╝██║     ██║██╔════╝██╔══██╗██╔══██╗
   ██║   ██║     ██║█████╗  ██████╔╝███████║
   ██║   ██║██   ██║██╔══╝  ██╔══██╗██╔══██║
   ██║   ██║╚█████╔╝███████╗██║  ██║██║  ██║
   ╚═╝   ╚═╝ ╚════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
________________________________________________

            -= PRESIONE START =-

"""

Espacio="""
"""

print(bienvenida)

while is_game:
  oponente = random.randint(1,3)
  print(Espacio)
  usuario = conversacion(input('Piedra, papel o tijera: '))
  print(Espacio)
  print(quien_gano(oponente, usuario))
  print(Espacio)
  is_game = seguir_jugando(input('Quieres seguir jugando? (S/N) ')) 
