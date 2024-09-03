from tkinter import*
from constant import*
import new
from cell import Cell
from data import*

root = Tk()

#changes background color and stuff
root.configure(bg = "white")
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title("Shadow Wizard Money Gang")
root.resizable(False, False)

#making the frame that will hold the gui and other elements
top_frame = Frame(root, bg= "grey", width = WIDTH, height = new.height_prct(10))
top_frame.place(x=0, y=0)

#displays game title
game_title = Label(top_frame, bg = "grey", fg="white", text="Shadow Wizard Money Gang",
                   font= ('', 20))
game_title.place(x=WIDTH/2, y=20, anchor='center')

centre_frame = Frame(root, bg="black", width = WIDTH, height = new.height_prct(90))
centre_frame.place(x=0, y=new.height_prct(10))

score_frame = Frame(root, bg="grey", width = WIDTH, height = new.height_prct(15))
score_frame.place(x=0, y=new.height_prct(85))

score_label = Label(score_frame, text=f'Score: ${SCORE}', bg="grey", fg="white", font=('', 16))
score_label.pack(expand=True)

for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        c = Cell(x, y, score_label)
        c.create_btn_object(centre_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

Cell.randomize_mines()

root.mainloop()


