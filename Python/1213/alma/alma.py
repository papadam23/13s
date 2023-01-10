import math


def alma():

    
    beker= int(input("Kérek egy egész számot"))
    if beker<200 or beker==200:
        láda= beker/20
        print(math.ceil(láda),"Láda kell az almáknak")
        print("Elég a 10 láda az almáknak")
   
    else:
        láda= beker/20
        print(math.ceil(láda),"Láda kell az almáknakj")

def f2():
    db=0
    dbszó=0
    
    beker= int(input("Kérek egy egész számot"))
    lista=[]
    while True:
        if db!=beker:
            bekerszó=input("Kérek szavakat:  ")
            lista.append(bekerszó+"\n")
            db+=1
        else:
            break
    van =False
    for i in range(db):
            if len(lista[i])==3: 
               van=True
    if van :
        print("Van benne 3 betűs")
        van=False
    for i in range(db):
        if len(lista[i])>=5:
            dbszó+=1
            
    print(dbszó, "db 5 betűs szó van a listában")
    f= open("szavak.txt", "w")
    f.writelines(lista)
    f.close
      



def main():
    #alma()
    f2()


main()

