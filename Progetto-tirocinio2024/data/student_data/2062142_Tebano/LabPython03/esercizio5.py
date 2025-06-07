m=input()
while m.islower()==False or m.isalpha()==False:
    print(m[0]+m[-1])
    m=input()
print(m[0]+m[-1])    
