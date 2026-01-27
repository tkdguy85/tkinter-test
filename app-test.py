import tkinter as tk

# Create the main application window
root = tk.Tk()

# Sets the title of the window
root.title("Test App")

def on_click():
  # print("Button clicked")
  label.config(text="Button Clicked")

label = tk.Label(root, text="Button Label")
label.grid(row=0, column=0) # Set the position of the label

print(label.config().keys()) # Print all configuration options for the label

# Add a button to the window
btn = tk.Button(root, text="Push the Button", command=on_click)
btn.grid(row=0, column=1)

root.mainloop()
