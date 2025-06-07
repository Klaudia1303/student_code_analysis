s=input("inserisci stringa: ")
k=0
for i in range(len(s)):
    if s.rfind(s[i])-i>k:
        k=s.rfind(s[i])-i
print(k)
