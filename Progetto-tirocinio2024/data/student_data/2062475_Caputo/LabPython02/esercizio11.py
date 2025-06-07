t = int(input("inserire la temperatura t: "))
if (t <= 10):
    print ("freddo")
elif (10 < t and t <= 20):
    print ("gradevole")
elif (20 < t and t <= 30):
    print ("caldo")
else:
    print ("molto caldo")
