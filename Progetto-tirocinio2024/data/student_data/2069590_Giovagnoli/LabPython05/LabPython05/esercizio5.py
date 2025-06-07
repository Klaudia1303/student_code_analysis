s=input("Inserire una stringa che contenga almeno 2 caratteri: ")
n=int(input("Inserire un intero positivo: "))
carattere=""
contatore=0
if len(s)>=2 and n>0:
    for i in range(len(s)):
        carattere=s[i]
        if i+n<len(s):
            if carattere==s[i+n]:
                contatore+=1
    if contatore>0:
        print("True")
    else:
        print("False")
        