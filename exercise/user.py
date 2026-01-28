users = {
    "md": "pass123",
    "alice": "alice@2026",
    "rahim": "rahim456",
    "karim": "karim789",
    "sophia": "sophia321"
}




# for username,password in users.items():
#     if username_input != username:
#         print("User not found");
#     elif password_input != password:
#         print("Incorrect password");
#     else:
#         print("Login successful")

def check_user(users,user_in,pass_in):
    # found = False;
    for username,password in users.items():
        if user_in.lower() == username.lower():
            if pass_in == password:
                # found = True;
                print("Login successful");
                return True;
            else:
                print("Incorrect password");
                return False

    print("User not found")
    return False;
    

for attempt in range(3):
    username_input = input("Username: ")
    password_input = input("Password: ")
    if check_user(users, username_input, password_input):
        break   
else:
    print("Too many failed attempts. Access denied.")
    




