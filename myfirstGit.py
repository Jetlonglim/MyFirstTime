import tkinter as tk

# Create a new Tkinter window
window = tk.Tk()

# Set the window title
window.title("Simple Tkinter Window")

# Set the window dimensions
window.geometry("400x300")

# Add a label widget
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

# Start the Tkinter event loop
window.mainloop()
