from audioop import mul


number1=int(input('insert a number: '))
number2=int(input('insert a number: '))

for multiplier in range(1,number2):
    result=number1*multiplier
    if result<=number2:
        print(result)