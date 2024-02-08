import tkinter as tk
from PIL import Image, ImageTk
import time

# Function to update the position of the heart
def update_position(x, y):
    root.geometry(f'+{x}+{y}')  # Use 'root' to update the position

# Initialize the tkinter window
root = tk.Tk()
root.overrideredirect(True)  # Remove window decorations

# Specify the full path to the heart image
image_path = r"C:\Users\Administrator\Downloads\heart-1.png"  # Adjust this path as needed
heart_image = Image.open(image_path)
heart_photo = ImageTk.PhotoImage(heart_image)

# Create a label to display the image
label = tk.Label(root, image=heart_photo)
label.pack()

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
image_width, image_height = heart_image.size

# Calculate positions
left = 0, (screen_height - image_height) // 2
right = screen_width - image_width, (screen_height - image_height) // 2
top = (screen_width - image_width) // 2, 0
middle = (screen_width - image_width) // 2, (screen_height - image_height) // 2

# Sequence of positions
positions = [left, right, top, middle]

# Move the heart to different positions
for pos in positions:
    update_position(*pos)
    root.update()
    time.sleep(5)  # Pause for 5 seconds

root.mainloop()
