n = ""
i = 0
stop = "*"
while n != stop:
        n = input("Inserire un numero intero ( * per terminare):")
        if n != stop and int(n) >= 0:
                i += 1
print(i)
