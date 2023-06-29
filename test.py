N = input("enter something: ")

if len(N) != 3:
    print("You must to enter a three-digit number")
else:
    N = int(N)
    a = N//100
    b = (N//10) % 10
    c = N % 10
    print(sum([a, b, c], 0))
