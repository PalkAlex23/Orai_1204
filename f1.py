def osztalybeir():
    kiFajl = open("fajlok/proba.txt", "a", encoding="utf-8")
    kiFajl.write("\nSZF/13B")
    kiFajl.close()

def kiir():
    # teljes fájl beolvasás
    beFajl = open("fajlok/proba.txt", "r", encoding="utf-8")
    adatok = beFajl.read()
    print(adatok)
    beFajl.close()

    beFajl = open("fajlok/proba.txt", "r", encoding="utf-8")
    beFajl.readline()
    print(beFajl.readline())
    beFajl.close()

    # első 5 karakter
    beFajl = open("fajlok/proba.txt", "r", encoding="utf-8")
    elso5 = beFajl.read(5)
    print(elso5)
    beFajl.close()
