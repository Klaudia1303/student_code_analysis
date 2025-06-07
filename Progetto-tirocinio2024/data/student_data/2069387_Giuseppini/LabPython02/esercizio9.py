#Scrivere un programma che chiede in input all’utente due interi che rappresentano un mese ed un anno e
#stampa a schermo i due interi corrispondenti al mese successivo. Il programma inoltre deve controllare che
#l’intero inserito per il mese sia compreso tra 1 e 12 (estremi inclusi). Nel caso in cui quest’ultima condizione
#non sia rispettata, il programma deve stampare “input non valido”. Esempi:
#a. Inserendo i valori 10 e 2017, stampa “11 2017”;
#b. Inserendo i valori 12 e 2017 stampa “1 2018”;
#c. Inserendo i valori 13 e 2018 stampa “input non valido”.

m=int(input('inserisci mese: '))
a=int(input('inserisci anno: '))

if m>12:
     print('input non valido')
elif (m==12):
    print(1,a+1)
elif (m<12):
    print(m+1, a)
    
