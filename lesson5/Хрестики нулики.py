import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeBot:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Хрестики-Нулики: Гравець vs Бот")

        self.player = "X"
        self.bot = "O"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_board()
        self.window.mainloop()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.window, text="", font=('Arial', 40), width=5, height=2,
                                   command=lambda r=row, c=col: self.player_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def player_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.player
            self.buttons[row][col].config(text=self.player)

            if self.check_winner(self.player):
                messagebox.showinfo("Гра закінчена", "Ви перемогли!")
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("Гра закінчена", "Нічия!")
                self.reset_game()
            else:
                self.window.after(500, self.bot_move)  # затримка для природності

    def bot_move(self):
        empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = self.bot
            self.buttons[row][col].config(text=self.bot)

            if self.check_winner(self.bot):
                messagebox.showinfo("Гра закінчена", "Бот переміг!")
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("Гра закінчена", "Нічия!")
                self.reset_game()

    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")

if __name__ == "__main__":
    TicTacToeBot()

