s=input("Inserire una stringa: ")
b=False
for c in s:
    if s.count(c)>1: b=True;    break
print("\nC\'è almeno un carattere che \
compare più di una volta?",b)
