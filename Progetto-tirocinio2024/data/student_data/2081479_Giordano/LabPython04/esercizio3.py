finish=False
sumTotal=0
while not finish:
    string=input('Insert string: ')
    if string=='*':
        finish=True
    elif int(string)<0:
        sumTotal+=int(string)
print(sumTotal)