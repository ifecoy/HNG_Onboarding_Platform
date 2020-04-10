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
onboarding_details = []

# Collect uer details
while argument:
    customer_info = user_details()
    user_password = password(customer_info, stringLength=5)
    print(f'Your password is "  {user_password}')
    password_query = input("""Are you okay with your password?
Enter Yes if you are okay or enter NO and immediately supply your desired password
not lower than seven (7) characters """).upper()

    password_loop = True

    while password_loop:

        if password_query == "YES":
            customer_info.append(user_password)
            onboarding_details.append(customer_info)
            print(f'Your HNG details are  {onboarding_details}')

            password_loop = False
            argument = False
        else:
            user_password = input("Enter your password not more that seven(7) characters: ")

            character_len = True

            while character_len:
                if len(user_password) >= 7:

                    customer_info.append(user_password)
                    onboarding_details.append(customer_info)
                    print(f'Your HNG details are  {onboarding_details}')

                    character_len = False

                    password_loop = False

                    argument = False
                else:
                    print("Your password is lower than seven(7)")
                    user_password = input("Enter your password not more that seven(7) characters: ")

    new_user = input("Would you like to register a new user Yes or No? ").upper()
    if new_user == "NO":
        argument = False
        for details in onboarding_details:
            print(details)
    else:
        argument = True
