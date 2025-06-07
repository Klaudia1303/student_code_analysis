#Scrivere un programma che prende in ingresso una sequenza di stringhe, una per una in maniera iterativa,
#e termina la richiesta di inserimento in input quando l’ultimo carattere della stringa precedente è uguale
#al primo carattere di quella attuale. Prima di terminare il programma stampa su un'unica riga le ultime
#due stringhe inserite, separate da uno spazio.
#Esempio:
#•
#Inserendo in questo ordine le stringhe “pippo”, “casa”, “albero”, il programma termina stampando“casa albero”.
#Nota: Si assuma che il programma riceva in ingresso sempre almeno due stringhe e che le stringhe in
#ingresso non siano mai vuote.
s1=""
s=input("inserisci una stringa : ")

while True:

    if s1 == "" or s1[-1]!=s[0]:
        s1=s
        s=input("inserisci una stringa : ")
    elif s1[-1]==s[0]:
        break
print(s1, s)
    
