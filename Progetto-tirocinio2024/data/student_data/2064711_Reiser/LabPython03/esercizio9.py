numero=int(input("Inserire un numero:"))
if numero<=1:
    print("inserire un numero maggiore di 1")
else:
    div,count=2,0
    while div<=numero/2 and count==0:
        if numero%div==0:
            count+=1
        div+=1
    if count==0:
        print("numero primo")
    else:
        print("numero non primo")
