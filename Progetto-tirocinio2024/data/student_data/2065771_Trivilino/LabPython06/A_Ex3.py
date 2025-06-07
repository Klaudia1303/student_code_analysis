def base10abase8(num):
    ottale=''
    if num > 7:
        while num>=1:
            resto=num%8
            num=num//8
            ottale=str(resto)+ottale
    else:
        ottale=num
    
    return(int(ottale))

for i in range(11):
    for j  in range(11):
        print(base10abase8(i*j),'\t',end='')
    print()
