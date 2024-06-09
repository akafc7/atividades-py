import tkinter as tk
import time

class Stopwatch:
    def __init__(self, master):
        self.master = master
        master.title("Cronômetro")

        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        
        self.time_label = tk.Label(master, text=f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
        self.time_label.pack()

        
        self.start_button = tk.Button(master, text="Iniciar", command=self.start)
        self.start_button.pack()

        
        self.stop_button = tk.Button(master, text="Parar", command=self.stop)
        self.stop_button.pack()

        
        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.pack()

    def update_time(self):
        if self.running:
            self.seconds += 1
            if self.seconds >= 60:
                self.seconds = 0
                self.minutes += 1
                if self.minutes >= 60:
                    self.minutes = 0
                    self.hours += 1
            self.time_label.config(text=f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
            root.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        if not self.running:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
            self.time_label.config(text=f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")


root = tk.Tk()
app = Stopwatch(root)


root.mainloop()
