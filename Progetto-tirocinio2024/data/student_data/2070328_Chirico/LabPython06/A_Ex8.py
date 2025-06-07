s1 = input()
s2 = input()
s3 = ''

n = int(input())


for i in range(len(s1)):
    if s2.find(s1[i]) != -1:
        if  0 <= abs(i - s2.find(s1[i])) <= n or 0 <= abs(i - s2.rfind(s1[i])) <= n:
                s3 = s3+s1[i]

print(s3)
                

