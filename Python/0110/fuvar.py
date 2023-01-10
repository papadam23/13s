import datetime
class Fuvar:
    def __init__(self,taxi_id,indulas,idotartam,tavolsag,viteldij,borravalo,fizetes_modja):
        self.taxi_id=taxi_id
        self.indulas=indulas
        self.idotartam=idotartam
        self.tavolsag=tavolsag
        self.viteldij=viteldij
        self.borravalo=borravalo
        self.fizetes_modja=fizetes_modja
    def __str__(self) -> str:
        return f"{self.taxi_id} {self.indulas.date()} {self.idotartam} {self.tavolsag} {self.viteldij} {self.borravalo} {self.fizetes_modja}"
lista=[]

def beolvas():
    f=open("fuvar.csv", encoding="UTF8")
    f.readline()
    for sor in f:
        reszek=sor.strip().split(";")
        taxi_id=int(reszek[0])
        indulas= datetime.datetime.strptime(reszek[1], "%Y-%m-%d %H:%M:%S")
        idotartam=int(reszek[2])
        tavolsag=float(reszek[3].replace(",","."))
        viteldij=float(reszek[4].replace(",","."))
        borravalo=float(reszek[5].replace(",","."))
        fizetes_modja=reszek[6]
        obj=Fuvar(taxi_id,indulas,idotartam,tavolsag,viteldij,borravalo,fizetes_modja)
        lista.append(obj)
    
def f3():
    print("3.feladat:",len(lista),"utazásra került sor")


def f4():
    db=0
    bevetel=0
    for item in lista:
        if item.taxi_id == 6185:
            bevetel=item.viteldij+item.borravalo+bevetel
            db+=1
      
            
    print("4.feladat",db,"fuvar alatt ", bevetel,"$")

def f5():
     stat={}
     for item in lista:
        kulcs=item.fizetes_modja
        if kulcs not  in stat:
            stat[kulcs]=0
        stat[kulcs]+=1
     print("5.feladat:")
     for item in stat:
        print("\t",item,":" , stat[item])

def f6():
    tav=0
    for item in lista:
        tav=item.tavolsag+tav
    tav=tav*1.6
    print("6.feladat:",round(tav,2),"km")



def main():
    beolvas()
    f3()
    f4()
    f5()
    f6()

main()