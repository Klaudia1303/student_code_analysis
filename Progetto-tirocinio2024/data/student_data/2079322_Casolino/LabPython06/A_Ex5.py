#Scrivere un programma Python che riceve in ingresso una stringa alfanumerica
#non vuota s e stampa il carattere con più occorrenze consecutive
#e il numero di occorrenze dello stesso. Se due caratteri condividono
#il massimo numero di occorrenze il programma stampa il secondo.
#Ad esempio, se s vale 'a32ppp7666' il programma stampa 6 3.

s = input("Inserire una stringa alfanumerica: ")
contatore=0
for i in range(len(s)-1,-1,-1):
    if s[i-1]==s[i]:
        i-=1
        print(s[i],s.count(s[i]))
        break
