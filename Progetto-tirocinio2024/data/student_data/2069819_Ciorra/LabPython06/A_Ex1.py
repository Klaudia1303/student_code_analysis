n1=int (input(" primo numero intero > 0 : "))
n2=int( input(" secondo numero intero > 0 : "))

divi = []
for i in range(1,n1+1):
    if n1 % i ==0:
        if n2 % i !=0:
            divi.append(i)

divi.reverse()
print(divi)
    
