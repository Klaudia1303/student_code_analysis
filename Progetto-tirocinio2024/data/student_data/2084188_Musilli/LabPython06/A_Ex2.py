s=input("Inserire una stringa per vedere il livello di palindromicità: ")
liv=0; b=True; l=len(s)-1
for i in range(len(s)):
    if s[i]==s[l]:  liv+=1; l-=1
    else: break
print("Livello palindromo:",liv)
