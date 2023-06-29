N = input("Enter a three-digit number: ")

if len(N) != 3:
    print("You must to enter a three-digit number")
else:
    N = int(N)
    a = N//100
    print(sum([a], 0))

string = "You are the coolest person i've ever known!"