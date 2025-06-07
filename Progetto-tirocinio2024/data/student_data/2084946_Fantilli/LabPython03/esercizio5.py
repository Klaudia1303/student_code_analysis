s = input()
while (s.isalpha() and s.islower()) is False:
    print(s[0:1]+s[(len(s)-1):len(s)])
    s = input()
if (s.isalpha() and s.islower()) is True:
    print(s[0:1]+s[(len(s)-1):len(s)])
