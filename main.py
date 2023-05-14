def load_users():
    try:
        with open("renters.txt", "r") as file:
            lines = file.readlines()
            users = dict(line.strip().split(":") for line in lines)
            return users
    except FileNotFoundError:
        return {}

# Function to save user data to file
def save_users(users):
    with open("renters.txt", "w") as file:
        lines = [f"{username}:{password}\n" for username, password in users.items()]
        file.writelines(lines)


def menu():
    print("Hi, Choose the option to continue:")
    print("1|Login  2|Register  3|Admin")
    x=int(input("Enter Number to continue: "))
    if x == 1:
        Login()
    elif x==2:
        Register()
    elif x==3:
        Admin()
    else:
        print(x)

def Login():
    username1=input("Enter username: ")
    password1=input("Enter Password:")
    if username1 in users and users[username1]==password1:
        print('Login Successful')
        change_password = input("Do you want to change your password? (Y/N): ")
        if change_password.upper() == "Y":
            new_password = input("Enter new password: ")
            users[username1] = new_password
            save_users(users)
            print("Password changed successfully!")
    else:
        print('Incorrect username or password')


def Register():
    newuser=input('Enter new username: ')
    if newuser in users:
        print('Username already taken')
        return
    newpass=input('Enter new pass: ')
    confirm_newpass=input('Enter confirm pass: ')
    if newpass==confirm_newpass:
        users[newuser]=newpass
        save_users(users)
        print('Registration Successful')

def Admin():
    adminname=input('Enter Admin name: ')
    adminpass=input('Enter password: ')
    if adminname=='admin' and adminpass=='admin123':
        print('Welcome back Admin')
    else:
        print("Wrong pass or name")
        return()

users=load_users()
menu()