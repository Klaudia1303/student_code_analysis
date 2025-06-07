#Scrivere un programma che chiede in input all’utente due interi che rappresentano un mese ed un anno e
#stampa a schermo i due interi corrispondenti al mese successivo. Il programma inoltre deve controllare che
#l’intero inserito per il mese sia compreso tra 1 e 12 (estremi inclusi). Nel caso in cui quest’ultima condizione
#non sia rispettata, il programma deve stampare “input non valido”. Esempi:
#a. Inserendo i valori 10 e 2017, stampa “11 2017”;
#b. Inserendo i valori 12 e 2017 stampa “1 2018”;
#c. Inserendo i valori 13 e 2018 stampa “input non valido”.
mese=int(input("Inserisci un mese: "))
anno=int(input("Inserisci un anno: "))
if(mese>12 or mese<1):
    print("input non valido");
else:
    if(mese==12):
        mese=1
        anno+=1
        print(mese, anno)
    else:
        mese+=1
        print(mese, anno)
