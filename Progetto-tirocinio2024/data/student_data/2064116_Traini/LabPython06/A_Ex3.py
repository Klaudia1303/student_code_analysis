#Scrivere un programma Python che stampa la tabellina pitagorica dei numeri in base ottale. Usare due cifre, 
#e.g., 02x04=10
v=''
a=''
b=''
c=''
for i in range(0,8):
    for j in range(1,8):
        n=i*j
        if n%8!=0:
            v=n%8
            a=(n-v)//8
            b='0'+str(i)
            c='0'+str(j)
            print(str(b),'X',str(c),'=',str(a)+str(v))
            
