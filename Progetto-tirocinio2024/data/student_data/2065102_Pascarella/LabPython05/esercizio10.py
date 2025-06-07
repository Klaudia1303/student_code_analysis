n=int(input())

print("*"*n)                        #Base superiore del quadrato (riga 1)
for i in range(0, n-2):             
    print("*",end="")               # * iniziale della riga
    for x in range(0, n-2):
        if x==i or x==(n-i-3):      
            print("*", end="")      # * quando mi trovo in una casella dove i=x
        else:
            print(" ", end="")      # " " quando mi trovo in una casella dove i!=x
    print("*")                      # * finale della riga
print("*"*n)                        #Base inferiore del quadrato
    
