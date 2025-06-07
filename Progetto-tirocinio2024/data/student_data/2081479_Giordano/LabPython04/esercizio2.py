finish=False
posCount=0
while not finish:
    inputString=(input('insert a number: '))
    if inputString=='*':
        finish=True
    elif int(inputString)>=0:
        posCount+=1
print(posCount)
