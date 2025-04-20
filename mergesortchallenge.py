import tkinter as tk
import random
import time
from functools import partial

class MergeSortGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Merge Sort Game")
        self.root.geometry("700x400")
        
        self.score = 0
        self.time_left = 30
        self.data = []
        self.difficulty = "Easy"
        
        self.label = tk.Label(root, text="Merge Sort Challenge", font=("Arial", 18))
        self.label.pack(pady=10)

        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack(pady=10)

        self.info_frame = tk.Frame(root)
        self.info_frame.pack(pady=5)
        
        self.score_label = tk.Label(self.info_frame, text=f"Score: {self.score}", font=("Arial", 12))
        self.score_label.pack(side=tk.LEFT, padx=10)

        self.timer_label = tk.Label(self.info_frame, text=f"Time Left: {self.time_left}", font=("Arial", 12))
        self.timer_label.pack(side=tk.LEFT, padx=10)
        
        self.diff_label = tk.Label(self.info_frame, text=f"Difficulty: {self.difficulty}", font=("Arial", 12))
        self.diff_label.pack(side=tk.LEFT, padx=10)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.start_button = tk.Button(self.button_frame, text="Start Game", command=self.start_game)
        self.start_button.grid(row=0, column=0, padx=5)

        self.difficulty_menu = tk.StringVar(value="Easy")
        tk.OptionMenu(self.button_frame, self.difficulty_menu, "Easy", "Medium", "Hard").grid(row=0, column=1, padx=5)

    def start_game(self):
        self.score = 0
        self.time_left = {"Easy": 30, "Medium": 25, "Hard": 20}[self.difficulty_menu.get()]
        self.difficulty = self.difficulty_menu.get()
        self.data = [random.randint(1, 99) for _ in range({"Easy": 6, "Medium": 8, "Hard": 10}[self.difficulty])]
        self.update_info()
        self.draw_blocks()
        self.run_timer()

    def update_info(self):
        self.score_label.config(text=f"Score: {self.score}")
        self.timer_label.config(text=f"Time Left: {self.time_left}")
        self.diff_label.config(text=f"Difficulty: {self.difficulty}")

    def draw_blocks(self):
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()
        
        for i, val in enumerate(self.data):
            btn = tk.Button(self.canvas_frame, text=str(val), width=5, height=2,
                            command=partial(self.merge_attempt, i))
            btn.grid(row=0, column=i, padx=5)

    def merge_attempt(self, index):
        if index < len(self.data) - 1:
            a, b = self.data[index], self.data[index+1]
            if a <= b:
                merged = a + b  # Simulate merge
                self.data = self.data[:index] + [merged] + self.data[index+2:]
                self.score += 10
                self.update_info()
                self.draw_blocks()
            else:
                self.score -= 5
                self.update_info()

    def run_timer(self):
        if self.time_left > 0:
            self.update_info()
            self.time_left -= 1
            self.root.after(1000, self.run_timer)
        else:
            self.end_game()

    def end_game(self):
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()
        tk.Label(self.canvas_frame, text=f" Time's Up! Final Score: {self.score}", font=("Arial", 16), fg="red").pack()


# Main Application
root = tk.Tk()
game = MergeSortGame(root)
root.mainloop()
