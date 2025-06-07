#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.1

while True:

    print("Inserire il numero di ore, minuti e secondi nel seguente formato HH:MM:SS, ad esempio 02:23:57: ");
    orario = input();

    ore = int(orario[0:2]);

    secondi = ore * 3600;

    minuti = int(orario[3:5]);
    seconditemp = int(orario[6:8]);
    if minuti > 59 or seconditemp > 59:
        print("Errore di inserimento minuti.", minuti,":",seconditemp, "non è un lasso di tempo valido. Provare con minuti e secondi tra 00 e 59 riprova");
        
    else:
        secondi = secondi + (minuti * 60)
        secondi = secondi + seconditemp;
        print("Il numero di secondi è:", secondi);
        break
