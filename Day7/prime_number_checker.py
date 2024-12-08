num_to_check = int(input("Please input the number you want to check:\n"))

def is_prime(num):
    division_list = []
    for i in range(num+1):
        if num % (i+1) == 0:
            division_list.append(i+1)
    if len(division_list) > 2:
        return f"{num_to_check} is not a prime number."
    else:
        return f"{num_to_check} is a prime number."

print(is_prime(num_to_check))