string=input('Please enter a word to check the palindrome level: ')
i=0
level=0
rString=string[::-1]
while string[i]==rString[i]:
    level+=1
    i+=1
print('The palindrome level for',string,'is',level)
