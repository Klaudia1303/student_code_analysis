s=input("Inserire una stringa:   ")
if s[0]==s[len(s)-1]:
    print("Carattere iniziale e finale uguali"),
elif s[0]!=s[len(s)-1]:
    print("Carattere iniziale e finale diversi")
