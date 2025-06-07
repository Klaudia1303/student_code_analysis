s1: str = input('> ')
s2: str = input('> ')
maxSeq: str = ''
for i in range(len(s1)):
    for n in range(len(s1), -1, -1):
        if s1[i:n] in s2 and len(s1[i:n]) > len(maxSeq):
            maxSeq = s1[i:n]
print(maxSeq)
