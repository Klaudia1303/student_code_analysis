x = input('Inserire un numeo intro (* per terminare): ')
i = 0

while x!='*':
    x = int(x)
    if x>=0:
        i+=1
    x = input('Inserire un numeo intro (* per terminare): ')
print(i)
