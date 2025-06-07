n = int(input('base del triangolo isoscele = '))
j = 1

while n%2 == 0 or n == 1:
    n = int(input('base del triangolo isoscele = '))
    
for i in range(int(n/2),-1,-1):
        print(' '*i+'*'*j)
        j = j+2
    
