b=int(input('inserisci la misura della base: '))

for i in range(1, b+1, 2):
    print(' '*((b-i)//2) + '*'*i + ' '*((b-i)//2))
    
