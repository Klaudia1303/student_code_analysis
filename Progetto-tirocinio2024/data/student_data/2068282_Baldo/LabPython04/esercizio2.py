ast = False
i = 0
while not ast:
    if n == "*":
        ast = True
    elif int(n) > 0:
        i += 1
print(i)
