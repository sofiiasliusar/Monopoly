import tkinter as tk
from tkinter import messagebox
import random

class Player:
    def __init__(self, name, balance=1500):
        self.name = name
        self.balance = balance
        self.position = 0

class MonopolyGame:
    def __init__(self, master, players):
        self.master = master
        self.master.title("Monopoly Game")

        self.players = [Player(name) for name in players]
        self.current_player_index = 0

        self.create_board()
        self.create_dice_button()

    def create_board(self):
        # Customize your game board GUI here
        # For simplicity, let's create a basic board with labels
        self.board_label = tk.Label(self.master, text="Monopoly Board")
        self.board_label.pack()

    def create_dice_button(self):
        self.dice_button = tk.Button(self.master, text="Roll Dice", command=self.roll_dice)
        self.dice_button.pack()

    def roll_dice(self):
        dice_result = random.randint(1, 6)
        messagebox.showinfo("Dice Roll", f"{self.players[self.current_player_index].name} rolled a {dice_result}")

        # Update player position (for simplicity, just increment position)
        self.players[self.current_player_index].position += dice_result

        # Update GUI to show player position
        self.board_label.config(text=f"{self.players[self.current_player_index].name}'s Position: {self.players[self.current_player_index].position}")

        # Switch to the next player
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

if __name__ == "__main__":
    root = tk.Tk()
    players = ["Player 1", "Player 2"]
    monopoly_game = MonopolyGame(root, players)
    root.mainloop()
