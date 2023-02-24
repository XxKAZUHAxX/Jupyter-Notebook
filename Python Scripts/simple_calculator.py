def validating_input():
    while True:
        try:
            input_value1 = int(input("Enter the first number:\t"))
            input_value2 = input("Enter the operator:\t")
            input_value3 = int(input("Enter the second number:\t"))
        except ValueError:
            print("Invalid Input!")
            continue
        else:
            if input_value2 not in '+-*/':
                print("Invalid Operator!")
                continue
            print("Valid input!")
            break
    return input_value1,input_value2,input_value3

def calculate(num_tuple):
    if num_tuple[1] == '+':
        return num_tuple[0] + num_tuple[2]
    elif num_tuple[1] == '-':
        return num_tuple[0] - num_tuple[2]
    elif num_tuple[1] == '*':
        return num_tuple[0] * num_tuple[2]
    elif num_tuple[1] == '/':
        try:
            num_tuple[0] / num_tuple[2]
        except ZeroDivisionError:
            return "Error: Division by zero"
        else:
            return num_tuple[0] / num_tuple[2]

def rerun():
    while True:
        rerun = ""
        try:
            rerun = input("Do you want to rerun the program? (y/n):\t")
        except rerun.lower() not in 'yn':
            print("Invalid Input!")
            continue
        else:
            if rerun.lower() == 'yn':
                print("Invalid Input!")
                continue
            elif rerun.lower() == 'ny':
                print("Invalid Input!")
                continue
            else:
                return rerun


while True:
    user_input = validating_input()
    result = calculate(user_input)
    print(f"The result of {user_input[0]} {user_input[1]} {user_input[2]} is {result}")
    system_rerun = rerun()
    if system_rerun == "y":
        print("Rerunning the program...\n\n\n")
        continue
    else:
        break
    
