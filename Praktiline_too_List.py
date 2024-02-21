from random import *
from string import *
from time import sleep
#1v for
for i in range(100): #i=0..99
    sym=i*"#"
    print(sym)
    sleep(random())
    
print()

lst = []
v = int(input("Kui palju numbreid te nimekirjas soovite?"))
for i in range(v):
    v = int(input("Arv: "))
    sleep(1)
    lst.append(v)
suur = 0
for el in lst:
    if el > suur:
        suur = el
lst[lst.index(suur)] = suur / len(lst)
print(f"suur {suur}, indeks on {lst.index(suur) + 1}\n{lst}")

#11

#2v sort
lst = []
v = int(input("Kui palju numbreid te nimekirjas soovite?"))
for i in range(v):
    v = int(input("Arv: "))
    lst.append(v)
lst.sort()
suur = lst[-1]

lst[lst.index(suur)] = suur / len(lst)
print(f"suur {suur}, indeks on {lst.index(lst[-1]) + 1}\n{lst}")





numbers = input("Введите числа через пробел: ").split()
numbers = list(map(int, numbers))
if not numbers:
    print("Ошибка: список чисел пуст.")
else:
    max_number = max(numbers)
numbers[numbers.index(max_number)] = max_number / len(numbers)
print("Список после замены:", numbers)





#6 
nimekirja=[]
n=int(input("Nimekirja suurus: "))
for i in range(n):
    arv=randint(10,100)
    nimekirja.append(arv)
print(nimekirja)
maksimum=max(nimekirja)
vajavarv=maksimum/len(nimekirja)
nimekirja[nimekirja.index(maksimum)]=vajavarv
print(nimekirja)

nimekirja1=[]
nimekirja=[]
n=int(input("Nimekirja suurus: "))
for i in range(n):
    arv=randint(10,100)
    nimekirja1.append(arv)
    nimekirja.append(arv)
maksimum=nimekirja[0]
for arv in nimekirja:
    if arv>maksimum:
        maksimum=arv
vajavarv=maksimum/len(nimekirja)
for i in range(len(nimekirja)):
    if nimekirja[i]==maksimum:
        nimekirja[i]=vajavarv
print(nimekirja1)
print(nimekirja)


#5 Vahetus
rida=[]
N=randint(2,25)
for i in range(N):
    rida.append(choice(ascii_uppercase))
print(rida)
kogus=int(input("Mitu elemendi vahetame oma vahel "))
if len(rida)//2>=kogus:
    for i in range(kogus):
        a=rida[i]
        rida[i]=rida[len(rida)-i-1]
        rida[len(rida)-1-i]=a
print(rida)



#4 Indeksid
Indeksid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
while True:
    while True:
        try:
            indeks=int(input("Sisesta viienumbriline indeks: "))#10000,15478,98564
            #if 10000<=indeks<=99999:
            indeks_elemendide_arv=len(str(indeks))
            if indeks_elemendide_arv==5:
                print("5numbriline indeks ")
                break
            else:
                print("On vaja 5numbriline arv(indeks)")
        except:
            print("Vale andmetüüp!")
    arv1=indeks//10000
    print(arv1)
    #symbolid=list(str(indeks))
    print(f"Sa elad piirkonnas {Indeksid[arv1-1]}")


#3

arvud=[]
N=int(input("Mitu rida joonistame? "))
S=input("Sisesta sümbol: ")
#loendi täitmine
for p in range(N):
    arvud.append(randint(1,100))
#diagrammi loomine
for p in range(N):
    print(arvud[p]*S)




#2
#nimed=[]
#for i in range(5):
#    while True:
#        nimi=input(i+1,". Sisesta nimi: ").capitalize()
#        if nimi not in nimed:
#            nimed.append(nimi)
#            break
#        else:
#            print("Sisesta  veel kord:")

#print("Loetelu oli: ",nimed)
#nimed.sort()
#print("Loetelu sorteeritud: ",nimed)
#for n in range(len(nimed)):
#    print(n+1,". ",nimed[n],sep="")
#print("Vimasena oli lisatud: ",nimi)
##dublikatid
#uued_nimed=[]
#for nimi in nimed:
#    if nimi not in uued_nimed:
#        uued_nimed.append(nimi)
#print(uued_nimed)
##dublikatid 2
#uued_nimed=list(set(nimed))
##2.3
#vanused=[]
#for i in range(5):
#    vanus=int(input("Sisesta vanus: "))
#    vanused.append(vanus) #
#maksimum=max(vanused)
#minimum=min(vanused)
#summa=sum(vanused)
#keskmine=summa/len(vanused)
##Kuva ekraanile nimi koos vanusega
#for i in range(5):
#    print(nimed[i],"on ", vanused[i],"aastat vana")






#1
vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
konsonanti="qwrtpsdfghklzxcvbnmj"
markid=punctuation
v=k=m=t=0
tekst=input("Sisesta sõna või lause: ").lower() #"ABCD"->"abcd!"
tekst_list=list(tekst) #["a","b","c","d","!"]
for sümbol in tekst_list:
    if sümbol in vokaali:
        v+=1
    elif sümbol in konsonanti:
        k+=1
    elif sümbol in markid:
        m+=1
    elif sümbol==" ":
        t+=1
print("Vokaali:",v,"\nKonsonanti:",k)
print("Kirjuvahemärgid:",m)
print("Tühikud:",t)