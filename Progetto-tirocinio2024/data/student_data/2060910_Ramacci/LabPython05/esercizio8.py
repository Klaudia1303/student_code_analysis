n=int(input("inserire una base dispari per il triangolo isoscele >= a 3: "))
for i in range(n+1):
    if i%2!=0:
        print(((n-i)//2)*" ","*"*i)
        
