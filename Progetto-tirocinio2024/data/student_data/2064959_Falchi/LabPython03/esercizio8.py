done = False

msg = "Inserire una stringa palindroma: "

while not done:
    s = input(msg)

    if s == s[::-1]:
        print("stringa palindroma di lunghezza", len(s))
        done = True
    else:
        msg = "stringa non palindroma, inserire una stringa palindroma: "
