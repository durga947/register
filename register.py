def register_user():
    print("=== Registration Form ===")
    
    # Collect user input
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    # Save user data to a file
    with open('users.txt', 'a') as file:
        file.write(f"Username: {username}, Email: {email}, Password: {password}\n")
    
    print("Registration successful!")

if __name__ == "__main__":
    register_user()
