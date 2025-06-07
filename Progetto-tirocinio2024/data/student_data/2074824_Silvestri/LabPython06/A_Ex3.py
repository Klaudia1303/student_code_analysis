prodotto=1
ottale=''
for i in range(1,9):
    for j in range(1,9):
        prodotto = i*j
        if prodotto<8:
            print(prodotto,''*2,end='')
        if prodotto >= 8 and prodotto <= 56:
            primo= prodotto//8
            secondo=prodotto%8
            print(str(primo)+str(secondo), '', end= '')
        if prodotto == 64:
            print(100, end= '')
print()
        
