def statements():
    if answer == total:
        print("Congratulations! You got it right!")
        return
    else:
        print("Sorry, the correct answer is: ", total)
        return


    return statements()

number1 = 547
number2 = 998
total = number1 + number2

print("Please add the following numbers.")
print("   ", number1)
print("+  ", number2)
print("--------")
answer = int(input("What is the answer? "))

statements()