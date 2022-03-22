from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *

from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.configure(bg = "#FFFFFF")

frame = Frame(window)
frame.grid(row=0,column=0, sticky="n")

def gridImages(Directory, r, c): 
    image1 = Image.open(Directory)
    test = ImageTk.PhotoImage(image1)
    label1 = Label(frame, image=test)
    label1.image = test
    label1.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)

gridImages(relative_to_assets("image_1.png"), 0, 0)
gridImages(relative_to_assets("image_2.png"), 0, 1)
gridImages(relative_to_assets("image_3.png"), 1, 0)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 300,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.grid(row = 0, column = 1)

canvas.create_rectangle(
    0,
    0,
    300,
    800,
    fill="#D2D2D2",
    outline="")

canvas.create_text(
    12,
    185.0,
    anchor="nw",
    text="Which visualization\nassisted you in making \nthis decision?",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    12,
    419.0,
    anchor="nw",
    text="Prediction Confidence:",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    12,
    104.0,
    anchor="nw",
    text="Prediction:",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    200,
    120.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)

canvas.create_window(200, 120.5, window=entry_1)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    width=298.1923828125,
    height=115.14483642578125
)

canvas.create_window(150, 750, window=button_1)

#Radio Buttons
selected_visual = StringVar()
selected_visual.set(' ')
selections = (('Image', 'I'),
         ('TSNE', 'T'),
         ('Histogram', 'H'))

height = 300
# radio buttons
for visual in selections:
    r = Radiobutton(
        window,
        text=visual[0],
        value=visual[1],
        variable=selected_visual,
        anchor=W,
        justify = LEFT,
        bg="#D2D2D2"
    )
    canvas.create_window(100, height, window=r)
    height += 30




window.resizable(False, False)
window.mainloop()
