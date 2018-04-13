def camelcase(s):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total = 1

    for e in uppercase:
        if e in s:
            total += 1

    print(total)
