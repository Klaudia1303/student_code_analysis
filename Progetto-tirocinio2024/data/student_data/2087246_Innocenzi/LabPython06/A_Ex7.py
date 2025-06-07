s1=input("Inserisci una stringa: ")
s2=input("Inserisci una stringa: ")
j=''
k=0
massimo=0
if(len(s1)>len(s2)):
    massimo=len(s1)
else:
    massimo=len(s2)

while k<(massimo):
    i=0
    if k<len(s1):
        if s1[k] in s2:
            while s1[k:k+i] in s2:
                i+=1
            if len(s1[k:k+i-1])>len(j):
                j=s1[k:k+i-1]
    else:
        break
    k+=1

print(j)
        