last_string = ""
last_char = ""
flag = False

while not flag:
    s = input("Inserisci una stringa: ")

    if last_char == s[0]:
        print(last_string, s)
        flag = True

    last_char = s[-1]
    last_string = s
