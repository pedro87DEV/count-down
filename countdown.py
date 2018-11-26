#########################################################################
# Author : Mattia Pedroncelli                                           #
# 26/11/2018                                                            # 
# CALCOLO ORE, MINUTI, SECONDI MANCANTI ALLA FINE GIORNATA LAVORATIVA   #
#########################################################################

import time

# IMPOSTAZIONE INIZIALE COSTANTI (ORA FINE GIORNATA LAVORATIVA)
ora_fine = 17
minuti_fine = 00 
secondi_fine = 59 

  
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

    print "                 "
    print "MALANDRINO NON FARE IL FURBO !!!!!!!!"
    print "La tua giornata di lavoro e' gia' finita...spegni il pc e fila!!! "
    print "----------------------------------------------------------------"
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

   # CALCOLO ORE, MINUTI, SECONDI MANCANTI
   ore_mancanti = ora_fine - time_int[0]
   minuti_mancanti = minuti_fine - time_int[1]
   secondi_mancanti = secondi_fine - time_int[2]

   somma_secondi_attuali = (time_int[0]*3600)+(time_int[1]*60)+time_int[2]
   differenza_secondi = somma_secondi_fine - somma_secondi_attuali
 
   print "                 "
   print " TIENI DURO !!!                    **************"
   print "                                   * Count-down *"
   print "                                   **************"
   print " Alla fine mancano solo : ",ore_mancanti,"Ore -",minuti_mancanti,"Minuti -",secondi_mancanti,"Secondi"
   print " "
   print "----------------------------------------------------------------"
   time.sleep(1)


while 1>0:
   print "                 "
   print "E' FINITAAAAAAAAAAAAAAAAAA TUTTI A CASAAAAAAAAAAAAAA !!!!!!!!"
   print "Spegni il pc e fila"
   print "----------------------------------------------------------------"
   time.sleep(1)
 
