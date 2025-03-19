
from datetime import *
from random import *
#14
#maht=int(input("Bussi maht: "))
#i=int(input("Inimeste arv: "))
#ba=round(i/maht) #2,3->2
#if i%maht!=0:
#    ba+=1
#vb=i%maht
#print("Kokku on vaja {0} bussi ja viimasel sõidavad {1} inimest".format(ba,vb))



#11
# from colorama import *
# init(autoreset = True)
# print(Fore.GREEN+Back.BLUE+'Juubel või ei ole')
# print('Juubel või ei ole')
# ta=date.today().year
# sp=date(int(input("Sünniaasta: ")),int(input("Sünnikuu: ")),int(input("Sünnipäev: "))).year
# if (ta-sp)%5==0:
#     print(Fore.GREEN+"Juubel")
# else:
#     print(Back.BLUE+"Tavaline sünnipäev")

#8.2 Poes
arve_nr= date.today()#datetime.now()
print(arve_nr)
tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0
for toode in ["Piim","Leib","Komm"]:
    hind=randint(50,150)/100
    v=input("Toode: "+toode+" Hind: "+str(hind)+"\nKas tahad osta?").lower()
    if v=="jah":
        mitu=int(input("Mitu? "))
        tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
        summa+=mitu*hind
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)
while True:
    raha=float(input("Maksa "+str(summa)+"\n"))
    if raha==summa:
        print("Tänan ostu eest!")
        break
    elif raha>summa:
        print("Tänan ostu eest! Tagasi "+str(raha-summa))
        break
    else:
        summa-=raha
        print("Maksa veel"+str(summa))



#8.1 Poes
arve_nr= date.today()#datetime.now()
print(arve_nr)
tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0

toode="Piim"
hind=randint(50,150)/100
v=input("Toode: "+toode+" Hind: "+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu? "))
    tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
    summa+=mitu*hind
toode="Leib"
hind=randint(90,300)/100
v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
    summa+=mitu*hind
toode="Kommid"
hind=randint(600,1500)/100
v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
    summa+=mitu*hind
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)
raha=float(input("Maksa "+str(summa)))
if raha==summa:
    print("Tänan ostu eest!")
elif raha>summa:
    print("Tänan ostu eest! Tagasi "+str(raha-summa))
else:
    print("Maksa veel"+str(summa-raha))













print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Siseda oma nimi.")
print(nimi, " , oi kui ilus nimi!")
number=int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))

def sisend(andmed, andmetüüp): 
        sisend_väärtus = input(andmed)
        try:
            return andmetüüp(sisend_väärtus)
        except ValueError:
            print("Viga! Palun sisestage õige tüüpi andmed.")

if number==1:
    pikkus=sisend("Palun siseda oma pikkus. ", int)
    mass=sisend("Palun siseda oma kaal. ", float)
    index=round(mass/(0.01*pikkus)**2,1)
    print(nimi+"! Sinu keha indeks on: "+str(index))
    if index<=0 or index>=100:
        print("Vale andmed")
    elif index<=16:
        print("Tervisele ohtlik alakaal")
    elif 16>=index<19:
        print("Alakaal")
    elif 19>=index<25:
        print("Normaalkaal")
    elif 25>=index<30:
        print("Ülekaal")
    elif 30>=index<35:
        print("Rasvumine")
    elif 35>=index<40:
        print("Tugev rasvumine")
    elif 40>=index:
        print("Tervisele ohtlik rasvumine")
else :
    print("Kahju! See on väga kasulik info!""\n")

from random import *
inimeste_arv = int(input("Sisestage, kui palju inimesi bussis sõida:"))
print()
bussi_maht = int(input("Valige siini helitugevus \n"
                       "1) eriti väike (kuni 10 istekohta)\n"
                       "2) väike (kuni 25)\n"
                       "3) keskmine (40–50)\n"
                       "4) suur (60-80)\n"
                       "5) eriti suur mahutavus (100-120 istekohta): "))
print()
if inimeste_arv <= 10 and bussi_maht == 1:
    print("Люди поместяться в автобус 1")

elif inimeste_arv <= 30 and bussi_maht == 2:
    print("Люди поместяться 2")

elif inimeste_arv <= 50 and bussi_maht == 3:
    print("Люди поместяться в автобус 3")

elif inimeste_arv <= 80 and bussi_maht == 4:
    print("Люди поместяться 4")

elif inimeste_arv <= 120 and bussi_maht == 5:
    print("Люди поместяться 5")
else:
    print("Люди не вместяться")


#1 Juku läheb kinno
nimi=input("Mis on sinu nimi?").capitalize() #"anna"->"Anna"
print("Tere",nimi) #"Tere, Anna"
if nimi=="Juku":
    print("Lahme kinno")
    vanus=int(input("Kui vana sa oled?"))
    if vanus<0 or vanus>100:
        pilet="vale vanus"
    elif vanus<6:
        pilet="tasuta pilet"
    elif vanus<=14:  #<15
        pilet="lastepilet"
    elif vanus<=65:
        pilet="täispilet"
    elif vanus<=100:
        pilet="sooduspilet"
    print(pilet) # Ilus ja õige vastus!"Vale vanus" või "On vaja osta ...."
else:
    print("Ma ootan Jukut")
print()


protsent=randint(-100,500) #0-100 0-60-"2", 61-75-"3", 76-89-"4", 90-100-"5"
print(protsent,"% on testi tulemus")
if protsent<0 or protsent>100:
    tulemus="valed andmed"
elif 0<protsent<60:    #protsent>0 and protsent<60, protsent<60
    tulemus="hinne 2"
elif 60<=protsent<75:
    tulemus="hinne 3"
elif 75<=protsent<90:
    tulemus="hinne 4"
else:    #= elif 90<=protsent<=100:
    tulemus="hinne 5"
print(tulemus)
print()


arv=randint(0,100) #juhuslik täisarv vahemikust 0...100

if arv%2==0:
    print(arv,"on paaris arv")
else:
    print(arv,"on paaritu arv")
print()

print("Tund on alanud")
hilinemine=input("Kas õpilane on hilinenud?")
# "JAH"-a.upper(), "jah"-a.lower(), "Jah"-a.capitalize(), jAH
if hilinemine.upper()=="JAH":
    print("Õpilane ootab 30 min")
print("Õpilane astub klassi")


