s=input("Inserisci una stringa:")
tot=0
if s== s[::-1]:
    print("Il livello di plindromicità è:",len(s))
else:
    for x in range(1,len(s)):
        if s[x-1] == s[-x]:
            tot = tot + 1
        else:
            break
        
print("Il livello di palindromicità è:", tot)
