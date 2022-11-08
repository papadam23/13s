class Tanar:
    nev=""
    tárgy=""
    osztaly=""
    oraszam=0


def beolvas():
    global tanarok
    f=open("beosztas.txt", encoding="UTF8")
    tanarok=[]
    while True:
        sor=f.readline().strip()
        if not sor:
            break
        else:
            ember=Tanar()
            ember.nev=sor
            ember.tárgy= f.readline().strip()
            ember.osztaly= f.readline().strip()
            ember.oraszam= int(f.readline().strip())
            tanarok.append(ember)
    f.close()
def f1():
    print(len(tanarok))

def f2():
    osszeg=0
    for item in tanarok:
        osszeg+=item.oraszam
    return osszeg



def f3():
    osszeg=0
    tanarnev=input("Add meg a tanár nevét")
    for item in tanarok:
        if item.nev==tanarnev:
            osszeg+=item.oraszam
    return osszeg



def main():
    beolvas()
    print(tanarok[7].nev)
    f1()
    print(f2())
    print(f3())

main()


