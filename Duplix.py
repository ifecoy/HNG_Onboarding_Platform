import string
import random


# Employee details
def user_details():
    print("Welcome to HNG Onboarding Platform ")
    f_name = input("Please enter your first name: ")
    l_name = input("Please enter your last name: ")
    email = input("Please enter your email: ")
    customer_info = [f_name, l_name, email]
    return customer_info


# Generating password string
def password(customer_info, stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(stringLength))
    user_password = rand_string + str(customer_info[0][0:2] + customer_info[1][-2:])
    return user_password


# Platform initiation
argument = True
container = []

while argument:
    customer_info = user_details()
    user_password = password(customer_info, stringLength=5)

    print("Your password is " + user_password)
    password_query = input("Are you okay with your password?, Enter Yes or No? ").upper()

    password_loop1 = True

    while password_loop1:
        if password_query == "YES":
            customer_info.append(user_password)
            container.append(customer_info)
            print(f'Your HNG employee onboarding details are:  {container}')

            password_loop1 = False

        else:
            u_password = input(str("Enter your password not more that seven(7) characters: "))
            pass_len = True

            while pass_len:
                if len(u_password) >= 7:
                    customer_info.append(u_password)
                    container.append(customer_info)
                    print(f'Your HNG employee onboarding details are:  {container}')
                    pass_len = False
                    password_loop1 = False
                else:
                    print("Your password is less than 7")
                    u_password = input(str("Enter password longer or equal to 7"))

new_user = input("Would you like to register? Yes or No? ").upper()
if (new_user == "NO"):
    argument = False
    for item in container:
        print(item)
    else:
        argument = True