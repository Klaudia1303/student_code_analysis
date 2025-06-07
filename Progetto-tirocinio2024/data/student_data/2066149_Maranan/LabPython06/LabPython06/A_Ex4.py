for day in range(1, 1001):
    if ((20*day) - (((day**2)+day)/2)) >= 0:
        print(day)
        break
