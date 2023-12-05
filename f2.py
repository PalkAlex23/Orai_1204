def osztalybeir():
    kiFajl = open("fajlok/felad2.txt", "a", encoding="utf-8")
    kiFajl.write("\nrajzolás")
    kiFajl.close()

def aFeladat():
    beFajl = kiFajl = open("fajlok/felad2.txt", "r", encoding="utf-8")
    beFajl.readline()
    print(beFajl.readline())
    beFajl.close()

def bFeladat():
    beFajl = kiFajl = open("fajlok/felad2.txt", "r", encoding="utf-8")
    adatok = beFajl.read()
    print(adatok)
    beFajl.close()
