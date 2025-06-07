k = 0
for i in range(1, 8):
    s = ""
    for j in range(1, 8):
        a = ""
        num = i * j
        while k == 0:
            a = a + str(num % 8)
            if (num // 8) == 0:
                break
            num = num // 8
        b = a[::-1]
        if len(b) < 2:
            b = "0" + b
        s = s + b + " "
    print(s)
            


