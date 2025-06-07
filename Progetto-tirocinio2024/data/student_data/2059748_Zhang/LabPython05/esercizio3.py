s1=input("scrivi una stringa: ")
s2=input("scrivi un'altra stringa: ")

for i in s1:
    if i not in s2:
        print(i,end='')
