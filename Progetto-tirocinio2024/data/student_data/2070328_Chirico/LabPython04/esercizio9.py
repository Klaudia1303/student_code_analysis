#Successione di Fibonacci

n = int(input("intero = "))
a = 0
b = 1
print(1)

while n > 1:
    i = a+b
    print(i)
    a = b
    b = i
    n = n-1
    
