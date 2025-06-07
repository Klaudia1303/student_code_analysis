s = input("Inserire una stringa palindroma: ")
i=0
contatore = 0
while i<(len(s)//2):
    #print((len(s)//2))     print di controllo
    if s[i]==s[(-i-1)]:
        contatore+=1
        i+=1
    else:
        print("non palindroma, ", end="")
        s = input("Inserire una stringa palindroma: ")
        i=0
if contatore == (len(s)//2):
    print("Stringa palindroma di lunghezza ",len(s))