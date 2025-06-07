velocità1=0
velocità2=0
count=0
for i in range(1,1001):
    velocità1+=20
    velocità2+=i

    if velocità2>=velocità1:
        print(i)
        break
