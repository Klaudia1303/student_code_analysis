n = int(input('Insert odd n>3: '))
sp = 0
for i in range(1,n+1,2):
    s = ' '*((n//2)-sp)
    sp = sp+1
    ch = '*'*i
    print(s+ch)
