s= input('stringa: ')
tots=1

while not (s.count('c') and s.count('a')):
    s= input('stringa: ')
    tots = tots+1
print(tots)
