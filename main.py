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

def save_booking(username1, hall_type, time_slot, date_day):
    with open("booking.txt", "a") as file:
        file.write(f"Username: {username1}\n")
        file.write(f"Hall Type: {hall_type}\n")
        file.write(f"Time Slot: {time_slot}\n")
        file.write(f"Date: {date_day}\n")
        file.write("-------------------------\n")
        return

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
        print('Invalid option, please try again')

def Login():
    username1=input("Enter username: ")
    password1=input("Enter Password:")
    if username1 in users and users[username1]==password1:
        print('Login Successful')
        Renter_main_page(username1)
    else:
        print('Incorrect username or password')

def Renter_main_page(username1):
        print('Please choose an option to continue: ')
        print('1. Create Booking')
        print('2. View Timeslot')
        print('3. Change Password')
        print('4. Change Booking')
        print('5. Logout')
        choice=int(input("Enter your choice: "))
        if choice==1:
            create_booking(username1)
        elif choice==2:
            view_timeslot()
        elif choice==3:
            change_password=str(input('Do you want to change password? (Y/N): '))
            if change_password.upper()=='Y':
                new_password=input('Enter new password: ')
                users[username1]=new_password
                save_users(users)
                print('Password changed successfully')
            else:
                print('Invalid option. Please try again')
                return
        elif choice==4:
            change_booking(username1)
            
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

def hall(username1,info):
    hall_choice = int(input('1. Normal | 2. Premium: '))
    if hall_choice == 1:
        hall_type = 'Normal'
        print('Your type of hall is normal')
        time(username1,info, hall_type)
    elif hall_choice == 2:
        hall_type = 'Premium'
        print('Your type of hall is premium')
        time(username1,info, hall_type)
    else:
        print('Invalid')
        return


def time(username1,info, hall_type):
    time_choice = int(input('1. 10am-12pm | 2. 12pm-2pm | 3. 2pm-4pm | 4. 4pm-6pm | 5. 6pm-8pm : '))
    if time_choice == 1:
        time_slot = '10am-12pm'
        print('Your rented hall will start at 10am-12pm')
        date(username1,info, hall_type, time_slot)
    elif time_choice == 2:
        time_slot = '12pm-2pm'
        print('Your rented hall will start at 12pm-2pm')
        date(username1,info, hall_type, time_slot)
    elif time_choice == 3:
        time_slot = '2pm-4pm'
        print('Your rented hall will start at 2pm-4pm')
        date(username1,info, hall_type, time_slot)
    elif time_choice == 4:
        time_slot = '4pm-6pm'
        print('Your rented hall will start at 4pm-6pm')
        date(username1,info, hall_type, time_slot)
    elif time_choice == 5:
        time_slot = '6pm-8pm'
        print('Your rented hall will start at 6pm-8pm')
        date(username1,info, hall_type, time_slot)            
    else:
        print('Invalid')
        return


def date(username1,info, hall_type, time_slot):
    date_choice = int(input('1. Monday | 2. Tuesday | 3. Wednesday | 4. Thursday | 5. Friday: '))
    if date_choice == 1:
        date_day = 'Monday'
        print('Your hall will be rented on Monday')
    elif date_choice == 2:
        date_day = 'Tuesday'
        print('Your hall will be rented on Tuesday')
    elif date_choice == 3:
        date_day = 'Wednesday'
        print('Your hall will be rented on Wednesday')
    elif date_choice == 4:
        date_day = 'Thursday'
        print('Your hall will be rented on Thursday')
    elif date_choice == 5:
        date_day = 'Friday'
        print('Your hall will be rented on Friday')
    else:
        print('Invalid')
        return
    
    # Display the final choices
    print('\nBooking Details:')
    print(f'Hall Type: {hall_type}')
    print(f'Time Slot: {time_slot}')
    print(f'Date: {date_day}')
    save_booking(username1, hall_type, time_slot, date_day)
    return

def create_booking(username1):
    info = ['Normal', 'Premium']

    choice = input("Choose the option you want to start booking: (Y/N) ")
    if choice.upper() == 'Y':
        hall(username1,info)
        Renter_main_page(username1)
    elif choice.upper() == 'N':
        print("Back to the main page")
        return
    else:
        print('Invalid. Try again')
        return

def view_timeslot():
    try:
        with open("timeslots.txt", "r") as file:
            timeslots = file.read()
            print(timeslots)
    except FileNotFoundError:
        print("Timeslot data not found.")
        return

def change_booking(username1):
    with open("booking.txt", "r") as file:
        bookings = file.readlines()

    if not bookings:
        print("No bookings found.")
        return

    print("Your Bookings:")
    user_bookings = []
    for i, booking in enumerate(bookings):
        if booking.startswith("Username:"):
            if booking.split(":")[1].strip() == username1:
                user_bookings.append(i)
                print(f"Booking {len(user_bookings)}:")
                print(booking)
                print(bookings[i+1])
                print(bookings[i+2])
                print(bookings[i+3])

    if not user_bookings:
        print("You have no bookings.")
        return

    booking_num = int(input("Enter the booking number you want to change: "))
    if booking_num > 0 and booking_num <= len(user_bookings):
        booking_index = user_bookings[booking_num - 1]
        hall_type = input("Enter new hall type (Normal/Premium): ")
        time_slot = input("Enter new time slot (10am-12pm, 12pm-2pm, 2pm-4pm, 4pm-6pm, 6pm-8pm): ")
        date_day = input("Enter new date (Monday, Tuesday, Wednesday, Thursday, Friday): ")

        bookings[booking_index+1] = f"Hall Type: {hall_type}\n"
        bookings[booking_index+2] = f"Time Slot: {time_slot}\n"
        bookings[booking_index+3] = f"Date: {date_day}\n"

        with open("booking.txt", "w") as file:
            file.writelines(bookings)

        print("Booking changed successfully!")
    else:
        print("Invalid booking number.")


users=load_users()
menu()