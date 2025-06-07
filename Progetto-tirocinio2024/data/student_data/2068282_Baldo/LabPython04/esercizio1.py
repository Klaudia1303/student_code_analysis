ac = True
i = 0
while ac:
    s = input("Inserire una stringa: ")
    if s.count("a") > 0 and s.count("c") > 0:
        ac = False
    i += 1
print(i)
