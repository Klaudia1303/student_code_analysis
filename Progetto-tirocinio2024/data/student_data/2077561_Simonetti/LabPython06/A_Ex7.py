s1=input('Please enter a word: ')
s2=input('Please enter a word: ')
answer = ""
len1, len2 = len(s1), len(s2)
for i in range(len1):
    match = ""
    for j in range(len2):
        if (i+j < len1 and s1[i+j] == s2[j]):
            match += s2[j]
        else:
            if (len(match) > len(answer)): answer = match
            match = ""

print(answer)
