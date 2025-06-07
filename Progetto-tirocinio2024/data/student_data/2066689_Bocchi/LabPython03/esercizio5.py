s= input('stringa: ')

while s.islower()== False or s.isalpha()== False:
    s= input('stringa: ')
print(s[0], s[-1])
