
import tkinter as tk
from tkinter import messagebox, scrolledtext
import pandas as pd
import os

def save_to_excel(data):
    # Create a DataFrame from the scraped data
    df = pd.DataFrame(data)
    
    # Get the desktop path and save the file there
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "scraped_data.xlsx")
    df.to_excel(file_path, index=False, engine='openpyxl')
    
    messagebox.showinfo("Info", f"Data saved to: {file_path}")

def start_scraping():
    # Placeholder function for web scraping
    link = url_entry.get()
    if not link:
        messagebox.showerror("Error", "Please enter a URL!")
        return
    
    # Placeholder: Later, the actual scraping function will be called here.
    # For now, we'll use dummy data for testing the save_to_excel function
    dummy_data = {
        "Product Name": ["Product A", "Product B"],
        "Price": ["$10", "$20"]
    }
    save_to_excel(dummy_data)

# Create the main window
root = tk.Tk()
root.title("Web Scraping Bot")
root.geometry("500x400")

# Label
lbl = tk.Label(root, text="Enter the URL:")
lbl.pack(pady=20)

# Entry for URL
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

# Start Scraping Button
start_btn = tk.Button(root, text="Start Scraping", command=start_scraping)
start_btn.pack(pady=20)

root.mainloop()
