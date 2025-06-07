print("questo programma riceve in input la temperatura dell'acqua, in gradi Celsius o Fahrenheit, e ne restitutisce lo stato\n")
t=float(input("inserire la temperatura:"))
scala=input("inserire C(celsius) o F(fahrenheit)")

if scala.capitalize()=="C":

    if t>=100:
        print("gassoso")
        
    if t<=0:
        print("solido")
        
    if t>0 and t<100:
        print ("liquido")

if scala.capitalize()=="F":

    if (t-32)/1.8>=100:
        print("gassoso")
        
    if (t-32)/1.8<=0:
        print("solido")
        
    if (t-32)/1.8>0 and (t-32)/1.8<100:
        print("gassoso")
    
