w= True

while w:
    s = input()
    if str(s) == str(s[::-1]):
        print('palindroma')
    else:
        print('non palindroma')