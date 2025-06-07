s=input("Inserire una stringa: ")
somma=0
for i in range(len(s)):
    v=s[i]
    if (s.rfind(v)-s.find(v))>somma:
        somma=s.rfind(v)-s.find(v)
print(somma)
