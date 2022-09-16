import random

nums = [i for i in range(1,101)]
comp = random.choice(nums)
# print(comp)

while True:
    try:
        a = int(input("Enter a Number(0 to 100): "))
        if a < comp:
            print("Number is Lesser! Please Choose Greater Number")
        elif a > comp:
            print("Number is Greater! Please Choose Lesser Number")
        else:
            print("You Successfully Guess the Number!!!")
            exit()
    except Exception as e:
        print("Please Enter Valid Value")

print("Thanks For Playing This Game")
