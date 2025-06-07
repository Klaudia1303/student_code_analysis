s=input("Inserisci una stringa s: ")
n=int(input("Inserisci un intero n: "))
new=''
for i in range(len(s)):
    new=new+(s[i]*n)
print(new)
