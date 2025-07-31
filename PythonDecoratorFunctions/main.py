import tkinter as tk
import time

# Decorator to log button clicks and measure execution time
def log_and_time(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[LOG] {func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper

# GUI setup
root = tk.Tk()
root.title("Decorator Demo")
root.geometry("300x200")

@log_and_time
def on_click():
    label.config(text="Button clicked!")
    time.sleep(0.5)

label = tk.Label(root, text="Click the button")
label.pack(pady=20)

btn = tk.Button(root, text="Click Me", command=on_click)
btn.pack()

root.mainloop()

