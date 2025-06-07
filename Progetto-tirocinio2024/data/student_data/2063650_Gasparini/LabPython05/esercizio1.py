a = input("Stringa 1: ")
b = input("Stringa 2: ")

s = ""
for i in range(len(a)):
    s += a[i] + b[i]
print(s)
