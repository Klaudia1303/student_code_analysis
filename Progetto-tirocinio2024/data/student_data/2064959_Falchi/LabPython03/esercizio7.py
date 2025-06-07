c = input("Inserire catattere: ")

done = False
i = 0

count = 0
while not done:
    s = input("Inserire una stringa: ")

    while i <= len(s):
        if s[i:i+1] == c:
            count = count + 1
        i = i + 1
    if count >= 2:
        print(count)
        done = True
    else:
        count = 0
        i = 0
