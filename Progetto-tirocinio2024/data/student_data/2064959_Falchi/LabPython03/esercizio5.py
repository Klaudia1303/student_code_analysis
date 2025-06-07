stringa = input("Inserire una stringa: ")

if stringa.isalpha() and stringa.islower():
     print(stringa[:1] + stringa[len(stringa)-1:])
else:
    while not (stringa.isalpha() and stringa.islower()):
        stringa = input("Inserire una stringa: ")

        if stringa.isalpha() and stringa.islower():
            print(stringa[:1] + stringa[len(stringa)-1:])
