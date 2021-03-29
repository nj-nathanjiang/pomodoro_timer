from tkinter import *
from PIL import ImageTk, Image
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
the_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(the_timer)
    timer_label.config(text="Timer")
    pomodoro_checks.config(text="")
    canvas.itemconfig(timer, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps == 8:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    else:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global the_timer

    count_minutes = count // 60
    count_seconds = count % 60

    if count_seconds < 10:
        string_seconds = f"0{count_seconds}"
    else:
        string_seconds = count_seconds

    canvas.itemconfig(timer, text=f"{count_minutes}:{string_seconds}")
    if count > 0:
        the_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            marks += "✔️"
        pomodoro_checks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg="white")

canvas = Canvas(window, width=250, height=274, bg="white")
canvas.grid(row=2, column=3)
tomato_image = ImageTk.PhotoImage(Image.open("tomato.jpg"))
canvas.create_image(125, 137, image=tomato_image)
timer = canvas.create_text(125, 150, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 60))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

pomodoro_checks = Label(text="", fg=GREEN)
pomodoro_checks.grid(column=1, row=3)


window.mainloop()
