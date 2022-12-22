from random import randrange
import os
clear = lambda: os.system('cls')

nomb_odinatè = randrange(0, 4)
def menu():
    print("===================-La woulet-===================")
    print('Jwet sa konsiste a devine nomdb odinate a mete a')
    print('                1)Antre nan jwet la')
    print('                2)Ed')
    print('                0)Kite jwet la')

menu()
opsyon = int(input('Entre opsyon u vle a: '))
clear()
while opsyon != 0:
    chans = 5
    if opsyon == 1:
        while chans > 0:
            print("==================================================")
            nomb_itilizatè = input(' Ki nonb ou chwazi itilizatè?: ')
            clear()
            chans -= 1
            if nomb_odinatè > int(nomb_itilizatè):
                print(' Ou echwe!!! nomb ou chwazi a pi piti pase sa odinatè')
                print(' Ou rete ' + str(chans) + ' chans')

            elif nomb_odinatè == int(nomb_itilizatè):
                print(' Ou reyisi!!! nomb ou chwazi a egal ak pa odinatè a')
                print(' Pati a fini!!! Ou genyen jwet la')
                print("==================================================")
                print()
                print()

                break
            else:
                print(' Ou echwe!!! nomb ou chwazi a pi gwo pase pa odinatè a')
                print(' Ou rete ' + str(chans) + ' chans')
                print()
                print()

            if chans == 0:
                print("==================================================")
                print(' Pati a fini!!! Ou pedi ou pa gn chans anko')
                print("==================================================")
                print()
                print()

    elif opsyon == 2:
           print("==================================================")
           print('Desole nu paka edew se chans pouw gnyn lolll')
           print("==================================================")
           print()
           print()

    else:
            print('Opsyon ou antre a pa valid')
    menu()
    opsyon = int(input('Entre opsyon u vle a: '))
    clear()

print("==================================================")
print('  Mesi deske chwazi itilize pwogram nou an!!!!')
print("==================================================")


