from random import *
#6
try:
    pass
except :
    pass

try:
    aeg = float(input("Mitu tundi kulus sõiduks? ")) #aeg ei saa olla 0
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
    kiirus = teepikkus/aeg
    print("Sinu kiirus oli " + str(kiirus) + " km/h")
except:
    print("Viga andmetüübiga")

print()

#10
P=randint(1,5)
hind=12.90
hind*=1.1 #hind koos jätatega
osa=round(hind/P,2)
print("Iga sõber maksab: ",osa)

print("Tere maailm!")
#1
nimi=input("Mis on sinu nimi?") #comment
vanus=int(input("Kui vana sa oled?")) #float()->2.5
#print("Tere tulemast! "+nimi+". Sa oled"+str(vanus)+" aastat vana")
#print("Tere tulemast!",nimi,". Sa oled",vanus,"aasta vana")
print("Tere tulemast! {0}. Sa oled {1} aastat vana".format(nimi,vanus))
#print("Muutuja vanus=",vanus,",tüüp on",type(vanus))
#2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print("Muutuja vanus=",vanus,",tüüp on",type(vanus))
print("Muutuja eesnimi=",eesnimi,",tüüp on",type(eesnimi))
print("Muutuja pikkus=",pikkus,",tüüp on",type(pikkus))
print("Muutuja kas_käib_koolis=",kas_käib_koolis,",tüüp on",type(kas_käib_koolis))