s=input("inserisci una parola: ")
carfi=''
accmax=0
for i in range(len(s)):
    acc=1
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            acc+=1
        else:
            break
    if acc>=accmax:
        accmax=acc
        carfi=s[i]
print(carfi,accmax)   
