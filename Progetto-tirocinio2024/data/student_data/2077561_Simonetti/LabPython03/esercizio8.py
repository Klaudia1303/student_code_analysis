s=input('please type a palindrome word or sentence: ')

while s[:]!=s[::-1]:
    print('not a palindrome. Try again: ')
    s=input('please type a palindrome: ')
print(s,'is a palindrome!')
    
    
