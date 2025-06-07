s=input("inserire una stringa alfanumerica: ")
maggiore=1
i=1
f=s[len(s)-1]
for j in range(1,len(s)):
    if s[j]==s[j-1]:
        i+=1
        if i>=maggiore:
            maggiore=i
            f=s[j]
    else:
        i=1
print(f,maggiore)
