import datetime

def teszt():
    mai=datetime.datetime.now()
    
    print(f"{mai.year} {mai.month} {mai.day}")
    tegnap= datetime.datetime(2022,11,28)
    print(tegnap)
    if mai.year == tegnap.year:
        print("egy évben van")
    if mai>tegnap:
        print("ja")


    datum="2022.10.10"
    d1= datetime.datetime.strptime( datum,"%Y.%m.%d")
    print(d1)




def main():
    teszt()

main()