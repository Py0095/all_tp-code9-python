from hashlib import sha3_256
import getpass
import os
import shutil
import zipfile

def  hash_1(f_first,last_1,password_user) :
    try:
        keys = sha3_256(password_user.encode('utf-8')).digest()
        with open(f_first,'rb') as f_first:
            with open(last_1,'wb') as last_1:
                i = 0
                while f_first.peek():
                    f = ord(f_first.read(1))
                    l = i % len(keys)
                    b = bytes([f^keys[l]])
                    last_1.write(b)
                    i +=1

    except:
        print('sa pa yon fichye')

        return



def zip_dossier(filename):
    format = "zip"
    directory = os.getcwd()
    shutil.make_archive(filename, format, directory)
    return

def dekrypte_dossier(test_file_name):
    try:
        with zipfile.ZipFile(test_file_name, 'r') as zip:
            zip.printdir()
            zip.extractall() 
    except zipfile.BadZipFile:
        print('zipfile.BadZipFile')
        return






# def lis_fichye(a):
#     # try:
#     with open(a, 'a') as list_fichye:
#         lis = list_fichye.write(a + '\n')
#     # except:
#     #     with open('all_fichye.pickle', 'a') as p:
#     #         lis.append(a)
#     #         pickle.dump(lis, p)
#         return lis

# def load_lis_fichye(lis):
#     with open(lis,"r") as lis:
#         print('-------------------------------------------')
#         g = lis.read()
#         print('-------------------------------------------')
#         return g       






































# import os


# # Pwogram sa ap pemet nou kripte epi kache fichye oubyen dosye ou yo


# class MaskeFichye :
    
    
    
#     def __init__(self) :
#         self.KodSekre = ""
#         self.NonDosFichPouKripte = ""
#         self.NonDosKache = ""
#         self.LisDosFichKripte = ""
        
# # Fonksyon antre pwogram nan 
        
#     def FonkByenvini(self) :
#         print("Byenvini nan pwogram HASHTYPO a ! \nAk pwogram sa konfidansyalite fichye ou yo asire")
#         print("Gras ak pwogram sa ou ap kapab maske fichye ou ak dosye ou genyen sou odinatè a")
#         Maske.MaskDosFich()
        
        
#  # Fonksyon pou kripte ak kache fichye       
#     def MaskDosFich(self) :
#         self.NonDosFichPouKripte = input("\nMete non fichye oubyen dosye ou vle kripte epi kache a !\nNon Fichye ou Dosye : ")
        
        
        
        
        
# Maske = MaskeFichye()



# AnplasmanAktyel = os.getcwd()
# AnplasmanFDMaske = AnplasmanAktyel + "\\Maskay\\LisFichyeDatabase.txt"


# try :
#     Maske.LisDosFichKripte = open(str(os.chdir(AnplasmanFDMaske)), "r")
#     Maske.LisDosFichKripte.close()
# except FileNotFoundError:
#     Maske.LisDosFichKripte = open (str(os.chdir(AnplasmanFDMaske)),"a")
#     Maske.LisDosFichKripte.write("Bonjou")
#     Maske.LisDosFichKripte.close()



# #print(AnplasmanAktyel)

# Maske.FonkByenvini()

    
        