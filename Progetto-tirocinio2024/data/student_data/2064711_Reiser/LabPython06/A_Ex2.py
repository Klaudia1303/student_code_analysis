s=str(input("inserisci una stinga:"))
l=len(s)
if l==1: print("stringa polindroma di livello 1")
else:
    for i in range(0,len(s)):
        if s[i]!=s[l-i-1]:
            break
    if i==0: print("stringa non palindroma(livello 0)")
    elif s==s[::-1]: print("stringa completamente palindroma(livello",l,")")
    else: print(s,"è palindroma di livello",i)
