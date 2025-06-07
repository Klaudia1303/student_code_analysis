s1 = input("stringa: ")
s2 = input("stringa2: ")
n = int(input("numero: "))

for i in range(len(s1)):
    if s1[i] in s2 and s2.rfind(s2[i]) - s1.find(s1[i]) <= n:
        print(s1[i], end="")
        
               
