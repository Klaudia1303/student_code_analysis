s = str(input('Insert string: '))
n = int(input('Insert number: '))
mul = ''
for i in range(len(s)):
    mul = mul+(str(s[i]*n))
print(mul)
