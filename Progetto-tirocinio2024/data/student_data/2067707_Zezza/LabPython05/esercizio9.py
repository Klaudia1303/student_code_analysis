l=int(input('lato intero >=3: '))
for i in range(l):
    if i==0 or i==l-1:
        print('*'*l)
    else:
        print('*'+' '*int(l-2)+'*')
