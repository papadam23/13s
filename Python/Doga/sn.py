import math
class versenyzo:
    def __init__(self,helyezes,nev,orszag,nyeremeny) -> None:
        self.helyezes=helyezes
        self.nev=nev
        self.orszag=orszag
        self.nyeremeny=nyeremeny
    def __str__(self) -> str:
        return "Név:"+self.nev+ " " "fizetése"+" "+str(self.nyeremeny)

versenyzok=[]

def beolvas():
    f=open("snooker.txt", encoding="UTF8")
    f.readline()
    for sor in f:
        temp=sor.strip().split(';')
        versenyzok.append(versenyzo(int(temp[0]),temp[1],temp[2],int(temp[3])))
    


def f3():
    print(f"3 feladat {len(versenyzok)}")

def f4():
    sum=0
    for item in versenyzok:
        sum+=item.nyeremeny
    print(round(sum/len(versenyzok)),2)

def f5():
    maxsorszam=-1
    max=0
    for i in range(len(versenyzok)):
        if versenyzok[i].orszag=="Kína"and versenyzok[i].nyeremeny>max:
            max=versenyzok[i].nyeremeny
            maxsorszam=i
    print(versenyzok[maxsorszam])

def f6(nemzetiseg):
    i=0
    while i<len(versenyzok) and versenyzok[i].orszag !=nemzetiseg:
        i+=1
    if i<len(versenyzok):
        return True
    else:
        return False

def f62():
    vanE=False
    for item in versenyzok:
        if item.orszag== "Norvégia":
            print("van")
            vanE=True
            break
    if not vanE:
        print("Nincs")
            

def f7(): #halmaz
    halmaz=set([])
    for item in versenyzok:
        halmaz.add(item.orszag)
    for item in halmaz:
        db=szamol(item)
        if db>4:
            print(f"{item}: {db}")
def szamol(orszag):
    db=0
    for item in versenyzok:
        if item.orszag== orszag:
            db+=1
    return db
def f72():
    #kulcs:orszag
    #érték:db: adott orszabbol hany van 
    stat={}
    for item in versenyzok:
        if item.orszag not in stat:
            stat[item.orszag]= 0
        stat[item.orszag]+=1
    for item in stat:
        if stat[item]>4:
            print(F"{item}: {stat[item]}")

beolvas()
f3()
f4()
f5()
vanE=f6("Norvégia")
print(vanE)
f7()
f72()