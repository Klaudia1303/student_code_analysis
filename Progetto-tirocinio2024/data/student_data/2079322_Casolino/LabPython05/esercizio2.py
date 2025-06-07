#Scrivere un programma che chiede in input all’utente
#una stringa s ed un intero positivo n e stampa una nuova stringa
#in cui ogni carattere di s è ripetuto n volte. Esempio:
#• inserendo la stringa “casa” e l’intero “2”, il programma stampa ‘ccaassaa’

s = str(input("Inserire una stringa: "))
n = int(input("Inserire un numero intero: "))
for i in range(len(s)):
    print(s[i]*n, end='')
    
