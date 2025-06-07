termina=False
p=input("immetti una stringa: ")
while not termina:
    s=input("immetti una stringa: ")
    if s[0]==p[-1]:
        termina=True
    else:
        p=s
print(p,s)
