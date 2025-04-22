import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    if not re.search("[A-Z]", password):
        return "Weak: Add at least one uppercase letter."
    if not re.search("[a-z]", password):
        return "Weak: Add at least one lowercase letter."
    if not re.search("[0-9]", password):
        return "Weak: Add at least one number."
    if not re.search("[@#$%^&*]", password):
        return "Weak: Add at least one special character."
    return "Strong: Great password!"

def password_checker():
    print("This is PASSWORD CHECKER")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")

        if password.lower() == "exit":
            break

        print(check_password_strength(password))

        print("your password: ",password)
    print("Thank you!")
    
if __name__ == "__main__" :
    password_checker()