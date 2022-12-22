from platform import machine


class Machin:
    # Atribi de klass 
    kawoutchou = 4

    #Konstrikte nan
    def __init__(self,met_machin_nan):
        print(f'Ou apenn kreye yon obje machin poprietel se {met_machin_nan}')
        self.vites = 0
        self.koule = 'nwa'
        self.model = 'Toyota'
        self.pwopriete = met_machin_nan
        self.gaz = 3500
        self.kantite_kob = 0
        self._tente = False
        self.ane = '2012'
        self._pri = 170000 
        self.konte = 0
        
    
    # method akselerasyn machin nan
    def akselerate(self):
            self.vites += 34 
            self.gaz -= 14
            if self.gaz >300:
                if self.vites < 200:
                    print(f'Wap kouri ak {self.vites} km/h.') 

                elif self.vites < 300:
                    
                    print(f'{self.vites} km/h 😳😳😳!!!! Wap kouri ak trop vites u k f aksidan dezakselere.')

                else:
                    self.vites = 450
                    print(f'{self.vites} km/h Wap peze saw t panc ou panse vites la patap fini🤣🤣🤣🤣 \n Ou rive ak trop vites maximal ou ou pap k aksele anko men fe \n atansyon pouw pa f aksidan dezakselere')

            elif self.gaz < 0:
                self.gaz = 0
                print('Ahhhh 😅😅😅 dat machine etenn anba pyewwww ou anpannn gaz')
            
            else:
                print ('Ahhhh Gaz ou preske fini ui fow tal fe yon ti gaz ou pouw pa anpannnn')
                return 

    # method frenen  machin nan
    def frenaj(self):
            self.vites -= 58
            self.gaz -= 7

            if self.vites > 0:
                a = f'Ou peze fren an vites aktyel ou se {self.vites} km/h.'

            elif self.vites <0:
                self.vites = 0
                a = f'Ou frenen machinn nan sek vites aktyel ou se {self.vites} km/h'

            else:
                a = f'ou frenen machine nan sek vites aktyel ou se {self.vites} km/h.'

            return a

    # method vant machin nan
    def van_machin(self,nouvo_pwopriete):
            self.pwopriete = nouvo_pwopriete
            return f'Toyota anne {self.ane} koule {self.koule} sa vannn pou {self._pri} goud nouvo pwoprietel se {self.pwopriete}.'

    # method douko machin nan
    def douko_machin(self,nouvo_koule):
        self.koule = nouvo_koule
        self._pri += 200
        return f'Machin sa douko nouvo koulel se {self.koule}.'
    

    # method ht gaz
    def ht_gaz(self,kantite_kob):
        g =''
        if self.gaz < 3500:
            if self.gaz > (kantite_kob * 3.785) // 750 :
                self.kantite_kob = kantite_kob  
                self.kantite_kob = (self.kantite_kob * 3.785) // 750
                r = 3500 - self.gaz
                t = (r * 750) / 3.785
                self.gaz += r
                kob =((self.kantite_kob - r)* 750) / 3.785
                g = f'Ou apennn sot fe gaz kantite reservwaw la se: {self.gaz} lit'
                print(f'Ou f gaz pou {t} goud ou rete {kob} goud')
                self.konte += 1
            
            else:
                print('Ou paka ht pou tut kob sa kantite sa')
                
        elif self.gaz == 3500 :
            g = f'Machine nan full li paka pran gaz anko kantite gaz resev ou se {self.gaz} lit donk nap remet ou kob la.'

        else:
            g = f'Machine nan full li paka pran gaz anko kantite gaz resev ou se {self.gaz} lit '
           

        if self.konte > 3:
            self._pri -= 1000
            self.konte = 0
        else:
            self.pri = self._pri
            
        return g
        
       

       

    def rezevwa_machin(self):

        g = f' Kantite gaz se machine ou an se {self.gaz} lit'
        return g


    def _gettente(self):
        print('Machine sa legal')

    def _settente(self,a):
            self._tente = a
            if a== True:
                print('⚠️ Sonje ou dwe gen papye legal DGI poutèt ou tente machin nan.')

            else:
                print('Machin sa pa tente li legall')
                

    tente = property(_gettente,_settente)

    def _getpri(self):
       
       return f'Pri machine nan se :{self._pri} goud'

    def _setpri(self,nouvo_pri):
        self._pri = nouvo_pri
        p = f'Pri 🚗 Machin nan change, nouvo pri a se :{self._pri } goud.'

        return p

    pri = property(_getpri,_setpri)

    
# a = Machin('Aliano')
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# a.akselerate()
# print(a.rezevwa_machin())
# a.tente = True
# a.tente = False