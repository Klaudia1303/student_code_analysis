#Scrivere un programma che chiede in input all’utente una stringa s ed un intero positivo n e stampa una 
#nuova stringa in cui ogni carattere di s è ripetuto n volte. Esempio:
#• inserendo la stringa “casa” e l’intero “2”, il programma stampa ‘ccaassaa’
s=str(input('inserisci una stringa: '))
n=int(input('inserire un intero: '))
for a in s:
    print(a*n,end='')
