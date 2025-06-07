velocità1=0
velocità2=0
a = 0
for i in range(1,1001):
    velocità1 = velocità1+20
    velocità2 = velocità2+i
    a = a+1
    if velocità2 >= velocità1:
        print(a)
        break
