
import tkinter as tk
from tkinter import messagebox, scrolledtext
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def save_to_excel(data):
    df = pd.DataFrame(data)
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "scraped_data.xlsx")
    df.to_excel(file_path, index=False, engine='openpyxl')
    console_log(f"Data saved to: {file_path}")
    start_btn['state'] = tk.NORMAL  # Re-enable the button

def console_log(message):
    console.insert(tk.END, f"{message}\n")
    console.see(tk.END)

def scrape_website(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    # Corrected the method calls
    product_names = [elem.text for elem in driver.find_elements_by_css_selector(".c16H9d")]
    prices = [elem.text for elem in driver.find_elements_by_css_selector(".c3gUW0")]

    driver.quit()
    return {"Product Name": product_names, "Price": prices}

def start_scraping():
    link = url_entry.get()
    if not link:
        messagebox.showerror("Error", "Please enter a URL!")
        return

    start_btn['state'] = tk.DISABLED  # Disable the button to indicate loading
    console_log("Scraping started...")

    try:
        data = scrape_website(link)
        save_to_excel(data)
        console_log("Scraping completed!")
    except Exception as e:
        console_log(f"Error: {str(e)}")
        start_btn['state'] = tk.NORMAL  # Re-enable the button in case of error

root = tk.Tk()
root.title("Web Scraping Bot V1.3")
root.geometry("600x500")

lbl = tk.Label(root, text="Enter the URL:")
lbl.pack(pady=10)

url_entry = tk.Entry(root, width=70)
url_entry.pack(pady=10)

start_btn = tk.Button(root, text="Start Scraping", command=start_scraping, width=20, height=2)
start_btn.pack(pady=10)

console_label = tk.Label(root, text="Console Log:")
console_label.pack(pady=5)

console = scrolledtext.ScrolledText(root, width=70, height=15)
console.pack(pady=10)

root.mainloop()
