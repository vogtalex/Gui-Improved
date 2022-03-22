from ast import Global
from pyexpat import model
# from models.net import *
# from csv_gui import *
# from tsne_run import *
import torch
import numpy as np
import matplotlib.pyplot as plt

import time
import tkinter as tk
from tkinter import messagebox as mb
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import torch
import torch.onnx as onnx
import torchvision.models as models
import torch.nn as nn
from torch.utils.data import DataLoader
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
import numpy as np
import matplotlib.pyplot as plt
import torchvision

import tkinter as tk
from tkinter import *

from PIL import Image, ImageTk

from functools import partial
import json

from numpy import load

npys = './npys'
eps = 'e3'
examples = 'examples'
limit = 10000

images_orig = np.load(os.path.join(npys, examples, 'advdata.npy')
                      ).astype(np.float64)[:limit]

# images_orig = np.load('./npys/advdata.npy').astype(np.float64)
images = []
for i in range(len(images_orig)):
    images.append(images_orig[i].reshape(28, 28))

# Variables initialized for my dataset. Can be changed for different user
path1 = "saved_image.png"
path2 = "tsne_output.png"
imageTitle = "What is this number?"

# This variable changes if user has labeled data or not. Change it to false if you don't have labeled data
labeledData = False

# This variable changes if user has model predictions. Change it to false if you don't have model predictions
modelData = False

# Count of image displayed currently and count guessed correctly in the GUI
global totalCount
totalCount = 0

# Generates an unlabeled image
def generateUnlabeledImage(count):
    image = images[count]
    plt.title(imageTitle)
    plt.imshow(image, cmap="gray")
    return plt.gcf()

# Iterates the total count to iterate through images
def countIterator():
    global totalCount
    totalCount = totalCount + 1
    return totalCount

# embeds the visualization in the appropriate column
def embedMatplot(fig, col):
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=col, padx=2, pady=2)

def myUnlabeledClick():
    # Create new image
    global totalCount

    currNum = e.get()

    # Add guess to CSV
    writeToCSV(currNum)

    totalCount = countIterator()

    # clear current matplots and embed new new ones
    plt.clf()
    embedMatplot(generateUnlabeledImage(totalCount),0)
    embedMatplot(generateTSNE(totalCount),1)

# Initialize CSV by deleting prior csv "response.csv"
initializeCSV()

# GUI
root = Tk()
root.title("Human Testing of Adversarial Training")

# Setup frames
# global image_frame
image_frame = tk.Frame(root, background="#FFFFFF", bd=1, relief="sunken")
input_frame = tk.Frame(root, bd=1, relief="sunken")
image_frame.grid(row=0, column=0, padx=2, pady=2)
input_frame.grid(row=1, column=0, padx=2, pady=2, columnspan=2)

# Configure frames
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)

# Create a photoimage object of the image in the path
embedMatplot(generateUnlabeledImage(0),0)
embedMatplot(generateTSNE(0),1)

# Creates entry box for user guess
lbl = Label(input_frame, text="What does this image depict?", font=20)
lbl.grid(row=0, column=0, sticky="nsew", padx=5, pady=20)

e = Entry(input_frame, width=30, justify=CENTER, font=20)
e.grid(row=0, column=1, sticky="nsew", padx=5, pady=20)
e.insert(0, "Enter your guess here")

lbl = Label(input_frame, text="Which visualizations led you to this answer?", justify=LEFT, font=20)
lbl.grid(row=1, column=0, sticky="nsew", padx=5, pady=20)

a = Entry(input_frame, width=30, justify=CENTER, font=20)
a.grid(row=1, column=1, sticky="nsew", padx=5, pady=20)

# Adds a Button
myButton = Button(input_frame,
                  text="Submit",
                  height=3,
                  width=30,
                  font=20,
                  background='#343a40',
                  fg='white',
                  command=partial(myUnlabeledClick))
myButton.grid(row=2, column=1, pady=20)

exit_button = Button(root, text="Exit",
                     command=root.quit,
                     height=3,
                     width=50,
                     background='#D11A2A',
                     fg='white',
                     font=50)
exit_button.grid(row=3, column=0, pady=20, columnspan=2)

root.configure(background="white")

# Loop
root.protocol("WM_DELETE_WINDOW", root.destroy)
root.mainloop()