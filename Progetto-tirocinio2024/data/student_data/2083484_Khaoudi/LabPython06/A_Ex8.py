s1=input("Inserisci una stringa : ")
s2=input("Inserisci una stringa : ")
n=int(input("Inserisci un numero intero : "))

newString=[]
for i in range(n):
    if i > n:
        break
    if s2.find(s1[i]) != -1:
                newString+=s1[i]

        

print(newString)