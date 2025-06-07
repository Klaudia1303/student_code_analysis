#9) Scrivere un programma che chiede in input all’utente due interi che rappresentano un mese ed un anno e
#stampa a schermo i due interi corrispondenti al mese successivo. Il programma inoltre deve controllare che
#l’intero inserito per il mese sia compreso tra 1 e 12 (estremi inclusi). Nel caso in cui quest’ultima condizione
#non sia rispettata, il programma deve stampare “input non valido”. Esempi:
#a. Inserendo i valori 10 e 2017, stampa “11 2017”;
#b. Inserendo i valori 12 e 2017 stampa “1 2018”;
#c. Inserendo i valori 13 e 2018 stampa “input non valido”.

var1=input('inserisci un anno: ')
var2=input('inserisci un mese: ')

v1=int(var1)
v2=int(var2)

if v2>0 and v2<12:
    print(v1, v2+1)
elif v2==12:
    print(v1+1, '1')
    
