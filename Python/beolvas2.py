def beolvas():
    f=open("emberek.txt", encoding="UTF8")
    global nevek
    global fizuk
    nevek=[]
    fizuk=[]
    for item in f:
        nev=item.split(";")[0]
        nevek.append(nev)
        fizuk.append(int(item.split(";")[1]))


def kiir(lista):
    for item in lista:
        print(item)

def kiir2(nevek,fizuk):
    for i in range(len(nevek)):
        print(f"név:{nevek[i]}, fizu:{fizuk[i]} ")

def iras():
    f=open("fizetesek.txt","w", encoding="UTF8")
    for i in range(len(nevek)):
        f.write(f"név:{nevek[i]}, fizu:{fizuk[i]} \n")

def main():

    beolvas()
    iras()

main()