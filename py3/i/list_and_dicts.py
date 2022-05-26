def run():
    my_list = [1,"Hello",True,4.5]
    my_dict = {"firstname: Josue","lastname: Barreno"}
    super_list = [
        {"firstname: Facundo","lastname: García"}, {"firstname: Miguel","lastname: Torres"}, {"firstname: Pepe","lastname: Rodelo"}, {"firstname: Susana","lastname: Martinez"}, {"firstname: Jose","lastname: Garcia"},
    ]
    super_dict = {
        "natural_nums": [1,2,3,4,5,6,7,8,9,10],
        "integer_nums": [-5,-4,-3,-2,-1,0,1,2,3,4,5],
        "floating_nums": [1.1,4.5,6.43]
    }

    print("--------------------------------")
    print("--------------------------------")
    for key, value in super_dict.items():
        print(key, " - ",value)

    print("--------------------------------")
    print("--------------------------------")
    for i in super_list:
        print(i)

    print("--------------------------------")
    print("--------------------------------")

if __name__ == '__main__':
    run()