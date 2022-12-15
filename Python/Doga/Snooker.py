class snooker:
    helyezes=""
    nev=""
    orszag=""
    nyeremeny=""


def beolvas():
    f=open("snooker.txt", encoding="UTF8")
    global snookerv
    snookerv=[]
    
    
    for sor in f:
        snok=snooker()
        helyezes=snok.helyezes=int=(sor.split(";")[0])
        nev=snok.nev=sor.split(";")[1]
        orszag=snok.orszag=sor.split(";")[2]
        nyeremeny=snok.nyeremeny=int=(sor.split(";")[3])
        snookerv.append(snok)
    f.close()
def f2():
    print(snookerv)

def f3():
    print("3.feladat: A világranglistán" ,len(snookerv)-1,"versenyző szerepel")
def f4():
    atlag=0
    
    for sor in snookerv:
        atlag +=sor.nyeremeny
    print(atlag/len(snookerv))

def f6():
    van=False
    





def main():
    beolvas()
    f2()
    f3()
    print(f4())

main()
    




   
    






