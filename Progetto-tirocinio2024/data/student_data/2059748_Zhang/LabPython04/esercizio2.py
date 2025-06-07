x=True
i=0
while x:
    n=input("scrivi un intero: ")
    if n[1:].isdecimal() and n[0]=='-':
        ''
    elif n=="*":
        x=False
        print(i)
    elif n.isdecimal():
        i+=1
