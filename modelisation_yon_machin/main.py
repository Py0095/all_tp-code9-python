import kawoutchou
import time
import menu

while True:
    menu.menu()
    opsyon = int(input('Entre opsyon u vle a: '))
    menu.clear()

    if opsyon == 1:
        while True:
            menu.menu1()
            opsyon = int(input('Entre opsyon u vle a: '))
            menu.clear()

            if opsyon == 1:
                nom = input('Antre nomw: ')
                menu.clear()
                obje = kawoutchou.Machin(nom)
                time.sleep(3)
                menu.clear()

            elif opsyon == 2:
                obje.akselerate()
                time.sleep(3)
                menu.clear()
            elif opsyon == 3:
                print(obje.frenaj())
                time.sleep(3)
                menu.clear()

            elif opsyon == 4:
                nouvo_nom = input('Antre nom moun kew ap van machin nan: ')
                menu.clear()
                print(obje.van_machin(nouvo_nom))
                time.sleep(4)
                menu.clear()

            elif opsyon == 5:
                 nouvo_koule = input('Ki nouvo koule ou ta renmen bay machin nan: ')
                 menu.clear()
                 print(obje.douko_machin(nouvo_koule))

            elif opsyon == 6:
                kob = int(input('Mete kantite montan kob kew vle a: '))
                menu.clear()
                print(obje.ht_gaz(kob))
                time.sleep(3)
                menu.clear()

            elif opsyon == 7:
                print(obje.rezevwa_machin())
                time.sleep(3)
                menu.clear()

            elif opsyon == 8:
                obje.tente = True
                time.sleep(3)
                menu.clear()

            elif opsyon == 9:
                print(obje.pri)
                time.sleep(3)
                menu.clear()
                
            elif opsyon == 10:
                print('Nom pwopriete machin nan se : ',obje.pwopriete)
                time.sleep(3)
                menu.clear()
                

            elif opsyon == 0:
                break
        
    elif opsyon == 2:
        print("================================================")
        print('Objektif pwogram sa se fe modelizasyon yon machine\n'
              'Kotew ke nu kreye yon klass machinn epi nu kreye plizye\n'
              'Atribi ak methode kote nu baw possiblite pouw teste machin\n' 
              'Ak tout fonksyonalite li gnyn yo')
        print("================================================")
        time.sleep(4)
    elif opsyon == 3:
        break
    else:
        print('Opsyon ou antre a pa valid')
        
print("==================================================")
print('  Mesi deske t chwazi itilize pwogram nou an!!!!')
print("==================================================")

