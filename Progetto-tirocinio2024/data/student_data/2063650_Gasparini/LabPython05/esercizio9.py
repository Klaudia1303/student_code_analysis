l = int(input("Lato: "))

print("*" * l)
for y in range(1, l - 1):
    print("*" + " " * (l - 2) + "*")
print("*" * l)
