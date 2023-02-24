
def validating_input():
    while True:
        try:
            input_value = int(input("Enter the first number:"))
        except ValueError:
            print("Please enter a valid number")
            continue
        else:
            break
    return input_value
    

while True:
    user_input = validating_input()
    print(user_input)
    print(type(user_input))
    break
