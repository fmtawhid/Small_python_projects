# tawhid program
# Mark Sheed
print("The Mark is class 10 Result ")

total_number=int(input("Input your Total Mark"))
sub=11.5
gor=total_number/sub


if gor>79:
    print("You got A+")
elif gor>69:
    print("You got A")
elif gor>59:
    print("you got A-")
elif gor>49:
    print("You got B")
elif gor>39:
    print("You got C")
elif gor>32:
    print("You got D or Passed")
else:
    print("Sorry You Falled")