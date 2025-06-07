s1=input('inserire stringa: ')
s2=input('inserire stringa: ')
n=int(input('inserire numero intero: '))
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j] and n>=abs(i-j):
            print(s1[i],end='')
            break
