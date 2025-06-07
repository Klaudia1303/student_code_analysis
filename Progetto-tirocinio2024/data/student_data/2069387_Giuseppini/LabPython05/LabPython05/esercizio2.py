#Scrivere un programma che chiede in input all’utente una stringa s ed un intero positivo n e stampa una
#nuova stringa in cui ogni carattere di s è ripetuto n volte.
s=input('inserisci una stringa: ')
n=int(input('inserisci il numero di volte che ogni carattere viene ripetuto: '))
somma=''
for i in range(0,len(s)):
        somma=somma+(s[i]*n)

        
print(somma)   
