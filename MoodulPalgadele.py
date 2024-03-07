def inimeste_ja_palkade_lisamine(i:list,p:list,n=1)->any:
    """Funktsioon tagastab uuendatud loendid, kus lisatud inimesi ja palka
    
    :param list i: Inimeste järjend
    :param list p: Palgate järjend
    :param int n: Inimeste arv
    :rtype: list,list
    """
    if n>0:
        for j in range(n):
            nimi=input("Nimi: ").capitalize()
            palk=int(input("Palk: "))
            i.append(nimi)
            p.append(palk)
    return i,p
def andmed_veerudes(i:list,p:list):
    """Funktsioon kuvab ekraanile kahe järjendite andmed veerudes
    :param list i: Inimeste järjend
    :param list p: Palgate järjend
    """
    for j in range(len(i)):
        print(i[j],"-",p[j])
def andmete_eemaldamine_nimi_jargi(i:list,p:list)->any:
    """Funktsioon kustutab andmeid ja tagastab listid.
    :param list i: Inimeste järjend
    :param list p: Palgate järjend
    :rtype: list,list
    """
    nimi=input("Keda kustutada ära(nimi): ")   
    for j in range(len(i)):
        if nimi in i:
            i.remove(nimi)
            p.pop(j)
    return i,p
def kellel_on_suurim_palk(i:list,p:list)->list:
    """
    """
    nimed=[] #tühi list
    max_palk=max(p) #suurim palk
    ind=-1 #start indeks
    for palk in p:
        if palk==max_palk:
            ind+=1
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed
def kellel_on_vaiksem_palk(i:list,p:list)->list:
    """
    """
    nimed=[] #tühi list
    min_palk=min(p) #suurim palk
    ind=p.index(min_palk) #start indeks
    mitu=p.count(min_palk)
    for j in range(mitu):
            nimi=i[p.index(min_palk,ind)]
            nimed.append(nimi)
            ind=+1
    return nimed
def sorteerimineA_Z(i:list,p:list):
    """

    """
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]>p[m]:
                p[m],p[n]=p[n],p[m]
                i[m],i[n]=i[n],i[m]
    return i,p
def vordsed_palgad(i:list,p:list)->list:
    """
    """
    nimed={} #{key1:value,key2:value}, key1!=key2
    #for id_, inim in enumerate(i):
    #    if inim==nimi:
    #        nimed.append=inim
    for palk in p:
        n=p.count(palk)
        ind=p.index(palk)
        if n>1:
            subnimed=[]
            for j in range(n):
                nimi=i[p.index(palk,ind)]
                subnimed.append(nimi)
                p.pop(ind)
                i.pop(ind)
                ind=+1
            nimed[palk]=subnimed
    print(nimed)
def palk_nimi_jargi(i:list,p:list)->dict:
    palgad={}
    nimi=input("Nimi: ")    
    n=i.count(nimi)
    if n>1:
        subp=[]
        for j in range(n):
            palk=p[i.index(nimi)]
            subp.append(palk)
            p.pop(i.index(nimi))
            i.pop(i.index(nimi))
        palgad[nimi]=subp
    print(palgad)
