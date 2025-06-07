n = int(input("numero: "))
primo = True

i = 2
while i <= n//2:
    if n % i != 0:
        i += 1
    else:
        primo = False
        break

if primo:
    print("numero primo")
else:
    print("numero non primo")
