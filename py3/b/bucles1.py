def cont(v1,v2):
    if v1<v2+1:
        print("2 elevado a "+str(v1)+ " es igual a: "+str(2**v1))     
        cont(v1+1,v2)
    else:
        print("Fin!")


if __name__ == "__main__":
    v2 = int(input("Cuantas potencias de dos quieres calcular: "))
    v1=0
    cont(v1,v2)