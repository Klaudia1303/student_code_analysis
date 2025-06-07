numero = int(input( "inserisci un numero: "))
if numero<=1:
    print("devi inserire un numero maggiore di 1")
else :
    div = 2
    count=0
    while div<=numero/2 and count == 0:
        if numero%div==0:
            count+=1
        div+=1
    if count==0:
        print("numero Primo")
    else:
        print("il numero non è primo")



