
i = 0
c = input("Inserire un carattere:")

while i==0:
    s = input("Inserire una stringa:")
    count = s.count(c)
    if count > 2:
        i=i+1
        print(s)
        print(count)
    else:
        print(s)


    
