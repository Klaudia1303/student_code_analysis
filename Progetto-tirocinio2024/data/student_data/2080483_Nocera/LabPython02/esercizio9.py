#Scrivere un programma che chiede in input all’utente due interi che rappresentano un mese ed un anno e
#stampa a schermo i due interi corrispondenti al mese successivo. Il programma inoltre deve controllare che
#l’intero inserito per il mese sia compreso tra 1 e 12 (estremi inclusi). Nel caso in cui quest’ultima condizione
#non sia rispettata, il programma deve stampare “input non valido”.
a = int(input("inserisci un anno :") )
m = int(input("inserisci un mese :") )
if  0<=m<=12:
    if m==12:
        print(1,a+1)
    else:
        print(m+1,a)
else:
    print("input non valido")
    
       

    
