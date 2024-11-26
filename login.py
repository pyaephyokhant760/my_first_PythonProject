attempts = 0
max_attempts = 3
authenticated = False

while attempts < max_attempts:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if (username == "pyae") and (password == 'ppk'):
        authenticated = True
        break
    else:
        print("Invilid username and password,Try again")
        attempts += 1

if authenticated:
    print("Authenticate successful")
else:
    print("Max login attempts reached.")