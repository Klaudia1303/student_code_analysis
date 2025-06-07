i=0
s="."
while i==0:
    n=input("inserisci una parola :")
    if s[-1] == n[0]:
        i=1
    else:
        s=n
print(s,n)
