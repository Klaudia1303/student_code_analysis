s=input('Please enter a word: ')
n=int(input('Please enter a number. If i find two character that are the same distant \'n\' from eachother I will print \'True\': '))
found=False
while n<=0:
    print('The number must be greater than 0: ')
    n=int(input('Please enter a number. If i find two character that are the same distant \'n\' from eachother I will print \'True\': '))
for i in range(len(s)):
    test=i+n
    if test>len(s)-1:
        break
    if s[test]==s[i]:
        found=True
        break

print(found)
