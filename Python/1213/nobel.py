
class Nobel:
    def __init__(self,evszam,típus,keresztnev,vezeteknev):
        self.evszam=evszam
        self.típus=típus
        self.keresztnev=keresztnev
        self.vezeteknev=vezeteknev

    def __str__(self) -> str:
         return f"{self.evszam} {self.típus} { self.keresztnev} {self.vezeteknev} "
    
lista=[]

def beolvas():
    f=open("nobel.csv" , encoding="UTF8")
    f.readline()
    for sor in f:
        reszek=sor.strip().split(";")
        evszam=reszek[0]
        típus=reszek[1]
        keresztnev=reszek[2]
        vezeteknev=reszek[3]
        obj=Nobel(evszam,típus,keresztnev,vezeteknev)
        lista.append(obj)

    for item in lista:
        print(item)

def f3():
    for item in lista:
        if item.keresztnev== "Arthur B." and item.vezeteknev=="McDonald":
            print( "3. feladat: ", item.típus)

def f4():
    for item in lista:
        if item.evszam=="2017" and item.típus=="irodalmi":
            print("4. feladat: ",item.keresztnev, item.vezeteknev)

def f5():
    print("5. feladat: ")
    for item in lista:
        if item.evszam>= "1990" and  item.vezeteknev=="":
            print( item.evszam,item.keresztnev)

def f6():
    print("6.feladat: ")
    név="Curie"
    for item in lista:
        if név in item.vezeteknev:
                print(item.evszam,":" , item.keresztnev, item.vezeteknev, "(", item.típus,")")

def f7():
    print("7. feladat:")
    fizikai=0
    kémiai=0
    orvosi=0
    irodalmi=0
    béke=0
    közgazdaságtani=0
    for item in lista:
        if item.típus=="fizikai":
            fizikai+=1
        if item.típus=="kémiai":
            kémiai+=1
        if item.típus=="orvosi":
            orvosi+=1
        if item.típus=="irodalmi":
            irodalmi+=1
        if item.típus=="béke":
            béke+=1
        if item.típus=="közgazdaságtani":
            közgazdaságtani+=1
    print("Fizikai\t\t\t",fizikai ,"\nKémiai\t\t\t",kémiai,"\nOrvosi\t\t\t",orvosi,"\nIrodalmi\t\t",irodalmi,"\nBéke\t\t\t",béke,"\nKözgazdaságtani\t\t",közgazdaságtani)
    
    stat = {}
    for item in lista:
        kulcs = item.típus
        if kulcs not in stat:
            stat[kulcs]=0
        stat[kulcs]+=1
    for item in stat:  #item: kulcs
        print(f"{item:25} {stat[item]:6}")


def f8():
    f=open("orvosi.txt", "w" ,encoding="UTF8")
    for item in lista:
        if item.típus=="orvosi":
            f.writelines([item.evszam,": ", item.keresztnev," ",item.vezeteknev," ","\n"])
    f.close()

def main():
    beolvas()
    f3()
    f4()
    f5()
    f6()
    f7()
    f8()
main()
