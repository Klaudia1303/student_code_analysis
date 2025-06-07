from gettext import find


c = input("insersici il carattere: ")
s = input("insersici la stringa: ")
while s.count(c)<=2:
    s = input("insersici la stringa: ")
print(s.count(c))