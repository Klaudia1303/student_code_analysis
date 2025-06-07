num=input('inserisci un numero maggiore di zero: ')
num=int(num)
div=0
while div<=num:
    div=div+1
    if num%div==0:
        print(div)
    else:
        print('')
