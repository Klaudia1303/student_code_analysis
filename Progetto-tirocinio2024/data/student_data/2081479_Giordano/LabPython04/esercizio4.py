finish=False
total=0
while not finish:
    number=int(input('Insert number: '))
    if number==0:
        finish=True
    elif number%3==0:
        total+=number
print(total)