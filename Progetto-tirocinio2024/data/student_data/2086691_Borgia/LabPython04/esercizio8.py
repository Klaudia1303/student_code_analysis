s=input("Inserire una stringa: ")
v=''
if s=='':
    print("La striunga non può essere vuota.")
else:
    while v!=s[0]:
        v=s[-1]
        s1=s
        s=input("Inserire una stringa: ")
    print(s1,s)
