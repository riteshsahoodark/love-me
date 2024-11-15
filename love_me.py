import tkinter as tk
import random

def move_no_button(event):
    """Move the 'No' button to a random location within the window."""
    new_x = random.randint(0, window.winfo_width() - 100)
    new_y = random.randint(0, window.winfo_height() - 50)
    no_button.place(x=new_x, y=new_y)

def love_response():
    """Display a message and show an image when 'Yes' is clicked."""
    label.config(text="I love you too! ❤")
    love_image = tk.PhotoImage(file="love.png")  # Replace 'love.png' with your image file path
    image_label.config(image=love_image)
    image_label.image = love_image  # Keep a reference to avoid garbage collection

# Create the main window
window = tk.Tk()
window.title("Do You Love Me?")
window.geometry("500x400")

# Add a label with the question
label = tk.Label(window, text="Do you love me?", font=("Arial", 18))
label.pack(pady=20)

# Add a button for "Yes"
yes_button = tk.Button(window, text="Yes", font=("Arial", 14), command=love_response)
yes_button.pack(pady=10)

# Add a button for "No" that moves when hovered over
no_button = tk.Button(window, text="No", font=("Arial", 14))
no_button.place(x=200, y=200)
no_button.bind("<Enter>", move_no_button)

# Add a placeholder for the image
image_label = tk.Label(window)
image_label.pack(pady=20)

# Load the image
image_path = "love.png"

# Run the application
window.mainloop()
