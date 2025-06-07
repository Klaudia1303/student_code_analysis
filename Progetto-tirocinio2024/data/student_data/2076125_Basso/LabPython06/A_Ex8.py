

s1=input("Inserire stringa:\t")
s2=input("Inserire stringa:\t")
n=int(input("Inserire intero:\t"))


for a in range(len(s1)):
    if a-n<0:
        if s1[a] in s2[:a+n+1]:
            print(s1[a], end='')
    else:
        if s1[a] in s2[a-n:a+n+1]:
            print(s1[a], end='')
