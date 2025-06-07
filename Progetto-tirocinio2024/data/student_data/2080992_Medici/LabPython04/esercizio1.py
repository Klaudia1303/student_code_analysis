i=1
tot=0
while i!=0:
    s=str(input('inserisci una stringa: '))
    tot+=1
    if s.count('c')!=0 and s.count('a')!=0:
        print(tot)
        break
