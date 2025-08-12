import tkinter as tk
from tkinter import messagebox
import random
import time

class CardMatchingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Card Matching Game")
        self.root.configure(bg='#2c3e50')
        
        # Game variables
        self.cards = []
        self.buttons = []
        self.flipped_cards = []
        self.matched_pairs = 0
        self.total_pairs = 8
        self.attempts = 0
        self.start_time = None
        
        # Card symbols (emojis for visual appeal)
        self.symbols = ['🎮', '🎯', '🎲', '🎪', '🎨', '🎭', '🎪', '🎸'] * 2
        
        self.create_widgets()
        self.setup_game()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="Card Matching Game", 
            font=('Arial', 24, 'bold'),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        title_label.grid(row=0, column=0, columnspan=4, pady=10)
        
        # Stats frame
        stats_frame = tk.Frame(self.root, bg='#34495e')
        stats_frame.grid(row=1, column=0, columnspan=4, pady=5)
        
        self.attempts_label = tk.Label(
            stats_frame,
            text="Attempts: 0",
            font=('Arial', 12),
            fg='#ecf0f1',
            bg='#34495e'
        )
        self.attempts_label.pack(side=tk.LEFT, padx=10)
        
        self.pairs_label = tk.Label(
            stats_frame,
            text="Pairs: 0/8",
            font=('Arial', 12),
            fg='#ecf0f1',
            bg='#34495e'
        )
        self.pairs_label.pack(side=tk.LEFT, padx=10)
        
        self.time_label = tk.Label(
            stats_frame,
            text="Time: 00:00",
            font=('Arial', 12),
            fg='#ecf0f1',
            bg='#34495e'
        )
        self.time_label.pack(side=tk.LEFT, padx=10)
        
        # Game frame
        self.game_frame = tk.Frame(self.root, bg='#2c3e50')
        self.game_frame.grid(row=2, column=0, columnspan=4, pady=10)
        
        # Control buttons
        button_frame = tk.Frame(self.root, bg='#2c3e50')
        button_frame.grid(row=3, column=0, columnspan=4, pady=10)
        
        self.new_game_btn = tk.Button(
            button_frame,
            text="New Game",
            command=self.new_game,
            font=('Arial', 12, 'bold'),
            bg='#3498db',
            fg='white',
            padx=20,
            pady=5
        )
        self.new_game_btn.pack(side=tk.LEFT, padx=5)
        
        self.exit_btn = tk.Button(
            button_frame,
            text="Exit",
            command=self.root.quit,
            font=('Arial', 12, 'bold'),
            bg='#e74c3c',
            fg='white',
            padx=20,
            pady=5
        )
        self.exit_btn.pack(side=tk.LEFT, padx=5)
        
    def setup_game(self):
        # Clear previous game
        for widget in self.game_frame.winfo_children():
            widget.destroy()
        self.buttons.clear()
        
        # Shuffle cards
        self.cards = self.symbols.copy()
        random.shuffle(self.cards)
        
        # Create card buttons
        for i in range(16):
            btn = tk.Button(
                self.game_frame,
                text="?",
                font=('Arial', 20, 'bold'),
                width=4,
                height=2,
                bg='#95a5a6',
                fg='#2c3e50',
                command=lambda idx=i: self.flip_card(idx)
            )
            btn.grid(row=i//4, column=i%4, padx=5, pady=5)
            self.buttons.append(btn)
        
        # Reset game state
        self.flipped_cards = []
        self.matched_pairs = 0
        self.attempts = 0
        self.start_time = time.time()
        self.update_stats()
        
    def flip_card(self, index):
        # Prevent flipping if already matched or already flipped
        if self.buttons[index]['state'] == 'disabled' or index in self.flipped_cards:
            return
            
        # Prevent flipping more than 2 cards
        if len(self.flipped_cards) >= 2:
            return
            
        # Show card
        self.buttons[index].config(text=self.cards[index], bg='#3498db')
        self.flipped_cards.append(index)
        
        # Check for match if 2 cards are flipped
        if len(self.flipped_cards) == 2:
            self.attempts += 1
            self.update_stats()
            self.root.after(1000, self.check_match)
            
    def check_match(self):
        idx1, idx2 = self.flipped_cards
        
        if self.cards[idx1] == self.cards[idx2]:
            # Match found
            self.buttons[idx1].config(state='disabled', bg='#2ecc71')
            self.buttons[idx2].config(state='disabled', bg='#2ecc71')
            self.matched_pairs += 1
            
            if self.matched_pairs == self.total_pairs:
                self.game_won()
        else:
            # No match
            self.buttons[idx1].config(text="?", bg='#95a5a6')
            self.buttons[idx2].config(text="?", bg='#95a5a6')
            
        self.flipped_cards = []
        self.update_stats()
        
    def update_stats(self):
        self.attempts_label.config(text=f"Attempts: {self.attempts}")
        self.pairs_label.config(text=f"Pairs: {self.matched_pairs}/{self.total_pairs}")
        
        if self.start_time:
            elapsed = int(time.time() - self.start_time)
            minutes = elapsed // 60
            seconds = elapsed % 60
            self.time_label.config(text=f"Time: {minutes:02d}:{seconds:02d}")
            
    def game_won(self):
        elapsed = int(time.time() - self.start_time)
        minutes = elapsed // 60
        seconds = elapsed % 60
        
        messagebox.showinfo(
            "Congratulations!",
            f"You won!\n\n"
            f"Attempts: {self.attempts}\n"
            f"Time: {minutes:02d}:{seconds:02d}\n\n"
            f"Great job!"
        )
        
    def new_game(self):
        self.setup_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = CardMatchingGame(root)
    root.mainloop()
