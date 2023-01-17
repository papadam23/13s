def f1():
    beker=int(input("Kérem a termék árát!"))
    beker1=int(input("Kérem a termék éves eladott mennyiségét!"))

    havi=beker/12
    print(round(havi,2),"Ft")
    if havi>= 35000:
        print("Nyereséges volt a termék")
    else:
        print("Nem volt nyereséges a termék")

lista=[]
def f2():
   
    f = open("elemek.txt", "r", encoding="UTF8")
    for item in f:
       lista.append(item.strip("\n"))

    print(lista)

    print(len(lista),"elem van a listában ")
    db=0
    while db!= len(lista):
        db+=1
    else:
        print(item)

def f23(kereses):
    
    if kereses in lista:
        True
    else:
        return False
    
beker2=input("Kérek egy elemet!")

        

        
    
def main():
    #f1()
    #f2()
    f23()





main()
