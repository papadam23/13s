import datetime
class Pilota:
    def __init__(self,nev, szuldatum,nemzetiseg,rajtszam):
        self.nev=nev
        self.szuldatum=szuldatum
        self.nemzetiseg=nemzetiseg
        self.rajtszam=rajtszam

    def __str__(self) -> str:
        return f"{self.nev} {self.szuldatum.date()} {self.nemzetiseg} {self.rajtszam}"
lista=[]

def beolvas():
    f=open("pilotak.csv", encoding="UTF8")
    f.readline()
    for sor in f:
        reszek=sor.strip().split(";")
        nev=reszek[0]
        szuldatum= datetime.datetime.strptime(reszek[1],"%Y.%m.%d")
        nemzetiseg=reszek[2]
        rajtszam=(reszek[3])
        obj=Pilota(nev,szuldatum,nemzetiseg,rajtszam)
        lista.append(obj)
    for item in lista:
        print(item)

def f3():
    print("3.feladat: A listában összesen ", len(lista), "adat van")

    
def f4():
    
    db=0
    for item in lista:
        if db!= len(lista):
            db+=1
    print("4. feladat:",item.nev)

def f5():
    print("5. feladat:")
    for item in lista:
        if item.szuldatum.year<1901:
            print( item.nev, item.szuldatum.date())

def f6():
    kicsi=0
    for item in lista:
        if item.rajtszam!="" and kicsi<item.rajtszam[item]:
            kicsi= item.rajtszam
        print(item.nemzetiseg)


       
        
def f7():
    db=0
    for item in lista:
        if item.rajtszam != "":
            if item.rajtszam== item.rajtszam:
                db=+1
            print(db)



def main():
    beolvas()
    f3()
    f4()
    f5()
    f6()
    #f7()



main()