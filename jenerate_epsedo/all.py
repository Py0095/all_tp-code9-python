import random
import os
import random
from secrets import choice 

clear = lambda: os.system('cls')
inverser= lambda mo: mo[::-1]
#menu
def menu():
    print("=== Jenerate epsedo ===")
    print('1)Antre nan program nan')
    print('2)Kisa program nan ye')
    print('3)Lis epsedo ')
    print('0)Kite programe nan')
# fonksyon pouw antre nomw
def bay_nomw(nom1) -> str:
    nom = ""
    while len(nom) < 3 or not nom.replace(" ", "").isalpha():
        nom = input('-Antre %s w: '%(nom1))
        if len(nom) < 3:
            print('Lolll m poko janm we yon non ki gen pi piti pase 3 let.\nReantre non w svp.')
        elif not nom.replace(" ", "").isalpha():
            print('%s Sa pa yon nom, ou oblije reeseye'%(nom))

    return nom.title().strip()
# fonksyon kap pran premye let nan nomw
def premye_let(n):
    e = ''
    for i in n.split():
     e += i[0]
    return e
# generate epsedo
def lis_epsedo(nom,siyati) -> str:
    epsedo1 = premye_let(nom) + premye_let(siyati) + str(len(nom.replace(' ','') + siyati.replace(' ','')))
    epsedo2 = nom.replace(' ','')+siyati.replace(' ','')
    epsedo3 =inverser(min(nom.split() + siyati.split(),key=len)) + str(random.randrange(1000,9999))# ''.join(reversed(min(nom.split() + siyati.split(),key=len))) sa c fason mw t k inverser mo anko
    gwoup_epsedo  = [nom,siyati,epsedo1,epsedo2.title(),epsedo3.title()]
    list=[nom,siyati,epsedo1,epsedo2.title(),epsedo3.title()]
    return  list#epsedo1,epsedo2,epsedo3,nom,siyati
    
# fonksyon chwa aleatwa
def chwa_epsedo(list) -> str:
    ch1 = []
    for i in list:
        if len(i) <= 7:
         ch1.append(i)
    return choice(ch1)


