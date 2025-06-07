n1=int(input('velocità primo viaggiatore: '))
n2=1
giorni=1
k=20
for i in range(2,1000):
    if n2>=k:
        break
    else:
        k+=n1
        n2+=i
        giorni+=1
print('giorni=',giorni)

    
