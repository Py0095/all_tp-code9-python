from ast import Break
import random
import os
from secrets import choice
import pickle
from time import sleep
clear = lambda : os.system('cls')

def chwa_odinate():
    chwa2 =random.choice(['papye','sizo','wòch'])
    return chwa2


def chwa_itilizate(chwa1,):
        lis = ['papye', 'sizo', 'wòch']
        if chwa1 == 'p' or chwa1 == 'P':
            chwa1 = lis[0]
        elif chwa1 == 's' or chwa1 == 'S':
            chwa1 = lis[1]
        elif chwa1 == 'w' or chwa1 == ' W':
            chwa1 = lis[2]
        elif chwa1 =='4':
            pass
        else:
            chwa1=f'"{chwa1}" Chwaw f a pa valid reeseye anko.'
        return chwa1

def komparezon(chwa1,chwa2,i,o):
    if chwa1 == 'sizo' and chwa2 == 'papye':
        print(f'{i} bat {o}')
        chwa1 = 50  #1

        try:
            with open("C:Sko_chwa1.txt",'rb') as rezilta_chwa1:
                done = pickle.load(rezilta_chwa1)
                done = done + chwa1

            with open("C:Sko_chwa1.txt", "wb") as rezilta_chwa1:
                pickle.dump(done,rezilta_chwa1)

        except FileNotFoundError:
            with open("C:Sko_chwa1.txt", "wb") as rezilta_chwa1:
                sko = chwa1
                pickle.dump(sko,rezilta_chwa1)
        
        print(f'🥳🥳🥳🥳🥳{i} gnyn {chwa1} pwen')
##########################################################################
    elif chwa1 == 'sizo' and chwa2 == 'wòch':
        print(f'{o} bat {i}')
        try:
            with open("C:Sko_chwa1.txt",'rb') as rezilta_chwa1:
                done = pickle.load(rezilta_chwa1)
                if done <= 0:
                    done = 0
                else:
                    done = done - 50

            with open("C:Sko_chwa1.txt", "wb") as rezilta_chwa1:
                pickle.dump(done,rezilta_chwa1)

        except FileNotFoundError:
            with open("C:Sko_chwa1.txt", "wb") as rezilta_chwa1:
                sko = 0
                pickle.dump(sko,rezilta_chwa1)

        print(f'{i} ou pedi 50 pwen😫😫.')
##############################################################################
    elif chwa1 == 'papye' and chwa2 == 'wòch':
         print(f'{i} bat {o}')
         chwa1 = 50
         try:
            with open("C:Sko_chwa1.txt",'rb') as rezilta_chwa1:
                done = pickle.load(rezilta_chwa1)
                done = done + chwa1

            with open("C:Sko_chwa1.txt", "wb") as rezilta_chwa1:
                pickle.dump(done,rezilta_chwa1)

         except FileNotFoundError:
                with open("C:Sko_chwa1.txt", "wb") as rezilta_chwa1:
                    sko = chwa1
                    pickle.dump(sko,rezilta_chwa1)
         print(f'🥳🥳🥳🥳🥳{i} gnyn {chwa1} pwen')
############################################################################
    elif chwa1 == 'papye' and chwa2 == 'sizo':
         print(f'{o} bat {i}')
         try:
            with open("C:Sko_chwa1.txt",'rb') as rezilta_chwa1:
                done = pickle.load(rezilta_chwa1)
                if done <= 0:
                    done = 0
                else:
                    done = done - 50

            with open("C:Sko_chwa1.txt", "wb") as rezilta_chwa1:
                pickle.dump(done,rezilta_chwa1)

         except FileNotFoundError:
            with open("C:Sko_chwa1.txt", "wb") as rezilta_chwa1:
                sko = 0
                pickle.dump(sko,rezilta_chwa1)

         print(f'{i} ou pedi 50 pwen😫😫.') 
############################################################################
    elif chwa1 == 'wòch' and chwa2 == 'papye':
         print(f'{o} bat {i}')
         try:
            with open("C:Sko_chwa1.txt",'rb') as rezilta_chwa1:
                done = pickle.load(rezilta_chwa1)
                if done <= 0:
                    done = 0
                else:
                    done = done - 50

            with open("C:Sko_chwa1.txt", "wb") as rezilta_chwa1:
                pickle.dump(done,rezilta_chwa1)

         except FileNotFoundError:
            with open("C:Sko_chwa1.txt", "wb") as rezilta_chwa1:
                sko = 0
                pickle.dump(sko,rezilta_chwa1)

         print(f'{i} ou pedi 50 pwen😫😫.')
         
###############################################################################
    elif chwa1 == 'wòch' and chwa2 == 'sizo':
         print(f'{i} bat {o}')
         chwa1 = 50
         try:
            with open("C:Sko_chwa1.txt",'rb') as rezilta_chwa1:
                done = pickle.load(rezilta_chwa1)
                done = done + chwa1

            with open("C:Sko_chwa1.txt", "wb") as rezilta_chwa1:
                pickle.dump(done,rezilta_chwa1)

         except FileNotFoundError:
            with open("C:Sko_chwa1.txt", "wb") as rezilta_chwa1:
                sko = chwa1
                pickle.dump(sko,rezilta_chwa1)
         print(f'🥳🥳🥳🥳🥳{i} gnyn {chwa1} pwen')
###################################################################################
    elif chwa1 == chwa2:
        print('Match null rejwe anko😁😁😀.')
    else:
        print('Chwaw 😡😡😡f yo pa nan jwet la asurew kew f yon chwa valid.')
        return 

def meye_sko():
    with open("C:Sko_chwa1.txt",'rb') as rezilta:
        done = pickle.load(rezilta)
        return done

def efase_sko():
   with open("C:Sko_chwa1.txt", "wb") as rezilta_chwa1:
        sko = 0
        t = pickle.dump(sko,rezilta_chwa1)
        return sko

def counter():
    print('1️⃣')
    sleep(1)
    clear()
            
    print('2️⃣')
    sleep(1)
    clear()
                
    print('3️⃣')
    sleep(1)
    clear()
    return


