#2

nimed=[]
for i in range(5):
    nimi=input("Sisesta nimi: ").capitalize()
    nimed.append(nimi)

print("Loetelu oli: ",nimed)
nimed.sort()
print("Loetelu sorteeritud: ",nimed)
for n in range(len(nimed)):
    print(n+1,".",nimed[n],sep="")
















from string import *
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