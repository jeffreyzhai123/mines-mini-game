from tkinter import Tk, Frame, Label, Button, StringVar
from tkmacosx import Button as MacButton  # Import Button from tkmacosx
import random 
import new
from constant import*
import sys
from data import*

class Cell:
    all = []
    score = SCORE

    def __init__(self, x, y, score_label, is_mine=False, clicked=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.clicked = clicked
        self.x = x
        self.y = y
        self.score_label = score_label

        #Append the obj to the cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        #MacOs is stupid and if you use normal tkinter buttons, the bg color wont change
        #why? because MacOs said so
        #instead import tkmacosx and use MacButton 
        btn = MacButton(
            location,
            width=120,
            height=50, 
        )
        #handles the button click event, Button-1 (left-click)
        btn.bind('<Button-1>', self.left_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if not self.clicked:
            if self.is_mine:
                self.show_mine()
                self.clicked = True
            else:
                self.show_cell()
                self.clicked = True

    def show_mine(self):
        #logic to interrpt the game and display a msg that player lost
        self.cell_btn_object.configure(text='mines hit')
        self.cell_btn_object.configure(bg="red")
        Cell.score = 0
        SCORE = Cell.score
        self.score_label.config(text=f'Score: ${SCORE}')
        #implement a function to show entire board, somehow await (call sleep(5) maybe) then exit system
        sys.exit()
    
    def show_cell(self):
        self.cell_btn_object.configure(text='safe')
        self.cell_btn_object.configure(bg="green")
        Cell.score = Cell.score * 2
        SCORE = Cell.score
        self.score_label.config(text=f'Score: ${SCORE}')

    @staticmethod
    def randomize_mines():
        #second arg gives the number of mines
        picked_cells = random.sample(
            Cell.all, MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"

