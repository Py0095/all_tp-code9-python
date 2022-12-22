from secrets import choice
import all_function
import os
import all 
import menu
from time import sleep
clear = lambda :os.system('cls')


print('-----------=Swiv instriksyon sa yo pouw ka komanc jwet la=-----------')
nom = all.bay_nomw('nomw')
siyati = all.bay_nomw('siyatiw')
lis_epsedo = all.lis_epsedo(nom,siyati)
epsedo = all.chwa_epsedo(lis_epsedo)
hostname = os.environ['HOSTNAME']
clear()
while True:
    print('_____________Welcome to the game____________') 
    print('Epsedo paw la nan jwet la se: ',epsedo)
    print('Epsedo pa advesew la nan jwet la se:',hostname)
    print('_____________________________________________')

    sleep(3)
    clear()
    print(f'----------------Afrontman-----------------\n            {epsedo} VS {hostname}\n-------------------------------------------')
    sleep(3)
    clear()

    while True:
        menu.menu()
        opsyon = input('Entre opsyon u vle a: ')
        clear()

        if opsyon == 'l' or opsyon == 'L':
                while True:
                    menu.menu1()
                    opsyon2 = input('Antre opsyn u vle a: ')
                    clear()
                    if opsyon2 == '3':
                        opsyon1 = input('CHwazi youn nan opsyn sa yo:\n1) "p"\n2) "s"\n3) "w"\n>')
                        if opsyon1 == opsyon1:
                                i = all_function.chwa_itilizate(opsyon1)
                                o = all_function.chwa_odinate()
                                clear()
                                all_function.counter()
                                print(f'{epsedo} :',i)
                                print(f'{hostname} :',o,'\n---------------------------------------------------------')
                                all_function.komparezon(i,o,epsedo,hostname)
                                sleep(2)
                                clear()
                    elif opsyon2 == '4':
                        break
                    elif opsyon2 == '5':
                        if os.path.isfile('C:Sko_chwa1.txt'):
                            print(f'{epsedo} Meye sko a yo se:\n',all_function.meye_sko(), 'pwen')
                        else:
                            print('⚠️ ⚠️ ⚠️ desole pako gn okenn sko ki anrejistre jwe pou k f sko.')
                            sleep(3)
                            clear()

                    elif opsyon2 == '6':
                        if os.path.isfile('C:Sko_chwa1.txt'):
                            print(' sko a se:',all_function.efase_sko(), 'pwen kunya')
                            
                            sleep(3)
                            clear()
                        else:
                            print('⚠️ ⚠️ ⚠️ desole ou paka efase sko paske gn okenn sko ki anrejistre.')
                        
                            sleep(3)
                            clear()
                    else:
                        print('❌❌❌ chwaw fe a pa valid!!!')
                        sleep(3)
                        clear()    
            
        elif opsyon == 'h' or opsyon == 'H':
            print("================================================")
            print('Jwet sa simple wap jis chwazi antre "P","W","S"\n'
                'si tout fwa ou chwazi eleman ki pi fo a wap gnyn 50 pwen\n'
                'sinon wap pedi 50 pwen map baw yon ti poul.\n- Wòch bat sizo - Sizo bat papye - Papye bat wòch\n la siw pa gnyn jwet la mpa responsabble')
            print("================================================")
            sleep(4)
            clear()
        elif opsyon == 'k' or opsyon == 'K':
                print("==================================================")
                print('  Mesi deske t chwazi itilize pwogram nou an!!!!')
                print("==================================================")
                exit()
        else:
            print('❌❌❌ Opsyon ou antre a pa valid!!!')
            sleep(3)
            clear()



