s = input("Inserire una stringa:")

for x in s:
    if s.count(x) > 1:
        print("True")
        break
    else:
        print("False")
        break
    
