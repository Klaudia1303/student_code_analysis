s1=input("inserisci una parola :")
s2=input("inserisci una parola :")
n=int(input("inserisci una distanza :"))
accdist=""
for i in range(len(s1)):
    acc=""
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            acc=acc+s1[i]
    if  abs(s1.find(acc)-s2.find(acc))<=n:
       accdist=accdist+acc
print(accdist)
