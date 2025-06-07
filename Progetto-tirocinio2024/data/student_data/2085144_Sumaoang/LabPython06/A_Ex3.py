n = 8
octal = 0
count = 1

for x in range(0, n):
    for y in range(1, n):
        decimale = x * y
        resto = decimale % 8
        octal += resto * count
        count *= 10
        decimale = decimale // 8
        print(str(0) + str(x) ,"*", str(0) + str(y), "=", str(decimale) + str(resto))

    
