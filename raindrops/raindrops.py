raindrops = int(input("Please enter an integer: "))

if raindrops % 3 == 0:
    print("Pling")

if raindrops % 5 == 0:
    print("Plang")

if raindrops % 7 == 0:
    print("Plong")

if raindrops % 3 != 0 and 5 != 0 and 7 != 0:
    print(raindrops)