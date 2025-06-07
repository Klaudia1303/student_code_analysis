s1 = input('stringa 1 = ')
s2 = input('stringa 2 = ')

for i in s1:
    if s2.find(i) == -1:
        print(i, end='')
