print('velocità del v1: 20km al giorno')
print('velocità del v2: 1km il primo giorno, 2 il secondo, 3 il terzo...')
v1=20
s2=0
i=1
for i in range(1,1001):
    s1=v1*i
    s2=(i+1)*(i/2)
    if s2>=s1:
        print("giorni necessari al v2 per raggiungere il v1:",i)
        break
