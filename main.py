def load_users():
    try:
        with open("users.txt", "r") as file:
            lines = file.readlines()
            users = dict(line.strip().split(":") for line in lines)
            return users
    except FileNotFoundError:
        return {}

# Function to save user data to file
def save_users(users):
    with open("users.txt", "w") as file:
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
    else:
        print('Incorrect username or password')


def Register():
    newuser=input('Enter new username: ')
    if newuser in renter:
        print('Username already taken')
        return
    newpass=input('Enter new pass: ')
    confirm_newpass=input('Enter confirm pass: ')
    if newpass==confirm_newpass:
        renter[newuser]=newpass
        print('Registration Successful')


def Admin():
    print('Admin')

menu()