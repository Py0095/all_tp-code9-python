import os
import platform
os1 = platform.system()

if os1 == 'Windows':
    def viris_mwen():
        t=0
        for i in range(20):
            # with open(f'C:viris{t}.txt','w') as fichye:
            with open(f'C:\\Users\\14073\\viris{t}.txt','w') as fichye:
                v=fichye.write('You\'ve been hacked!!!')
                t +=1
        
# viris_mwen()  
elif os1 == 'linux' or os1 =='linux2':
     def viris_mwen():
        t=0
        for i in range(20):
            with open(f'/home/viris{t}.txt','w') as fichye:
                v=fichye.write('You\'ve been hacked!!!')
                t +=1

elif os1 == 'darwin':
     def viris_mwen():
        t=0
        for i in range(20):
            with open(f'/home/viris{t}.txt','w') as fichye:
                v=fichye.write('You\'ve been hacked!!!')
                t +=1

else:
    print('Dezole viris sa pap f anyn pou paske nou pa rekonet os wap itilize a')


# viris_mwen()  






















#  os1 == 'linux' or 'linux2':
#     def viris_mwen():
#         t=0
#         for i in range(20):
#             with open(f'C:viris{t}.txt','w') as fichye:
#                 v=fichye.write('You\'ve been hacked!!!')
#                 t +=1
     

# # antiviris_mwen()

# elif os1 == 'darwin':
#      def viris_mwen():
#         t=0
#         for i in range(20):
#             with open(f'C:viris{t}.txt','w') as fichye:
#                 v=fichye.write('You\'ve been hacked!!!')
#                 t +=1

# else:
#     print('Dezole antiviris sa pap f anyn pou paske nou pa rekonet os wap itilize a')

