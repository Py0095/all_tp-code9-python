import all
import os
while True:
    all.menu()
    opsyon = int(input('Entre opsyon u vle a: '))
    all.clear()

    if opsyon == 1:
        fileName = r'database.txt'
        f=os.path.exists(fileName)
        if f:
            print(True)
        else:
            with open('database.txt','x') as file:
                file.close()
        nomw = all.bay_nomw('nomw')
        siyatiw = all.bay_nomw('siyatiw')
        file = open('database.txt','r')
        kantite = 0
        for line in file:
            kantite +=1
        file.seek(0)
        print('-Non ak Siyatiw se: %s %s \n'%(nomw,siyatiw))
        print(f"Bonjou {nomw} {siyatiw}, nou rekoni nan sèvis nou an, nou deja jenere {kantite} epsedo pou {kantite} moun deja.")
        file.close()
        eps = all.lis_epsedo(nomw,siyatiw)
        print('-------------------------------------------------------------------------------------------')
        print('1)Men lis epsedo :','\t'.join(eps))
        c = all.chwa_epsedo(eps)
        print('2)Selon yon chwa aleyatwa nou propozew epsedo sa:',c)
        print('-------------------------------------------------------------------------------------------')
        liseps=(f'{kantite+1})',c,'\n')
        
        with open('database.txt', 'a') as temp_file:
          for item in liseps:
            temp_file.write("%s" % item)
        

    elif opsyon == 2:
        print("================================================")
        print('Bonjour ou Bonsoir tou depan de le aksan grav kew wap li\n'
              'Wap li info sa yo objektif program sa se mande\n'
              'itilizate kap itilize pwogram nan poul antre nonl\n' 
              'epi lapjenere 5 epsedo pou li epi lap proze itilizate\n'
              'youn selon yon chwa ki fet aleyatwa.')
        print("================================================")
    elif opsyon == 3:
        print('--------==lis epsedo enregistre==----------')
        file = open('database.txt', 'r')
        print('\n',file.read())
        file.close()
        print('-------------------------------------------')
    
    elif opsyon == 0:
        break
    else:
        print('Opsyon ou antre a pa valid')
        
print("==================================================")
print('  Mesi deske t chwazi itilize pwogram nou an!!!!')
print("==================================================")




