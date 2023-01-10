class Kemia:
    def __init__(self,ev,elem,vegyjel,rendszam,felfedezo):
        self.ev=ev
        self.elem=elem
        self.vegyjel=vegyjel
        self.rendszam=rendszam
        self.felfedezo=felfedezo

def __str__(self) -> str:
    return f"{self.ev} {self.elem} {self.vegyjel} {self.rendszam} {self.felfedezo}"
lista=[]


def beolvas():
    f=open("felfedezesek.csv", encoding="UTF8")
    f.readline()
    for sor in f:
        reszek=sor.strip().split(";")
        if reszek[0]=="Ókor":
            ev=reszek[0]
        else:
            ev=int(reszek[0])
        elem=reszek[1]
        vegyjel=reszek[2]
        rendszam=reszek[3]
        felfedezo=reszek[4]
        obj=Kemia(ev,elem,vegyjel,rendszam,felfedezo)
        lista.append(obj)
    
  
        
def f3():
    print("3. feladat: Elemek száma:",len(lista))

def f4():
    db=0
    for item in lista:
        if item.ev =="Ókor":
            db+=1
    print("4. feladat: Felfedezések az ókorban:"  ,db)

def f5():
    jo=False
    beker= input("Kérek egy vegyjelet")
    while jo:
        if len(beker)==2 or len(beker)==1 and beker.isalpha():
            jo=True
    else:
        while jo:
            print("Nem jó")
            beker= input("Kérek egy vegyjelet")
    

def f7():
    for item in lista:
        if item.ev!="Ókor" and item.ev[item]-item.ev[item+1]>=200:
            print(item.ev)




def main():
    beolvas()
    f3()
    f4()
    f5()
    f7()


main()