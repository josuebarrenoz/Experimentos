import requests
# import time

def progress_bar(part, total, length =30):
    frac = part/total
    completed = int(frac*length)
    missing = length - completed
    bar = f"[{'#'*completed}{'-'*missing}]{frac:.2%}"
    return bar

def menu():
    print("""
    -------------------------------------------------------
    |            Bienvenido a list of stocks              |
    |     El archivo que se genera tiene de nombre:       |
    |               "list_of_stocks.csv"                  |
    -------------------------------------------------------
    """)

def run ():
    menu()
    f = open ("list_of_stocks.csv","a")
    b=0
    url = requests.get("https://financialmodelingprep.com/api/v3/stock/list?apikey=2fbdd3ee1ee8a21c305963e59f11fbe2").json()
    for i in url:
        if i["exchangeShortName"] == "NYSE" and i["type"] == "stock":
            a = i["symbol"]
            c = i["name"]
            d = i["price"]
            print(f"#{b+1}; {a}; {c}; {d}",file = f)
        b+=1
        print("    "+progress_bar(b,int(len(url)),45), end='\r')

    print("""

    ------------------------------------------------------
    |             Ha finalizado el Programa              |
    |       Busca tu archivo para que lo consultes.      |
    |                                                    |
    |Hecho por @josuebarrenoz.                           |
    ------------------------------------------------------
    """)
    f.close()


if __name__ == "__main__":
    run()
