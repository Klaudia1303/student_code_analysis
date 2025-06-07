s=input("Inserire una stringa")
cond = False
for i in range (len(s)):
    if(s.count(s[i])>1):
        cond = True
print(cond)
