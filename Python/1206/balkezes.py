import datetime
class Balkezes:
    def __init__(self,nev,elso,utolso,suly,magassag):
        self.nev=nev
        self.elso=elso
        self.utolso=utolso
        self.suly=suly
        self.magassag=magassag

    def __str__(self) -> str:
        return f"{self.nev} {self.elso.date()} { self.utolso.date()} {self.suly} {self.magassag}"

lista=[]

def beolvas():
    f=open("balkezesek.csv" , encoding="UTF8")
    f.readline()
    for sor in f:
        reszek=sor.strip().split(";")
        nev=reszek[0]
        elso=datetime.datetime.strptime(reszek[1],"%Y-%m-%d")
        utolso=datetime.datetime.strptime(reszek[2],"%Y-%m-%d")
        suly=int(reszek[3])
        magassag=int(reszek[4])
        obj=Balkezes(nev,elso,utolso,suly,magassag)
        lista.append(obj)

    for item in lista:
        print(item)

def f3():
    print("Összesen ",len(lista),"sor van az állományban")


def f4():
    for item in lista:        
        if item.utolso.year== 1999 and item.utolso.month== 10:           
            print( item.nev,  round(item.magassag*2.54,1) ,"cm")
            
        


def f5():
    beker=int(input())
    
    jó=False
    while jó==False:

        if beker > 1990 and beker < 2000:
            jó=True
            print(beker)
        else:
            print("Hibás adat! Egy számot kérek 1990 és 1999 között")
            beker=int(input("Kérek egy számot 1990-1999 között"))

def f6():
    ossz=0
    db=0
    for item in lista:
        if item.utolso.year==1995:
            db+=1
            ossz+=item.magassag
    print(round(ossz/db,2,"font"))


def main():
    beolvas()
    f3()
    f4()
    f5()
    f6()
    
main()
