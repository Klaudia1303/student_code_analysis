s=input("Inserire una striga: ")
distanza=0
for i in range(len(s)):
    for x in range(len(s)):
        if s[i]==s[x] and x!=i:
            if (x-i)>distanza:
                distanza=x-i
print(distanza)