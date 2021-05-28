import tkinter as tk
import time

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
pomodoro_after = None
timer_is_on = False
check_mark = "🗸"


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer_is_on
    global reps
    global check_mark
    pomodoro.after_cancel(pomodoro_after)
    canvas.itemconfig(canvas_timer, text="00:00")
    label_title.config(text="Timer", fg=GREEN)
    label_completed_pomodoros.config(text="")
    reps = 0
    check_mark = "🗸"
    timer_is_on = False


# ------------ TIMER MECHANISM -------------- #
def start_timer():
    global reps
    global timer_is_on
    global check_mark

    if timer_is_on:
        return

    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label_title.config(text="Break", fg=GREEN)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label_title.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        label_title.config(text="Work", fg=RED)


# --------------- COUNTDOWN MECHANISM ------------------ #
def count_down(count):
    global pomodoro_after
    global reps
    global timer_is_on
    global check_mark

    timer_is_on = True
    mins, secs = divmod(count, 60)
    timer = f"{mins:02d}:{secs:02d}"
    canvas.itemconfig(canvas_timer, text=timer)
    if count > 0:
        pomodoro_after = pomodoro.after(1000, count_down, count - 1)
    else:
        timer_is_on = False
        if reps % 2 != 0:
            label_completed_pomodoros.config(text=F"{check_mark}")
            check_mark += "🗸"
        if reps % 8 == 0:
            check_mark = "🗸"
            label_completed_pomodoros.config(text="")
# ---------------------------- UI SETUP ------------------------------- #


pomodoro = tk.Tk()
pomodoro.title("Pomodoro Timer")
pomodoro.config(padx=100, pady=50, bg=YELLOW)
img_tomato = tk.PhotoImage(file="tomato.png")

label_title = tk.Label(
    text="Timer",
    bg=YELLOW,
    fg=GREEN,
    font=(FONT_NAME, 35, "bold")
)
label_title.grid(column=1, row=0)

canvas = tk.Canvas(
    width=200,
    height=224,
    bg=YELLOW,
    highlightbackground=YELLOW
)
canvas.create_image(102, 112, image=img_tomato)
canvas_timer = canvas.create_text(100, 130, text="00:00",
                                  fill="white",
                                  font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = tk.Button(text="Start", command=start_timer)
button_start.grid(column=0, row=2)

button_reset = tk.Button(text="Reset", command=reset_timer)
button_reset.grid(column=2, row=2)

label_completed_pomodoros = tk.Label(
    text="",
    bg=YELLOW,
    fg=GREEN,
    font=(FONT_NAME, 25, "bold")
)
label_completed_pomodoros.grid(column=1, row=3)
pomodoro.mainloop()
