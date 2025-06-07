s=input("scrivi una stringa: ")
n=int(input("scrivi un intero positivo: "))


for i in range(len(s)):
    x=s[i]
    print(x*n,end='')
