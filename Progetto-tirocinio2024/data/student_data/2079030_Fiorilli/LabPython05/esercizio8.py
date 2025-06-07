b=0
while b<3 or b%2==0:
    b=int(input('inserisci la base dispari del trangolo isoscele da rappresentare: '))
for i in range (1, b+1, 2):
    print (' '*(b//2-i//2), '*'*i)
