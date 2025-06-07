#Scrivere un programma Python che riceve in ingresso una stringa alfanumerica non vuota s e stampa il
#carattere con più occorrenze consecutive e il numero di occorrenze dello stesso. Se due caratteri condividono
#il massimo numero di occorrenze il programma stampa il secondo. Ad esempio, se s vale 'a32ppp7666' il
#programma stampa 6 3.
s=input("Inserisci una stringa : ")
c=0
char=""
i=0
while i<len(s):
    if s.count(s[i]) >=c:
        c=s.count(s[i])
        char=s[i]
    i+=1

print(char, c)
    
