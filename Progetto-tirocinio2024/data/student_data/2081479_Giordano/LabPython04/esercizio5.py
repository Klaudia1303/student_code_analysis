number=int(input('insert a number: '))
if number>1:
    for fact in range(1,number):
        number*=fact
    print(number)
elif number>=1:
    print(1)