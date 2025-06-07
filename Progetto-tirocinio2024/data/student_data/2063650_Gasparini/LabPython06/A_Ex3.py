for a in range(1, 9):
    for b in range(1, 9):
        r = a * b
        rstr = ""
        if r >= 64:
            rstr = str(r // 64) + str((r // 8) % 8) + str(r % 8)
        else:
            rstr = str(r // 8) + str(r % 8)
        print(
            str(a // 8) + str(a % 8)
            + "x"
            + str(b // 8) + str(b % 8)
            + "="
            + rstr
        )
