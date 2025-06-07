print("questo programma prende in input una temperatura e restitutisce un feedback\n")
t=int(input("inserire la temperatura:"))

if t>30:
    print("molto caldo")
    
if t>20 and t<=30:
    print("caldo")

if t>10 and t<=20:
    print("gradevole")

if t<=10:
    print("freddo")
    
