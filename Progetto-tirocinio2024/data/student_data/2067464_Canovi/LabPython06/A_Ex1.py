n1 = int(input("inserisci un intero maggiore di 0: "))
n2 = int(input("inserisci un altro intero maggiore di 0: "))

div = n1
numDiv = 0

while div >= 2:
    if n1 % div == 0:
        if n2 % div == 0:
            numDiv == numDiv
        else:
            print(div)
            numDiv += 1
    div -= 1
        
