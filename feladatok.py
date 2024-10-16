import random

def fel_1():
    szam : int = int(input("Adj meg egy páratlan számot: "))
    while(szam%2==0): #páratlan szám--> szam%2==1
        szam : int = int(input("Adj meg egy páratlan számot: "))
    print()

def fel_2():
    i:int = 0
    db:int = 0
    while(i!=7):
        vszam: int = int(random.random()*96) +5
        if(vszam%5==0):
            db+=1
        i+=1
    print(f"A számok között {db}db 5-tel oszható van!")

def fel_3(text:str, betu:str):
    i:int=0
    db:int=0
    while(i<len(text)):
        if(text[i]==betu):
            db+=1
        i+=1    
    print(f"A szövegben {db}db '{betu}' van.")

def fel_4():
    nev:str= input("Adj meg egy nevet, @-al tudsz megállni!: ")
    while(nev!= "@"):
        nev:str= input("Adj meg egy nevet, @-al tudsz megállni!: ")
    print()

def fel_5():
    

   



