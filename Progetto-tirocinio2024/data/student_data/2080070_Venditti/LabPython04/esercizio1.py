s='?'
c=0
a=0
count_s=0
while (c and a)==0:
       s=input('inserisci una stringa')
       c=s.count('c')
       a=s.count('a')
       count_s +=1
if (c and a)!=0:
       print(count_s)
                           
