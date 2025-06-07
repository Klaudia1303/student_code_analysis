def inputAsk():
    number=int(input('Insert a number >0: '))
    if number<=0:
        inputAsk()
    elif number>0:
        divisor=number
        divider(divisor, number)
def divider(divisor, number):
    while divisor>=1:
        if number%divisor==0:
            print(int(number/divisor))
            divisor-=1
        elif number%divisor!=0:
            divisor-=1
inputAsk()