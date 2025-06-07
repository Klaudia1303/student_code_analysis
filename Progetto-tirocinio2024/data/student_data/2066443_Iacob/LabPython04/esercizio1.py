stop = False
sum_s = 0
while not stop:
    s = str(input('Insert string: '))
    sum_s = sum_s + 1
    i = 0
    while i<len(s):
        read = s[i]
        i = i+1
        if read=='c':
            while i<len(s):
                read = s[i]
                i = i+1
                if read=='a':
                    stop = True
print(sum_s)
