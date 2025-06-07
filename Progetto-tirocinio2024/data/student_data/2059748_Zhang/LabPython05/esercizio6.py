s=input("inserisci una stringa: ")
x=0

for i in range(len(s)):
    if (s.rfind(s[i])-s.find(s[i]))>x:
        x=s.rfind(s[i])-s.find(s[i])

print(x)
