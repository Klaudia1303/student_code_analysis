s=input("Inserisci una stringa: ")
count=0
for i in range(0,len(s)):
    if s[i]==s[len(s)-1-i]:
        count+=1
    else:
        break
    if i==len(s)//2-1:
        break
print(count)
