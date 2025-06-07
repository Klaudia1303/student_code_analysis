##5. Scrivere un programma Python che riceve in ingresso una stringa alfanumerica non vuota s e stampa il
##carattere con più occorrenze consecutive e il numero di occorrenze dello stesso. Se due caratteri condividono
##il massimo numero di occorrenze il programma stampa il secondo. Ad esempio, se s vale 'a32ppp7666' il
##programma stampa 6 3.

s=(input('inserire una stinga alfanumerica: '))
x=0
y=0
for i in range(len(s)):
    if s.count(s[0+i])>=x:
        x=s.count(s[0+i])
        y=s[0+i]
print(x,y)


