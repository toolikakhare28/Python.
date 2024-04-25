import tkinter as tk
from tkinter import messagebox
import time

class DrinkWaterReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drink Water Reminder App")
        self.root.geometry("300x150")

        self.label = tk.Label(root, text="Drink Water Reminder", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.reminder_interval = 30 * 60  # 30 minutes
        self.last_reminder_time = time.time()

        self.reminder_button = tk.Button(root, text="Take a Drink", command=self.show_reminder)
        self.reminder_button.pack(pady=20)

        self.quit_button = tk.Button(root, text="Quit", command=root.destroy)
        self.quit_button.pack()

        self.check_reminder()

    def show_reminder(self):
        messagebox.showinfo("Reminder", "It's time to take a drink!")

    def check_reminder(self):
        current_time = time.time()

        if current_time - self.last_reminder_time >= self.reminder_interval:
            self.show_reminder()
            self.last_reminder_time = current_time

        self.root.after(1000, self.check_reminder)  # Check every 1 second

if __name__ == "__main__":
    root = tk.Tk()
    app = DrinkWaterReminderApp(root)
    root.mainloop()
