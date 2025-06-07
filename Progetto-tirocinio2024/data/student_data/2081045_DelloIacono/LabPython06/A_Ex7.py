s1 = input("Inserire una stringa: ")
s2 = input("Inserire una stringa: ")
mass = 0
car = 0
for i in range (len(s1)):
    for j in range (i+1, len(s1)+1):
        s = s1[i:j]
        if s in s2:
            l = j-i
            if l>=mass:
                mass = l
                car = s
            else:
                break
print(car)
                

                
