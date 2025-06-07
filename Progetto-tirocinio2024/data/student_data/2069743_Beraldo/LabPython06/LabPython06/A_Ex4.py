n1 = 20
n2 = 1
d1 = 0
d2 = 1
g = 0

for i in range(1,1000):

    d1 = d1+20
    d2 = d2+i
    
    '''print("i =", i)
    print("d1 =", d1)
    print("d2 =", d2)'''

    g +=1

    if d2>=d1:
        print(g)
        break
