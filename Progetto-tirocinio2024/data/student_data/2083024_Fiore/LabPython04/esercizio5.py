num = int(input("inserisci un numero per farne il fattoriale: "))
counter = num
if num == 0:
    num = 1
   
elif num == 1:
    num = 1
   
else:
    while counter != 1:
        counter -= 1
        num = num*(counter)
        
    
print(num)
