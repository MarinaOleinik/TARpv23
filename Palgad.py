from MoodulPalgadele import *


palgad=[1,1500,1000,10,1200,55,55]
inimesed=["A","B","A","D","D","W","S"]
print(palgad)
print(inimesed)
while True:
    print("0-Naita andmed veerudes\n1-Andemete lisamine\n2-Andmete eemaldamine\n3-Kellel on suurim palk\n4-Kellel on kõige väiksem palk\n5-Lalle on võrdsed palgad\n6-Palga otsing nimi järgi")
    valik=int(input())
    if valik==1:
        inimesed,palgad=inimeste_ja_palkade_lisamine(inimesed,palgad,int(input("Mitu inimest lisame? ")))
    elif valik==0:
        andmed_veerudes(inimesed,palgad)
    elif valik==2:
        andmete_eemaldamine_nimi_jargi(inimesed,palgad)
    elif valik==3:
        nimed=kellel_on_suurim_palk(inimesed,palgad)
        print(nimed)
    elif valik==4:
        nimed=kellel_on_vaiksem_palk(inimesed,palgad)
        print(nimed)
    elif valik==5:
        vordsed_palgad(inimesed,palgad)
    elif valik==6:
        palk_nimi_jargi(inimesed,palgad)