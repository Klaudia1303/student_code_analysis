a = int(input('Insert number: '))
b = int(input('Insert times: '))
if b>0:
    i = b
    mul_pos=0
    while i>0:
        mul_pos = mul_pos+a
        i = i-1
    print(mul_pos)
elif b<0:
    i = b
    mul_neg=0
    while i<0:
        mul_neg = mul_neg-a
        i = i+1
    print(mul_neg)
elif b==0:
    print('0')
else:
    print('unexpected error')
