#!/usr/bin/env python
#########################################################################
# - Author: Mattia Pedroncelli (mattia.pedroncelli@gmail.com)           # 
# - Date  : 26/11/2018                                                  #
# - Linguaggio : Python                                                 #
# _____________________________________________________________________ # 
# CALCOLO ORE, MINUTI, SECONDI MANCANTI AD UN DETERMINATO ORARIO        #
#########################################################################

import time

# IMPOSTAZIONE INIZIALE ORARIO PER CALCOLO COUNT-DOWN(IMPOSTAZIONE VALORI DA SHALL)

print" "
print "INSERIMENTO DELL'ORARIO PER CUI VUOI VENGA ESEGUITO IL COUNT-DOWN"
ora_fine = raw_input("Inserisci l'ora (HH) : ")
minuti_fine = raw_input("Inserisci i minuti (MM) : ")
secondi_fine = raw_input("Inserisci i secondi (SS) : ") 

# *********************************************************************************************** 
# ***** INIZIO PRIMA ELABORAZIONE FUORI CICLO ***************************************************
# ***********************************************************************************************

somma_secondi_fine = (int(ora_fine)*3600)+(int(minuti_fine)*60)+int(secondi_fine)
 
ora_corrente=time.strftime("%H")
minuti_correnti=time.strftime("%M")
secondi_correnti=time.strftime("%S")

# TRASFORMAZIONE DELLE STRINGE RITORNATE DALLA FUNZIONE strftime IN VARIABILI DI TIPO INT
# METTO LE VARIABILI IN UNA LISTA time_int[] PER COMODITA'
time_strings = time.strftime("%H,%M,%S")
t = time_strings.split(',')
time_int = [ int(x) for x in t ]

# CALCOLO ORE, MINUTI, SECONDI MANCANTI PER PRIMA VERIFICA
somma_secondi_attuali = (time_int[0]*3600)+(time_int[1]*60)+time_int[2]
differenza_secondi = somma_secondi_fine - somma_secondi_attuali

if differenza_secondi < 0:

    print "---------------------------------------------------------------------------"
    print "ATTENZIONE !!!! CALCOLO COUNT-DOWN IMPOSSIBILE"
    print "                 "
    print "L'orario attuale e' successivo all'orario impostato per il count-down !!! "
    print "Orario impostato :",ora_fine,":",minuti_fine,":",secondi_fine,""
    print "Orario attuale   :",ora_corrente,":",minuti_correnti,":",secondi_correnti,""
    print "---------------------------------------------------------------------------"
    exit()
# ***********************************************************************************************
# ***** FINE PRIMA ELABORAZIONE FUORI CICLO *****************************************************
# ***********************************************************************************************


   
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

   # ********************************************************************************************
   # INIZIO CALCOLO ORE, MINUTI, SECONDI MANCANTI ***********************************************
   # ********************************************************************************************

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
      ore_mancanti = int(differenza_secondi/3600)  
      minuti_mancanti = int((differenza_secondi - (ore_mancanti*3600))/60)
      secondi_mancanti = differenza_secondi - (ore_mancanti*3600) - (minuti_mancanti*60)
   # ********************************************************************************************
   # FINE CALCOLO ORE, MINUTI, SECONDI MANCANTI *************************************************
   # ********************************************************************************************
 
   print "                 "
   print "                                                   ",ora_corrente,":",minuti_correnti,":",secondi_correnti,""
   print "                                                   **************"
   print "                                                   * Count-down *"
   print "                                        ************            ************"
   print " Alle ore",ora_fine,":",minuti_fine,":",secondi_fine,"       mancano :   ",ore_mancanti,"Ore -",minuti_mancanti,"Minuti -",secondi_mancanti,"Secondi  "
   print "                                        ************************************"
   print "---------------------------------------------------------------------------"
   time.sleep(1)


while 1>0:
   print "                 "
   print "E' FINITAAAAAAAAAAAAAAAAAA !!!!!!!!"
   print "Count-down terminato               "
   print "---------------------------------------------------------------------------"
   time.sleep(1)
