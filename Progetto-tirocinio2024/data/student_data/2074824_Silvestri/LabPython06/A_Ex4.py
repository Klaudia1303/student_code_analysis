vel1 = int(input("velocità: "))



spazio1 = 0
spazio2 = 0 

giorno = 1

for i in range(1,1001):
    
    spazio2 += i
    spazio1 += vel1
    print(spazio1,spazio2)
    if spazio1 <= spazio2:
        print(i)
        break
        
