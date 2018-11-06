n = int(input())

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and n in range(2, 5 + 1):
    print("Not Weird")
elif n % 2 == 0 and n in range(6, 20 + 1):
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")