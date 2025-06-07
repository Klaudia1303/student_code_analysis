n = int(input('Insert number n>=0: '))
if n==0 or n==1:
    print('1')
elif n>1:
    fac_n = 1
    i = n
    while i>0:
        fac_n = fac_n*i
        i = i-1
    print(fac_n)
else:
    print('Error')
