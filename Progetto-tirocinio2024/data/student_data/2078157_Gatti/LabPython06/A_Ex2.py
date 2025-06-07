s = input('inserisci una stringa: ')
a = 0
if s[::] == s[::-1]:
    print(len(s))
elif len(s) % 2 == 0:
    for i in range(len(s)//2):
        if s[i] == s[-i - 1]:
            a = a + 1
        else:
            break
    print(a)
else:
    for i in range(len(s)//2 - 1):
        if s[i] == s[-i - 1]:
            a = a + 1
        else:
            break
    print(a)
