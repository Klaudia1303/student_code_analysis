s=input("inserisci una stringa ")
a=" "
while s[0]!=a[-1]:
    a=s
    s=input("inserisci una stringa ")
    
print(a+" "+s)
