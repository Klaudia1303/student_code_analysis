s: str = ''
count: int = 0
while ('a' not in s) or ('c' not in s):
    s = input('stringa: ')
    count += 1
print(count)
