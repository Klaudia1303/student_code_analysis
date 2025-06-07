s=input()
c=len(s)
liv=0
for i in range(c):
    if s[i]== s[(c-1)-i]:
        liv+=1
    else:
        break

print(liv)
