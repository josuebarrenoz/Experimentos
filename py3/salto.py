def inicio():
    print("""
    -------------------------------------------
    |Bienvenido al programa de saltos de linea|
    -------------------------------------------
    
    """)


def final():
    print("""
    
    -----------------------------------------
    |  Muchas gracias por usar el programa  |
    |    Contactame por @josuebarrenoz en   |
    |Github, Telegram y otras redes sociales|
    -----------------------------------------
    """)
    
    
def run():
    inicio();
    archivo = str(input("Escribe el nombre del archivo con su extension: "));
    ruta = f"/home/wade/proy/experimentos/py3{archivo}";
    with open(ruta, 'r', encoding="utf8") as f:
        lines = f.readlines()

    #lines = [line.replace(r'\n', ' ').replace(r' ', ' ') for line in lines];
    #print(lines);
    #lines = lines.rstrip()
     
    lines = [line.replace("\n", " ") for line in lines];
    s = "".join(lines);
    
    with open(r'Resultados.txt', 'w', encoding="utf8") as f:
        f.writelines(s)
    
    final();

if __name__ == "__main__":
    run()
