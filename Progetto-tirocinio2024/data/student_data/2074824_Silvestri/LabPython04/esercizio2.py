n=(input("Inserire un numero intero (* per terminare):"))
count=0
while str(n)!="*":
    if len(n)>0 and (n.isdecimal() or (n[0] in "+-" and n[1:].isdecimal())):
        n1=int(n)
    else:
        print("Non è un numero intero.")
        n1=0
    if n1>0:
        count+=1
    n=(input("Inserire un numero intero (* per terminare):"))
print("Il numero d interi letti:", count)
    
