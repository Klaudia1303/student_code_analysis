b=True; i=0
while b:
    s=input("Inserire una stringa: ")
    i+=1
    for c in s:
        if ("a" and "c") in s:  b=False   
print("Numero stringhe visualizzate prima del termine:",i)
