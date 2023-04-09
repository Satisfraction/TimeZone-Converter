from datetime import datetime
from pytz import timezone, common_timezones
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x300")
root.title("Zeitzonen-Konverter")

# Standard-Zeitzone festlegen (Berlin)
standard_tz = timezone('Europe/Berlin')

# Funktion zur Aktualisierung der Zeit
def update_time():
    # Aktuelle Zeit in der Standard-Zeitzone
    current_time = datetime.now(standard_tz)
    time_label.config(text=current_time.strftime('%d.%m.%Y %H:%M:%S'))

    # Zeit in der ausgewählten Zeitzone
    selected_tz = timezone(selected_tz_str.get())
    selected_time = current_time.astimezone(selected_tz)
    selected_time_label.config(text=selected_time.strftime('%d.%m.%Y %H:%M:%S'))

# Dropdown-Menü für die Standard-Zeitzone
standard_tz_label = tk.Label(root, text="Standard-Zeitzone:")
standard_tz_label.pack(pady=10)

standard_tz_str = tk.StringVar(value='Europe/Berlin')
standard_tz_dropdown = ttk.Combobox(root, textvariable=standard_tz_str, values=common_timezones)
standard_tz_dropdown.pack()

# Dropdown-Menü für die zweite Zeitzone
selected_tz_label = tk.Label(root, text="Zweite Zeitzone:")
selected_tz_label.pack(pady=10)

selected_tz_str = tk.StringVar(value='UTC')
selected_tz_dropdown = ttk.Combobox(root, textvariable=selected_tz_str, values=common_timezones)
selected_tz_dropdown.pack()

# Zeit-Labels
time_label = tk.Label(root, text="")
time_label.pack(pady=10)

selected_time_label = tk.Label(root, text="")
selected_time_label.pack(pady=10)

# Aktualisierungs-Button
update_btn = tk.Button(root, text="Aktualisieren", command=update_time)
update_btn.pack(pady=10)

# Initialisierung der Zeit
update_time()

root.mainloop()
