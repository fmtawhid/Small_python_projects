import random
for x in range(1,6):
    x=int(input("Enter yor Luky Number: "))
    y=int(random.randint(1,5))

    if x==y:
        print("Success You Won")
    else:
        print("Sorry ! You Loss")

    print(y)
