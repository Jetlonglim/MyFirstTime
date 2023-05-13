import tkinter as tk
from tkinter import messagebox

# Create the main application window
window = tk.Tk()
window.title("Rental Movie Theatre")
window.geometry("400x300")

# Create two frames - Page 1 and Page 2
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)

# Function to switch to Page 1
def show_frame1():
    frame2.pack_forget()  # Hide frame 2
    frame3.pack_forget() # Hide frame 3 
    frame4.pack_forget() # Hide frame 4
    frame1.pack()  # Show frame 1
    
# Function to switch to Page 2(Login)
def show_frame2():
    frame1.pack_forget()  # Hide frame 1
    frame2.pack()  # Show frame 2

#Function to switch to Page 3(Register)
def show_frame3():
    frame1.pack_forget() #Hide frame 3
    frame3.pack() # Show frame 3

#Function switch to Page 4(Admin)
def show_frame4():
    frame1.pack_forget() #Hide frame 4
    frame4.pack() #Show frame 4

# Page 1 content
label1 = tk.Label(frame1, text="HI. Choose the option to continue")
label1.pack()
button1 = tk.Button(frame1, text="Login", command=show_frame2)
button1.pack(side=tk.LEFT, padx=5)
button2 = tk.Button(frame1, text="Register", command=show_frame3)
button2.pack(side=tk.LEFT, padx=5)
button3 = tk.Button(frame1, text="Admin", command=show_frame4)
button3.pack(side=tk.LEFT, padx=5)

# Page 2 content
label2 = tk.Label(frame2, text="Login")
label2.pack()
button2 = tk.Button(frame2, text="Back", command=show_frame1)
button2.pack()

# Page 3 content
label3 = tk.Label(frame3, text="Register")
label3.pack()
button3 = tk.Button(frame3, text="Back", command=show_frame1)
button3.pack()

# Page 4 content

label4 = tk.Label(frame4, text="Admin")
label4.pack()
button4 = tk.Button(frame4, text="Back", command=show_frame1)
button4.pack()

# Show Page 1 by default
show_frame1()

# Start the Tkinter event loop
window.mainloop()
