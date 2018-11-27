#########################################################################
# - Author: Mattia Pedroncelli  mattia.pedroncelli@gmail.com            # 
# - Date  : 26/11/2018                                                  #
# - Linguaggio : Python                                                 # 
# CALCOLO ORE, MINUTI, SECONDI MANCANTI AD UN DETERMINATO ORARIO        #
#########################################################################

import time

# IMPOSTAZIONE INIZIALE COSTANTI (ORARIO CALCOLO COUNT-DOWN)
ora_fine = 12
minuti_fine = 15 
secondi_fine = 50 

  
# ***** PRIMA ELABORAZIONE FUORI CICLO *******************************************************

somma_secondi_fine = (ora_fine*3600)+minuti_fine*60+secondi_fine
 
ora_corrente=time.strftime("%H")
minuti_correnti=time.strftime("%M")
secondi_correnti=time.strftime("%S")

# TRASFORMAZIONE DELLE STRINGE RITORNATE DALLA FUNZIONE strftime IN VARIABILI DI TIPO INT
# METTO LE VARIABILI IN UNA LISTA time_int[] PER COMODITA'
time_strings = time.strftime("%H,%M,%S")
t = time_strings.split(',')
time_int = [ int(x) for x in t ]

# CALCOLO ORE, MINUTI, SECONDI MANCANTI
somma_secondi_attuali = (time_int[0]*3600)+(time_int[1]*60)+time_int[2]
differenza_secondi = somma_secondi_fine - somma_secondi_attuali

if differenza_secondi < 0:

    print "------------------------------------------------------------------------------"
    print "ATTENZIONE !!!!!!!!"
    print "                 "
    print "L'orario attuale e' successivo all'orario impostato per il count-down !!! "
    print "Orario impostato :",ora_fine,":",minuti_fine,":",secondi_fine,""
    print "Orario attuale   :",ora_corrente,":",minuti_correnti,":",secondi_correnti,""
    print "------------------------------------------------------------------------------"
    exit()

# ***** PRIMA ELABORAZIONE FUORI CICLO *******************************************************

 
# CICLO ELABORATIVO PRINCIPALE
 
while differenza_secondi > 0:

   # OTTIENE ORA MINUTI E SECONDI ATTUALI , VARIABILI DI TIPO STRING
   ora_corrente=time.strftime("%H")
   minuti_correnti=time.strftime("%M")
   secondi_correnti=time.strftime("%S")

   # TRASFORMAZIONE DELLE STRINGE RITORNATE DALLA FUNZIONE strftime IN VARIABILI DI TIPO INT
   # METTO LE VARIABILI IN UNA LISTA time_int[] PER COMODITA'
   time_strings = time.strftime("%H,%M,%S")
   t = time_strings.split(',')
   time_int = [ int(x) for x in t ]


   # CALCOLO ORE, MINUTI, SECONDI MANCANTI -------------

   somma_secondi_attuali = (time_int[0]*3600)+(time_int[1]*60)+time_int[2]
   differenza_secondi = somma_secondi_fine - somma_secondi_attuali

   if differenza_secondi < 60:
      ore_mancanti = 0
      minuti_mancanti = 0
      secondi_mancanti = differenza_secondi

   elif differenza_secondi < 3600:
      ore_mancanti = 0 
      minuti_mancanti = int(differenza_secondi/60)
      secondi_mancanti = differenza_secondi - (minuti_mancanti*60)
      
   else:

      

   # ---------------------------------------------------

 
   print "                 "
   print " Alle",ora_corrente,":",minuti_correnti,":",secondi_correnti,""
   print " Alle",ora_fine,":",minuti_fine,":",secondi_fine,"" 
   print "                                                         **************"
   print "                                                         * Count-down *"
   print "                                                         **************"
   print " Mancano solo :                                ",ore_mancanti,"Ore -",minuti_mancanti,"Minuti -",secondi_mancanti,"Secondi"
   print " "
   print "------------------------------------------------------------------------------"
   time.sleep(1)


while 1>0:
   print "                 "
   print "E' FINITAAAAAAAAAAAAAAAAAA !!!!!!!!"
   print "Count-down terminato               "
   print "------------------------------------------------------------------------------"
   time.sleep(1)

