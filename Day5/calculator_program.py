def add(n1, n2):
    return float(n1) + float(n2)

def subtract(n1, n2):
    return float(n1) - float(n2)

def multiply(n1, n2):
    return float(n1) * float(n2)

def subdivide(n1, n2):
    return float(n1) / float(n2)


cal_start = True
continue_value = 0
continue_cal = False
while cal_start:
    if continue_cal:
        user_choice = input("Please choose one of the special characters below:\n+\n-\n*\n/\n")
        s_num = input("Please enter your second number:\n")
        if user_choice == "+":
            print(f"Your calculation result is {add(continue_value, s_num)}")
            continue_value = add(continue_value, s_num)
        elif user_choice == "-":
            print(f"Your calculation result is {subtract(continue_value, s_num)}")
            continue_value = subtract(continue_value, s_num)
        elif user_choice == "*":
            print(f"Your calculation result is {multiply(continue_value, s_num)}")
            continue_value = multiply(continue_value, s_num)
        elif user_choice == "/":
            print(f"Your calculation result is {subdivide(continue_value, s_num)}")
            continue_value = subdivide(continue_value, s_num)
        else:
            print("Please enter a correct special character")
    else:
        user_choice = input("Please choose one of the special characters below:\n+\n-\n*\n/\n")
        f_num = input("Please enter your first number:\n")
        s_num = input("Please enter your second number:\n")
        if user_choice == "+":
            print(f"Your Calculation result is {add(f_num, s_num)}")
            continue_value = add(f_num, s_num)
        elif user_choice == "-":
            print(f"Your Calculation result is {subtract(f_num, s_num)}")
            continue_value = subtract(f_num, s_num)
        elif user_choice == "*":
            print(f"Your Calculation result is {multiply(f_num, s_num)}")
            continue_value = multiply(f_num, s_num)
        elif user_choice == "/":
            print(f"Your Calculation result is {subdivide(f_num, s_num)}")
            continue_value = subdivide(f_num, s_num)
        else:
            print("Please enter a correct special character")

    user_last_choice = input("\n\nDo you want to continue calculate with the result?\n"
                             "Type Yes/No to continue calculate with the result or start a new calculation.\n"
                             "If you want to end the program type Exit\n").lower()
    if user_last_choice == "yes":
        continue_cal = True
    elif user_last_choice == "no":
        continue_cal = False
    else:
        cal_start = False
