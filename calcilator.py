# import tkinter as tk
# from tkinter import messagebox

# def bosilganda(belgi):
#     hozirgi = ekran.get()
#     ekran.delete(0, tk.END)
#     ekran.insert(0, hozirgi + belgi)

# def tozala():
#     ekran.delete(0, tk.END)

# def hisobla():
#     try:
#         natija = eval(ekran.get())
#         ekran.delete(0, tk.END)
#         ekran.insert(0, str(natija))
#     except Exception:
#         messagebox.showerror("Xato", "Noto'g'ri ifoda")

# # Asosiy oyna
# root = tk.Tk()
# root.title("Python Kalkulyator")
# root.geometry("375x400")

# # Ekran qismi
# ekran = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="flat", justify='right')
# ekran.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# # Tugmalar ro'yxati
# tugmalar = [
#     '7', '8', '9', '/',
#     '4', '5', '6', '*',
#     '1', '2', '3', '-',
#     'C', '0', '=', '+'
# ]

# r = 1
# c = 0

# for tugma in tugmalar:
#     if tugma == '=':
#         tk.Button(root, text=tugma, width=5, height=2, font=("Arial", 14), 
#                   command=hisobla, bg="#4CAF50", fg="white").grid(row=r, column=c, padx=5, pady=5)
#     elif tugma == 'C':
#         tk.Button(root, text=tugma, width=5, height=2, font=("Arial", 14), 
#                   command=tozala, bg="#f44336", fg="white").grid(row=r, column=c, padx=5, pady=5)
#     else:
#         tk.Button(root, text=tugma, width=5, height=2, font=("Arial", 14), 
#                   command=lambda t=tugma: bosilganda(t)).grid(row=r, column=c, padx=5, pady=5)
    
#     c += 1
#     if c > 3:
#         c = 0
#         r += 1

# root.mainloop() 

# azamat azamat az az azamat
# xazina olmani ol azamatni oyoqiw
# olmani tagiga olma tushdi


# azamatova gull 
# qodirov azam 
# azamov azam
# aziz
# guli esa aza,at

#oddiy soat
# import tkinter as tk
# import time

# def update_time():
#     # Hozirgi vaqtni HH:MM:SS formatida olish
#     current_time = time.strftime('%H:%M:%S')
#     # Ekrandagi matnni yangilash
#     label.config(text=current_time)
#     # Har 1000 millisoniyada (1 sekund) funksiyani qayta chaqirish
#     label.after(1000, update_time)

# # Asosiy oynani yaratish
# root = tk.Tk()
# root.title("Mening Soatim")

# # Soat dizayni (shrift, rang va fon)
# label = tk.Label(root, font=('Helvetica', 48, 'bold'),
#                  background='black',
#                  foreground='cyan')

# # Soatni oyna markaziga joylashtirish
# label.pack(anchor='center', expand=True)

# # Vaqtni yangilash funksiyasini ishga tushirish
# update_time()

# # Dasturni doimiy ishchi holatda saqlash
# root.mainloop()





# import tkinter as tk
# from tkinter import ttk
# import time

# class ClockApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Multi-Soat Loyihasi")
#         self.root.geometry("400x300")

#         # Tablar uchun kontrol (Varaqlar)
#         self.tabs = ttk.Notebook(root)
#         self.tab_clock = ttk.Frame(self.tabs)
#         self.tab_stopwatch = ttk.Frame(self.tabs)

#         self.tabs.add(self.tab_clock, text="Asosiy Soat")
#         self.tabs.add(self.tab_stopwatch, text="Sekundamer")
#         self.tabs.pack(expand=1, fill="both")

#         # --- 1. ASOSIY SOAT QISMI ---
#         self.label_clock = tk.Label(self.tab_clock, font=('Helvetica', 40, 'bold'), fg='blue')
#         self.label_clock.pack(expand=True)
#         self.update_clock()

#         # --- 2. SEKUNDAMER QISMI ---
#         self.sw_running = False
#         self.sw_start_time = 0
#         self.sw_elapsed = 0

#         self.label_sw = tk.Label(self.tab_stopwatch, text="00:00:00.0", font=('Helvetica', 40))
#         self.label_sw.pack(pady=20)

#         btn_frame = tk.Frame(self.tab_stopwatch)
#         btn_frame.pack()

#         tk.Button(btn_frame, text="Boshlash", command=self.sw_start).pack(side="left", padx=5)
#         tk.Button(btn_frame, text="To'xtatish", command=self.sw_stop).pack(side="left", padx=5)
#         tk.Button(btn_frame, text="Reset", command=self.sw_reset).pack(side="left", padx=5)

#     # Soat funksiyasi
#     def update_clock(self):
#         current = time.strftime('%H:%M:%S')
#         self.label_clock.config(text=current)
#         self.root.after(1000, self.update_clock)

#     # Sekundamer funksiyalari
#     def sw_update(self):
#         if self.sw_running:
#             self.sw_elapsed = time.time() - self.sw_start_time
#             minutes, seconds = divmod(self.sw_elapsed, 60)
#             hours, minutes = divmod(minutes, 60)
#             # Millisoniyalarni ham ko'rsatish
#             time_str = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}.{int((self.sw_elapsed % 1)*10)}"
#             self.label_sw.config(text=time_str)
#             self.root.after(100, self.sw_update)

#     def sw_start(self):
#         if not self.sw_running:
#             self.sw_start_time = time.time() - self.sw_elapsed
#             self.sw_running = True
#             self.sw_update()

#     def sw_stop(self):
#         self.sw_running = False

#     def sw_reset(self):
#         self.sw_running = False
#         self.sw_elapsed = 0
#         self.label_sw.config(text="00:00:00.0")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ClockApp(root)
#     root.mainloop()





#ilon o'yin


import turtle
import time
import random

delay = 0.1
score = 0

# Oyna sozlamalari
wn = turtle.Screen()
wn.title("Iloncha O'yini")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) # Ekran yangilanishini vaqtincha to'xtatish

# Ilon boshi
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Ovqat (Olma)
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = [] # Ilon tanasi qismlari

# Funksiyalar (Harakatlar)
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Klaviatura nazorati
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Asosiy o'yin sikli
while True:
    wn.update()

    # Devorga urilishni tekshirish
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0

    # Ovqatni yeyishni tekshirish
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Tanani o'stirish
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Tanani boshiga ergashishini ta'minlash
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # O'z tanasiga urilishni tekshirish
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for s in segments:
                s.goto(1000, 1000)
            segments.clear()

    time.sleep(delay)

wn.mainloop()












