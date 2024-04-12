from os import system
from gtts import *
def loe_failist(fail:str)->list:
    """Loeme failist read ja salvestame järjendisse. Funktsioon tagastab järjend
    :param str fail:
    :rtype: list
    """
    f=open(fail,'r',encoding="utf-8") #try
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend
def kirjuta_failisse(fail:str,jarjend=[]):
    """
    """
    #n=int(input("Sisesta mitu elemendi: "))
    #for i in range(n):
    #    jarjend.append(input(f"{i+1}. element: "))
    f=open(fail,'w',encoding="utf-8")
    for el in jarjend:
        f.write(el+"\n")
    f.close()
def kirjuta_log_pas(fail:str,jarjend1=[],jarjend2=[]):
    """
    """
    f=open(fail,'w',encoding="utf-8")
    for i in range(len(jarjend1)):
        f.write(jarjend1[i]+":"+jarjend2[i]+"\n")
    f.close()
def loe_pas_ja_log(fail:str)->any:
    """Loeb failist andmed, mis oli sisestatud formaadis "login:password" igas reas eraldi
    """
    fail=open(fail,"r",encoding="utf-8")
    log=[]
    pas=[]
    #log_pas={}
    for line in fail:
        n=line.find("-")# login:password - разделитель
        log.append(line[0:n].strip())
        pas.append(line[n+1:len(line)].strip())    
        #l,p=line.strip().split("-")
        #log_pas[l]=p        
    fail.close()
    return log,pas #,log_pas

def heli(tekst:str,keel:str):
    obj=gTTS(text=tekst,lang=keel,slow=False).save("heli.mp3")
    system("heli.mp3")


