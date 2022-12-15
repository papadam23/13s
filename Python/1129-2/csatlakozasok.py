import datetime
class Csatlakozas:
    def __init__(self, orszag, datum):
        self.orszag=orszag
        self.datum=datum

    def __str__(self) -> str:
        return f"{self.orszag}{ self.datum.date()}"

lista=[]

def beolvas():
    f=open("csatlakozasok.txt", encoding="UTF8")
    for sor in f:
        reszek=sor.strip().split(";")
        orszag=reszek[0]
        datum= datetime.datetime.strptime(reszek[1],"%Y.%m.%d")
        obj=Csatlakozas(orszag,datum)
        lista.append(obj)

    for item in lista:
        print(item)


def f3():

    print(f"3 feladat Eu tagállamok száma 2018-ban: {len(lista)}")

def f4(ev):
    db=0
    for item in lista:
        if item.datum.year== ev:
            db+=1
    print("4. feladat", ev,"ben ", db," orszag csatlakozott")


def f5(orszag):
    i=0
    while lista[i].orszag !=orszag:
        i+=1
    print("5.feladat: ", orszag ," csatlakozásánaka dátuma:", lista[i].datum)


def f6():
    i=0
    while i<len(lista) and lista[i].datum.month != 5:
        i+=1

    if i<len(lista):
        print("6. feladat: Igen volt Májusban csatlakozás")
    else:
        print("Nem volt")


def f7():
    max= lista[0]
    for item in lista:
        if max.datum < item.datum:
            max=item

    print("7. feladat: A legkésőbb csatlakozott ország:", max.orszag)


def f8():
    stat={}
    for item in lista:
        kulcs=item.datum.year
        if kulcs not  in stat:
            stat[kulcs]=0
        stat[kulcs]+=1
    for item in stat:
        print(item,":" , stat[item])




def main():
    beolvas()
    f3()
    f4(2007)
    f5("Magyarország")
    f6()
    f7()
    f8()










main()