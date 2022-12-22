import hashtypo
import os 
import menu
from hashlib import sha3_256
import getpass
from time import sleep
 
clear = lambda: os.system('cls')


while  True:
    menu.menu()
    opsyon = input('Antre opsyon u vle a: ')
    clear()
    if opsyon == '1':
        f_first = input('Antre nom fichier ke wap kripte a: ')
        last_1 = f_first +'_'
        password_user = getpass.getpass(prompt = 'Antre modpas kriptaj a: ')
        k = hashtypo.hash_1(f_first,last_1,password_user)
        with open('list_fichye', 'a') as file:
            lis = file.write(last_1 + '\n')
            os.remove(f_first)
        sleep(1)
        print('Fichye kripte ak sikse.')

    elif opsyon == '2':
        with open('list_fichye',"r") as file:
            print('-------------------------------------------')
            g = file.read()
            print(g)
            print('-------------------------------------------')
        f_first = input('Antre nom fichier ke wap dekripte a: ')
        last_1 = f_first[:-1]
        password_user = getpass.getpass(prompt = 'Antre modpas dekriptaj la: ')
        k = hashtypo.hash_1(f_first,last_1,password_user)
        os.remove(f_first)
        sleep(2)
        clear()
        print('Fichye dekripte ak sikse.')

    elif opsyon == '3':
        f_first = input('Antre nom fichier ke wap kripte a: ')
        hashtypo.zip_dossier(f_first)

    elif opsyon == '4':
        file_name = input('Antre nom fichier ke wap dekripte a: ')
        hashtypo.dekrypte_dossier(file_name)

    elif opsyon == '5':
        print('------------------------------------------------\nMesi deskew t itilize pwogram nou an\n------------------------------------------------')
        exit()

    else:
        print('Opsyon sa pa valid!!!!')
        sleep(2)
