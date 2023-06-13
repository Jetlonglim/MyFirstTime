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

def save_booking(username1, hall_type, hall_number, time_slot, date_day):
    with open("booking.txt", "a") as file:
        file.write(f"Username: {username1}\n")
        file.write(f"Hall Type: {hall_type}\n")
        file.write(f"Hall Number: {hall_number}\n")
        file.write(f"Time Slot: {time_slot}\n")
        file.write(f"Date: {date_day}\n")
        file.write("-------------------------\n")
        return

def add_hall(choice_of_NP, num_hall, price_hall):
    # Read the existing number of halls from the file
    with open("hall.txt", "r") as file:
        existing_halls = file.readlines()
    
    # Calculate the new total number of halls
    total_halls = len(existing_halls) // 3 + num_hall

    # Write the new number of halls to the file
    with open("hall.txt", "a") as file:
        for hall_number in range(total_halls - num_hall + 1, total_halls + 1):
            file.write(f"Type of hall: {choice_of_NP}\n")
            file.write(f"Hall Number: {hall_number}\n")
            file.write(f"Price of Hall: RM{price_hall}\n")
            file.write("-------------------------\n")

    print(f"{num_hall} halls added to {choice_of_NP} successfully.")
    print(f"Total halls created: {total_halls}")

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
        elif choice==5:
            print('LogOut Successful')
            menu()
            
def admin_panel():
    print('Please choose an option to continue:')
    print('1. Create Hall')
    print('2. View History')
    print('3. Update Hall info')
    print('4. Delete Old Renter')
    print('5. LogOut')
    choice=int(input("Enter your choice: "))
    if choice==1:
        create_hall()
    elif choice==2:
        view_history()
    elif choice==3:
        update_hall_info()
    elif choice==4:
        delete_renter()
    elif choice==5:
        print('LogOut Successful')
        return
    else:
        print('Invalid choice. Please Try Again')
        menu()

def create_hall():
    num_normal = 0
    num_premium = 0
    choice_of_NP= str(input('Type of Hall to Create (Normal[N])/(Premium[P]): '))
    num_hall= int(input('Number of hall: '))
    if choice_of_NP.upper() == 'N':
        choice_N ='Normal'
        num_normal+=num_hall
        price_normal=100
        print(choice_N, ':',num_normal, ': RM', price_normal)
        confirm_add=str(input('Press Y to confirm to add: '))
        if confirm_add.upper() == 'Y':
            add_hall(choice_N, num_normal, price_normal)
        else:
            print('Back To Admin Panel')
            return
    elif choice_of_NP.upper()=='P':
        choice_P ='Premium'
        num_premium+=num_hall
        price_premium=200
        print(choice_P, ':',num_premium, ': RM', price_premium)
        confirm_add=str(input('Press Y to confirm to add: '))
        if confirm_add.upper() == 'Y':
            add_hall(choice_P, num_premium, price_premium)
        else:
            print('Back To Admin Panel')
            return
    else:
        print('Invalid,please try again')
        admin_panel()

def view_history():
    with open("booking.txt", "r") as file:
        bookings = file.readlines()

    if len(bookings) == 0:
        print("No bookings found in the history.")
        admin_panel()
    else:
        print("Booking History:")
        print("-------------------------")
        for i in range(0, len(bookings), 6):
            username = bookings[i].strip().split(": ")[1]
            hall_type = bookings[i + 1].strip().split(": ")[1]
            hall_number = bookings[i + 2].strip().split(": ")[1]
            time_slot = bookings[i + 3].strip().split(": ")[1]
            date = bookings[i + 4].strip().split(": ")[1]
            print(f"Username: {username}")
            print(f"Hall Type: {hall_type}")
            print(f"Hall Number: {hall_number}")
            print(f"Time Slot: {time_slot}")
            print(f"Date: {date}")
            print("-------------------------")
    admin_panel()

def update_hall_info():
    choice = input("Which one would like to update: Timeslot[T] / Price of Hall[P]: ").upper()

    if choice == 'P':
        hall_type = input("Which hall would you like to update Normal[N]/Premium[P]: ").upper()

        if hall_type == 'N':
            new_price = input("Enter the new price for Normal halls: ")
            update_price('Normal', new_price)
            print(f"The price of Normal halls has been updated to {new_price}.")
        elif hall_type == 'P':
            new_price = input("Enter the new price for Premium halls: ")
            update_price('Premium', new_price)
            print(f"The price of Premium halls has been updated to {new_price}.")
        else:
            print("Invalid choice.")
            admin_panel()
    elif choice == 'T':
        day = input("Enter the day you want to update (e.g., Monday, Tuesday, etc.): ")
        new_timeslot = input("Enter the new timeslot for the day: ")
        update_timeslot(day, new_timeslot)
        print(f"The timeslot for {day} has been updated to {new_timeslot}.")
    else:
        print("Invalid choice.")

    admin_panel()

def update_timeslot(day, new_timeslot):
    with open("timeslots.txt", "r") as file:
        lines = file.readlines()

    with open("timeslots.txt", "w") as file:
        for line in lines:
            if line.startswith(f"{day}:"):
                file.write(f"{day}: {new_timeslot}\n")
            else:
                file.write(line)

