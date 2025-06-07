#10) Scrivere un programma python che chiede in input all’utente una sequenza di stringhe, una per una in
#maniera iterativa terminando la richiesta di inserimento quando la somma delle lunghezze di due
#stringhe adiacenti (cioè immesse una dopo l’altra) è uguale alla lunghezza della stringa successiva.
#Prima di terminare il programma stampa su un’unica riga le tre stringhe coinvolte nel confronto,
#separate da uno spazio.
#Esempio:
#• Inserendo in questo ordine le stringhe “fondamenti”, “uno”, “due”, “FI1”, “darwin” il
#programma termina stampando “due FI1 darwin”.
#Nota: Si assuma che il programma riceva sempre in ingresso almeno tre stringhe.
s1=""
s2=""
s3=""

while True:
    
    
    if s1 =="" or s2=="" or s3=="":
        s=input("inserisci una stringa :")
        s1=s2
        s2=s3
        s3=s
    if len(s2)+len(s1)==len(s3):
        print(s1,s2,s3)
        break
    else:
        s=input("inserisci una stringa :")
        s1=s2
        s2=s3
        s3=s
