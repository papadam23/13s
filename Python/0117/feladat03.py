class Korcsolya:
    def __init__(self,nev,orszag,Technikai,Komponens,levonas) -> None:
        self.nev=nev
        self.orszag=orszag
        self.Technikai=Technikai
        self.Komponens=Komponens
        self.levonas=levonas

    def __str__(self) -> str:
        return f"{self.nev} {self.orszag} {self.Technikai} {self.Komponens} {self.levonas}"
    
lista=[]

def beolvas():
    f=open("korcsolya.csv", encoding="UTF8")
    f.readline()
    for sor in f:
        reszek=sor.strip().split(";")
        nev=reszek[0]
        orszag=reszek[1]
        Technikai=float(reszek[2])
        Komponens=float(reszek[3])
        levonas=float(reszek[3])
        obj=Korcsolya(nev,orszag,Technikai,Komponens,levonas)
        lista.append(obj)
    
    for item in lista:
        print(item)
    f.close()
        
def f2():
    print("3.feladat: ",len(lista),"résztvevő van ")

def f3():
    db=0
    for item in lista:
        if item.orszag=="HUN":
           db+=1
    if db==1:
        print("Van magyar versenyző")
    else:
        print("Nincs")

def f4():
    db=0
    for item in lista:
        if item.Technikai>1000 or item.Komponens>1000:
            db+=1
    print("Olyan versenyzők akiknek a pontszáma nem kiszámítható:",db)


def f5(nev):
    for item in lista:
        if item.nev==nev:
            if item.Technikai<1000 and item.Komponens<1000:
                pontszam= item.Technikai + item.Komponens - item.levonas
                return round(pontszam,2)
            else:
                return 0
        

def f6():
    f=open("tokeletesek.txt" ,"w", encoding="UTF8")
    for item in lista:
        if item.Technikai<1000 and item.Komponens<1000:
            pontszam= item.Technikai + item.Komponens - item.levonas
            f.write(f"{item.nev}:{round(pontszam,2)}\n")
    
    f.close()


def main():
    beolvas()
    f2()
    f3()
    f4()
    print(f5(input("Kérek egy nevet")))
    f6()





main()