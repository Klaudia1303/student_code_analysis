#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.6

numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

for i in range (1, len (numeraleAlieno)):
    numerAli = 0;
    base = i;
    esponente = 0;

    for i in numeraleAlieno [::-1]:
        numerAli += int (i)*(base**esponente);
        esponente += 1;
    if numerAli == numeroTerrestre:
        print (base);
        break;