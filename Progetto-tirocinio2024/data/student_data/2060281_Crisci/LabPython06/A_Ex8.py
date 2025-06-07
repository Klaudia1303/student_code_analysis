s1=input("Inserire una stringa: ")
s2=input("Inserire un'altra stringa: ")
n=int(input("inserire un intero: "))
risultato=''
for i in range(len(s1)):
        if(s1[i] in s2):
            posizione=s2.find(s1[i])
            if(-n<=i-posizione<=n):
                risultato=risultato+s1[i]
print(risultato)
