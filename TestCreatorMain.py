import tkinter as tk
from threading import *
from turtle import left
from PIL import Image, ImageTk
class TestCreatorWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Lane Recognition Test Window")

        self._createToolbar(self.root)
        self._createImageWin(self.root)
        self.root.mainloop()
    
    def _createImageWin(self, MainWin):
        self.ImageFrame = tk.Frame(MainWin)

        self.BeforeFrame = tk.Frame(self.ImageFrame)
        self.BeforeCanvas = tk.Canvas(self.BeforeFrame)
        self.BeforeImg = ImageTk.PhotoImage(file='./BlackImage.jpg')
        self.BeforeCanvas.create_image(20, 20, anchor=tk.NW, image=self.BeforeImg)

        self.AfterFrame = tk.Frame(self.ImageFrame)
        self.AfterCanvas = tk.Canvas(self.AfterFrame)
        self.AfterImg = ImageTk.PhotoImage(file='./BlackImage.jpg')
        self.AfterCanvas.create_image(20, 20, anchor=tk.NW, image=self.AfterImg)

        self.BeforeCanvas.pack()
        self.AfterCanvas.pack()
        self.BeforeFrame.pack(side=tk.LEFT, anchor=tk.NW)
        self.AfterFrame.pack(side=tk.LEFT, anchor=tk.NW)
        self.ImageFrame.pack(side=tk.LEFT, anchor=tk.NW)

    def _createToolbar(self, MainWin):
        def LoadImage():
            pass
        def SaveImage():
            pass
        self.ToolBarFrame = tk.Frame(MainWin)
        self.LoadImageButton = tk.Button(self.ToolBarFrame, text='Load Image', command=LoadImage(), width = 15)
        self.SaveButton = tk.Button(self.ToolBarFrame, text="Save Image", command = SaveImage(), width = 15)

        self.ToolBarFrame.pack(side="left", anchor=tk.NW)
        self.LoadImageButton.pack(side=tk.TOP, anchor=tk.NW)
        self.SaveButton.pack(side=tk.TOP, anchor=tk.NW)

if __name__=="__main__":
    TestCreatorWindow()