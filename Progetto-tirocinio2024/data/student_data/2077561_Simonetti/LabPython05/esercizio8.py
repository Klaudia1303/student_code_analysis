base=int(input('please type a whole number: '))
while base%2==0 and base<=3:
    print('The number must be a odd number and positive.',end='')
    base=int(input('please type a whole number: '))
spaces=(base-1)//2
ast=0
for i in range (base//2+1):
    print((spaces-i)*' '+'*'*(ast+1))
    ast+=2
