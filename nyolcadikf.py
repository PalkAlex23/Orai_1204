def nyolcadik():
    lista = []
    beFajl = open("fajlok/dal.txt", "r", encoding="utf-8")
    fajlTartalma = beFajl.read()
    beFajl.close()
    # print(fajlTartalma)
    dbk = 0
    dbK = 0
    fajlTartalmaUj = ""
    for index in range(0, len(fajlTartalma), 1):
        if fajlTartalma[index] == "k":
            dbk += 1
            fajlTartalmaUj += "*"
        elif fajlTartalma[index] == "K":
            dbK += 1
            fajlTartalmaUj += "*"
        else:
            fajlTartalmaUj += fajlTartalma[index]
    print(f"Cenzúrázott fájl tartalma: {fajlTartalmaUj}")
    print(f"Kis k betűk száma: {str(dbk)}, nagy K betűk száma: {str(dbK)}")

    # lista kiírás
    kiFajl = open("fajlok/nyolcadik.txt", "w", encoding="utf-8")
    for index in range(0, len(lista), 1):
        print(lista[index], file=kiFajl, end="")
        # kiFajl.write(lista[index])
