n=input('please enter a number: ')
sumN=0
while n!='*':
    if '-' in n:
        sumN+=int(n)
    n=input('please enter a number: ')
print(sumN)
