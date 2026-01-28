import tkinter as tk
from tkinter import ttk # Basic theme for Tkinter widgets

root = tk.Tk()
root.title("Simple Tkinter App")

def add_to_list():
  text = entry.get()
  if text:
    text_list.insert(tk.END, text)  # Adds text to the listbox
    entry.delete(0, tk.END)         # Clear the entry field after submission
    
# Configure grid to make the frame expand with window resizing
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)   # Takes up equal space across the two cols
root.rowconfigure(0, weight=1)

# Frame is a container used to hold widgets together
frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5) # Sticky NSEW makes the frame expand in all directions/. Padx/y is padding around the frame.

frame.columnconfigure(0, weight=1) # Text entry column expands
frame.rowconfigure(1, weight=1)    # Listbox row expands


# Add a text entry container to the frame
entry = ttk.Entry(frame)
entry.grid(row=0, column=0, sticky='ew')  # Sticky EW lets the entry expand horizontally

entry.bind('<Return>', lambda event: add_to_list())  # Bind Enter key to add_to_list function

# Button to add text from the entry to the label
entry_btn = ttk.Button(frame, text='Add', command=add_to_list)
entry_btn.grid(row=0, column=1)

# Text input area
text_list = ttk.Listbox(frame)
# Column span spreads the widget across a couple of columns. Sticky EW means stick to the East/West Sides
text_list.grid(row=1, column=0, columnspan=2, sticky='ew') 


# Duplicate Frame
frame2 = tk.Frame(root)
frame2.grid(row=0, column=1, sticky='nsew')

frame2.columnconfigure(0, weight=1) 
frame2.rowconfigure(1, weight=1)    

entry = tk.Entry(frame2)
entry.grid(row=0, column=0, sticky='ew')

entry.bind('<Return>', lambda event: add_to_list())

entry_btn = tk.Button(frame2, text='Add', command=add_to_list)
entry_btn.grid(row=0, column=1)

text_list = tk.Listbox(frame2)
text_list.grid(row=1, column=0, columnspan=2, sticky='ew') 


root.mainloop()
