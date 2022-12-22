import os
import menu
import platform
os1 = platform.system()

if os1 == 'Windows':
    def antiviris_mwen():
        t=0
        for i in range(20):
            # fileTest = r"f'C:viris{t}.txt'"
            try:
                a = os.remove(f'C:\\Users\\14073\\viris{t}.txt')
                t +=1
 
            except OSError as e:
                # print('nou pa detekte okenn viris',e)
                menu.clear()
            
            #print('Nou pa detekte okenn viris potansyel!!!')


    try:
        os.makedirs('C:\\Users\\14073\\telegram')
    except FileExistsError as e:
        print('Dosier sa egziste deja')
        # menu.clear()
   
    if antiviris_mwen:
        # print('yes')
        with open('C:\\Users\\14073\\telegram\\rescue.txt','a') as file:
            f = file.write(f'{1}')
                    # print(f)
    else:
        print('Ou toujou infekte')
   
        


elif os1 == 'linux' or os1 == 'linux2' :
    def antiviris_mwen():
        t=0
        for i in range(20):

            try:
                
                a = os.remove(f'/home/viris{t}.txt')
                t +=1

            except OSError as e:
                # print(e)
                menu.clear()
    try:
        os.makedirs('/home/telegram')
    except FileExistsError as e:
        print('Dosier sa egziste deja')
        menu.clear()

    if antiviris_mwen:
        # print('yes')
        with open('/home/telegram/rescue.txt','a') as file:
            f = file.write(f'{1}')
                    # print(f)
    else:
        print('Ou toujou infekte')

# antiviris_mwen()

elif os1 == 'darwin':
    def antiviris_mwen():
        t=0
        for i in range(20):

            try:
                
                a = os.remove(f'/home/viris{t}.txt')
                t +=1
            except OSError as e:
                # print(e)
                menu.clear()
    try:
        os.makedirs('/home/telegram')
    except FileExistsError as e:
        print('Dosier sa egziste deja')
        menu.clear()
    if antiviris_mwen:
        # print('yes')
        with open('/home/telegram/rescue.txt','a') as file:
            f = file.write(f'{1}')
                    # print(f)
    else:
        print('Ou toujou infekte')


else:
    print('Dezole antiviris sa pap f anyn pou paske nou pa rekonet os wap itilize a')

# antiviris_mwen()