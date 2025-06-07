s=input("Inserisci un numero>> ")
count=0
while s!="*":
    if int(s)>0:
        count=count+1
    s=input("Inserisci un numero>> ")
print(count)