def update_price(hall_type, new_price):
    with open("hall.txt", "r") as file:
        lines = file.readlines()

    with open("hall.txt", "w") as file:
        for i, line in enumerate(lines):
            if line.startswith(f"Type of hall: {hall_type}"):
                if lines[i + 2].startswith("Price of Hall:"):
                    original_price = lines[i + 2].split(": ")[1].strip()
                    lines[i + 2] = f"Price of Hall: RM{new_price}\n"
                    print(f"The price of {hall_type} hall has been updated from RM{original_price} to RM{new_price}.")
            file.write(line)

def delete_renter():
    try:
        with open("renters.txt", "r") as file:
            renters = file.readlines()

        if len(renters) == 0:
            print("No renters found.")
            admin_panel()

        print("Current renter information:")
        for renter in renters:
            print(renter.strip())

        delete_acc = input("Enter the username of the renter account you want to delete: ")
        password = input("Enter the password for the renter account to confirm delete: ")

        found = False
        with open("renters.txt", "w") as file:
            for renter in renters:
                username, stored_password = renter.strip().split(":")
                if username == delete_acc and password == stored_password:
                    found = True
                else:
                    file.write(renter)

        if found:
            print(f"\nThe renter account '{delete_acc}' has been deleted.")
            admin_panel()
        else:
            print(f"\nThe renter account '{delete_acc}' was not found or the password is incorrect.")
            admin_panel()

    except FileNotFoundError:
        print("No renters found.")
    admin_panel()

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
        admin_panel()
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
        hall_number(username1,info, hall_type, time_slot,date_day)
    elif date_choice == 2:
        date_day = 'Tuesday'
        print('Your hall will be rented on Tuesday')
        hall_number(username1,info, hall_type, time_slot,date_day)
    elif date_choice == 3:
        date_day = 'Wednesday'
        print('Your hall will be rented on Wednesday')
        hall_number(username1,info, hall_type, time_slot,date_day)
    elif date_choice == 4:
        date_day = 'Thursday'
        print('Your hall will be rented on Thursday')
        hall_number(username1,info, hall_type, time_slot,date_day)
    elif date_choice == 5:
        date_day = 'Friday'
        print('Your hall will be rented on Friday')
        hall_number(username1,info, hall_type, time_slot,date_day)
    else:
        print('Invalid')
        return
    
def hall_number(username1, info, hall_type, time_slot, date_day):
    # Check hall availability
    available_halls = []
    with open("hall.txt", "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 4):
            hall_info = lines[i:i + 4]
            if hall_info[0].startswith(f"Type of hall: {hall_type}"):
                hall_number = hall_info[1].split(": ")[-1].strip()
                available_halls.append(hall_number)

    if len(available_halls) == 0:
        print(f"No {hall_type} halls are currently available.")
        return

    print(f"Available {hall_type} halls: {', '.join(available_halls)}")

    hall_number = input("Enter the hall number you want to book: ")
    if hall_number not in available_halls:
        print("Invalid hall number. Please try again.")
        return

    # Display the final choices
    print('\nBooking Details:')
    print(f'Hall Type: {hall_type}')
    print(f'Hall Number: {hall_number}')
    print(f'Time Slot: {time_slot}')
    print(f'Date: {date_day}')
    save_booking(username1, hall_type, hall_number, time_slot, date_day)
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
    if booking_num <= 0 or booking_num > len(user_bookings):
        print("Invalid booking number.")
        return

    booking_index = user_bookings[booking_num - 1]

    hall_change = int(input("Enter new hall type ([1]Normal/[2]Premium): "))
    hall_type = ""
    if hall_change == 1:
        hall_type = 'Normal'
    elif hall_change == 2:
        hall_type = 'Premium'
    else:
        print('Invalid hall type.')
        return

    time_change = int(input("Enter new time slot ([1]10am-12pm, [2]12pm-2pm, [3]2pm-4pm, [4]4pm-6pm, [5]6pm-8pm): "))
    time_slot = ""
    if time_change == 1:
        time_slot = '10am-12pm'
    elif time_change == 2:
        time_slot = '12pm-2pm'
    elif time_change == 3:
        time_slot = '2pm-4pm'
    elif time_change == 4:
        time_slot = '4pm-6pm'
    elif time_change == 5:
        time_slot = '6pm-8pm'
    else:
        print('Invalid time slot.')
        return

    date_change = int(input("Enter new date ([1]Monday, [2]Tuesday, [3]Wednesday, [4]Thursday, [5]Friday): "))
    date_day = ""
    if date_change == 1:
        date_day = 'Monday'
    elif date_change == 2:
        date_day = 'Tuesday'
    elif date_change == 3:
        date_day = 'Wednesday'
    elif date_change == 4:
        date_day = 'Thursday'
    elif date_change == 5:
        date_day = 'Friday'
    else:
        print('Invalid date.')
        return

    bookings[booking_index+1] = f"Hall Type: {hall_type}\n"
    bookings[booking_index+3] = f"Time Slot: {time_slot}\n"
    bookings[booking_index+4] = f"Date: {date_day}\n"

    with open("booking.txt", "w") as file:
        file.writelines(bookings)

    print("Booking changed successfully!")



users=load_users()
menu()