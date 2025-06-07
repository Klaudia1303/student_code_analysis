s=input()
for el in s:
    if s.count(el)>1:
        print("True")
        break
else: print("False")