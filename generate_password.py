import tkinter as tk
import random
import string
import time
import threading

# מחולל סיסמה חכמה
def generate_password(length=14):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_-+=<>?"
    return ''.join(random.choice(chars) for _ in range(length))

# אנימציה של טעינה
def loading_animation(label):
    for frame in ["⠋", "⠙", "⠸", "⠼", "⠴", "⠦", "⠇"]:
        label.config(text=frame)
        time.sleep(0.07)

# אפקט רקע מתחלף
def color_flash(window):
    for _ in range(8):
        window.config(bg=random.choice(["#ff5f5f", "#5fff82", "#6ea8ff", "#ffea6e"]))
        time.sleep(0.07)
    window.config(bg="#1e1e1e")

# פונקציה שמייצרת הכל
def generate():
    threading.Thread(target=animate_and_generate).start()

def animate_and_generate():
    loading_label.config(text="")
    password_label.config(text="")

    # אפקט – אנימציית טוען
    for i in range(12):
        loading_animation(loading_label)

    # אפקט צבעוני ברקע
    color_flash(window)

    # יצירת סיסמה
    pwd = generate_password()
    password_label.config(text=pwd)

def copy_to_clipboard():
    pwd = password_label.cget("text")
    window.clipboard_clear()
    window.clipboard_append(pwd)
    copied_label.config(text="✔️ הועתק!")

# חלון
window = tk.Tk()
window.title("🔐 מחולל סיסמאות קטלני")
window.geometry("420x420")
window.config(bg="#1e1e1e")

title_label = tk.Label(window, text="⚡ מחולל סיסמאות על 🔥", 
                       font=("Arial", 22, "bold"), fg="white", bg="#1e1e1e")
title_label.pack(pady=20)

loading_label = tk.Label(window, text="", font=("Arial", 30), fg="#00ffea", bg="#1e1e1e")
loading_label.pack(pady=5)

password_label = tk.Label(window, text="", font=("Consolas", 20, "bold"), fg="#ffea00", bg="#1e1e1e")
password_label.pack(pady=20)

generate_btn = tk.Button(window, text="🎲 צור סיסמה", font=("Arial", 14),
                         bg="#3a3aff", fg="white", padx=20, pady=10, command=generate)
generate_btn.pack(pady=10)

copy_btn = tk.Button(window, text="📋 העתק", font=("Arial", 14),
                     bg="#00b36b", fg="white", padx=20, pady=10, command=copy_to_clipboard)
copy_btn.pack(pady=5)

copied_label = tk.Label(window, text="", fg="lime", font=("Arial", 12), bg="#1e1e1e")
copied_label.pack()


# בתוך window.mainloop():
def smooth_background():
    colors = ["#1e1e1e", "#252525", "#2b2b2b", "#1e1e1e"]
    i = 0
    def loop():
        nonlocal i
        window.config(bg=colors[i % len(colors)])
        i += 1
        window.after(500, loop)
    loop()
smooth_background()


window.mainloop()
