x = input('Inserire un numeo intro (* per terminare): ')
s = 0

while x!='*':
    x = int(x)
    if x<0:
        s+=x
    x = input('Inserire un numeo intro (* per terminare): ')
print(s)
