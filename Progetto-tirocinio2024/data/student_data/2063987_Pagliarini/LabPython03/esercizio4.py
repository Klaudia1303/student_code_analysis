x=int(input())
y=int(input())
i=0
if 0<=x<=10 and 0<=y<=10:
    while i<=10:
        if i!=x and i!=y:
            print(i)
        i+=1
else:
    print("il numero deve essere compreso tra 0 e 10")
        
