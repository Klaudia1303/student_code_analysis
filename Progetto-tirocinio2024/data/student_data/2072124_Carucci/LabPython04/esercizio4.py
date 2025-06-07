n = int(input('Inserire un numeo intro (0 per terminare): '))
s = 0

while n!=0:
    if (n%3)==0:
        s+=n
    n = int(input('Inserire un numeo intro (0 per terminare): '))
print(s)
