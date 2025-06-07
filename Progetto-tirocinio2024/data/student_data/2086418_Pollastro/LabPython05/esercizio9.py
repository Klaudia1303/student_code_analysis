l= int(input('inserire il lato del quadrato: '))

for c in range(l):
    if c==0:
        print(l*'*')
    elif 0<c<l-1:
        print('*'+str(' '*(l-2))+'*')
    else:
        print(l*'*')
