s1=str(input("Inserire una stringa:"))
s2=str(input("Inserire una stringa:"))
n=int(input("Inserire un numero:"))
risposta=''
for i in range(len(s1)):
    ex1=i-n
    ex2=i+n+1
    if ex1<0:
        ex1=0
    if ex2>len(s1):
        ex2=len(s1)
    if s1[i] in s2[ex1:ex2]:
        risposta=risposta+s1[i]
print(risposta)


    
    


