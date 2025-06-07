n = int(input('Insert integer here: '))
d = 2
c = 0
while d<=n//2 and c==0:
    if n%d==0:
        c = c+1
        d = d+1
if c==0:
    print('Numero primo')
else:
    print('Numero non primo')
