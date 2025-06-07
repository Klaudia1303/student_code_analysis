i = 0
while i == 0:
    s = str(input("scrivi una parola : "))
    if s != "" and (not (s.islower()) or not(s.isalpha())):
        len(s)
        print(s[0:1]+s[:-2:-1])

    else: i = 1
print ("non hai inserito una  parola giusta") 