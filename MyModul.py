from math import *
def season(a:int)->str:
    """
    """
    while True:
        if a>0 and a<13:
            break
        else:
            try:
                a=int(input("Ainult 1-12!\n Sisesta veel kord number: "))
            except:
                print("Viga andmetüübiga")
    if a==12 or a==1 or a==2:
        s="talv"
    elif a>2 and a<6:
        s="kevad"
    elif a in range(6,9,1):
        s="suvi"
    elif 9<=a<=11:
        s="sügis"
    return s



def square(külg:float)->any:
    """Tagastab S,P,d
    """
    S=külg**2
    P=4*külg
    d=külg*sqrt(2)
    return S,P,d

def is_year_leap(aasta: int)->bool:
    """Funktsioon otsustab kas aasta on liigaasta või ei ole.
    Tagastad True kui aasta on liigaasta ja False kui aasta on tavaline aasta.

    :param int aasta: Aasta sisestab kasutaja
    :rtype: bool
    """
    if aasta%4==0 and aasta%100!=0:
        return True
    else:
        return False


def Summa(arv1:int,arv2:int,arv3=0)->int:
    """ Funktsioon tagastab kolme arvu summa
        Summa(arv1,arv2,arv3)
    
    :param int arv1: Arv1 sisestab kasutaja
    :param int arv2: Arv2 sisestab kasutaja
    :param int arv3: Vaikimisi arv3 võrdub nulliga
    :rtype: int
    """
    s=arv1+arv2+arv3
    return s
def TuubiKontroll()-> any:
    """Teeb andmete tüübi kontroll ja tagastab x leitud formaatis


    """
    x=input("Sisesta andmed: ")
    try:
        t=int(x)
        return x
    except:
        try:
            t=float(x)
            return x
        except:
            return x