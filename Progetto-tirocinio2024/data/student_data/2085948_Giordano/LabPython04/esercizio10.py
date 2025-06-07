s=str(input("Inserisci una stringa: "))
s2=str(input("Inserisci una stringa: "))
s3=str(input("Inserisci una stringa: "))
while not slen(s)+len(s2)==len(s3):
    s=str(input("Inserisci una stringa: "))
    if not len(s3)+len(s2)==len(s):
        s2=str(input("Inserisci una stringa: "))
        if not len(s)+len(s3)==len(s2):
            s3=str(input("Inserisci una stringa: "))
        else:
            break    
    else:
        break
print(s,"",s2,"",s3)
