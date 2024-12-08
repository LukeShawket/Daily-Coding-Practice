from ctypes import windll
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
check_mark_text = ""
total_remaining_sc = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(str(timer))
    canvas.itemconfig(timer_text, text="00:00")
    app_title.config(text="Timer", fg="white")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    global reps
    global check_mark_text
    reps += 1
    if reps % 8 == 0:
        app_title.config(text="Break", fg=PINK)
        count_down(long_break)
    elif reps % 2 == 0:
        app_title.config(text="Break", fg=PINK)
        count_down(short_break)
        global check_mark_text
        check_mark_text += "✅"
        check_mark.config(text=check_mark_text)
    else:
        app_title.config(text="Work", fg="white")
        count_down(work_time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global total_remaining_sc
    total_remaining_sc = count
    remaining_minutes = int(count / 60)
    remaining_seconds = count % 60
    # this is called python dynamic typing
    if remaining_minutes < 10:
        remaining_minutes = f"0{int(count/60)}"
    if remaining_seconds < 10:
        remaining_seconds = f"0{count%60}"
    canvas.itemconfig(timer_text, text=f"{remaining_minutes}:{remaining_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

app_title = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=GREEN, fg="white")
app_title.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130,text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=2, row=3)

start_button = Button(text="Start")
start_button.grid(column=1, row=4)
start_button.config(command=start_timer)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3,row=4)

check_mark = Label(bg=GREEN, fg=RED)
check_mark.grid(column=2, row=4)










window.mainloop()