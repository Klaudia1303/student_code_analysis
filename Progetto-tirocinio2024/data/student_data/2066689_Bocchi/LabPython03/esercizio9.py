n = int(input('numero intero: '))
i=2
fine = True

while i<n:
    if n%i == 0:
        fine = False
    i = i+1
if fine and (n!=1):
    print('numero primo')
else:
    print('numero non primo')
