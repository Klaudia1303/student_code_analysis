s=input("Inserisci una stringa: ")
M=int(s.rfind(s[0])-s.find(s[0]))
for i in range(len(s)):
    if(s.rfind(s[i])> i):
        if((s.rfind(s[i])-s.find(s[i]))>M):
            M=(s.rfind(s[i])-s.find(s[i]))
print(M)
