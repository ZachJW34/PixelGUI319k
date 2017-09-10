from tkinter import *
from functools import partial
from PIL import Image
import sys


class ZachsButtons(object):
    colorfillvar = 0
    gridwidth = 8
    gridheight = 8
    griddim = gridwidth * gridheight
    colors = []
    basecolor = "red"
    picname = []
    buttonw = 2
    buttonh = 2

    def __init__(self, master):

        self.fillbutton = "0"
        menu = Menu(master)
        master.config(menu=menu)
        bFrame = Frame(master)
        subMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=subMenu)
        topPadding = Frame(master, width=370, height=40)
        subMenu.add_command(label="New Project", command=self.doNothing)
        subMenu.add_command(label="New File", command=partial(self.importpic, bFrame, topPadding))
        subMenu.add_separator()
        subMenu.add_command(label="Exit", command=self.doNothing)

        editMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Rect2Square", command=self.rect2square)
        toolbar = Frame(master, width=370, height=20, bg="grey")
        frameSep = Frame(master, width=370, height=2, bg="black")
        bottomPadding = Frame(master, width=370, height=40)
        self.setfillbutton = Checkbutton(bottomPadding, text="Fill")
        self.setfillbutton.config(state=DISABLED)
        self.setfillbutton.pack(side=LEFT)
        colorselect = Button(toolbar, text="Set Color", command=partial(self.colorfillask, bFrame, topPadding))
        colorselect.pack(side=LEFT)
        gridSelect = Button(toolbar, text="Grid Select", command=partial(self.changeGrid, bFrame, topPadding))
        gridSelect.pack(side=LEFT)
        View = Button(toolbar, text="View", command=partial(self.viewImage, 40))
        View.pack(side=LEFT)
        baseCol = Button(toolbar, text="Color Fill", command=partial(self.fillColor, bFrame, topPadding))
        baseCol.pack(side=LEFT)
        exportbut = Button(toolbar, text="Export", command=self.expFunc)
        exportbut.pack(side=LEFT)
        self.buttons = []

        for i in range(self.griddim):
            self.buttons.append(Button(bFrame, width=self.buttonw, height=self.buttonh, bg=self.basecolor,
                                       command=partial(self.buttonColor, i, bFrame, topPadding)))
            self.buttons[i].grid(row=int((i / self.gridwidth)), column=int((i % self.gridwidth)))
            self.colors.append(self.basecolor)
        toolbar.pack_propagate(0)
        toolbar.pack(side=TOP)
        frameSep.pack(side=TOP)
        topPadding.pack(side=TOP)
        bFrame.pack()
        bottomPadding.pack(side=BOTTOM)

    def doNothing(self):
        print("Nope")

    def buttonColor(self, position, frame, padding):

        if self.colorfillvar == 0:
            colorask = Frame(padding)
            label_1 = Label(colorask, text="What Color?")
            entry_1 = Entry(colorask)
            label_2 = Label(colorask, text="Input takes lower case standard color, \nor #xxxxxxxxx hexadecimal number ")
            buttonOK = Button(colorask, text="OK",
                              command=partial(self.getEntry, entry_1, position, frame, colorask, padding))
            label_1.grid(row=0, sticky=E)
            entry_1.grid(row=0, column=1)
            label_2.grid(row=1, columnspan=2)
            buttonOK.grid(row=2, columnspan=2)
            colorask.pack()
        else:
            self.buttons[position].grid_forget()
            self.buttons[position] = Button(frame, width=self.buttonw, height=self.buttonh, bg=self.fillbutton,
                                            command=partial(self.buttonColor, position, frame, padding))
            self.buttons[position].grid(row=int(position / self.gridwidth), column=int(position % self.gridwidth))
            self.colors[position] = self.fillbutton

    def getEntry(self, entry, position, frame, colorask, padding):
        if entry.get() == "":
            colorask.destroy()
            return
        self.colorentry = entry.get()
        colorask.destroy()
        if self.colorfillvar == 0:
            self.buttons[position].grid_forget()
            self.buttons[position] = Button(frame, width=self.buttonw, height=self.buttonh, bg=self.colorentry,
                                            command=partial(self.buttonColor, position, frame, padding))
            self.buttons[position].grid(row=int(position / self.gridwidth), column=int(position % self.gridwidth))
            self.colors[position] = self.colorentry
        else:
            self.fillbutton = self.colorentry

    def getButtonColor(self, button):
        rgb = button.winfo_rgb(button.cget('bg'))
        r = (rgb[0] >> 11)
        g = (rgb[1] >> 10)
        g = g << 5
        b = rgb[2] >> 11
        b = b << 11
        rgb = b + g + r
        return '0x%04x' % (rgb)

    def colorfillask(self, frame, padding):

        colorask = Frame(padding)

        label_1 = Label(colorask, text="What Color?")
        entry_1 = Entry(colorask)
        label_2 = Label(colorask, text="Input takes lower case standard color, \nor #xxxxxxxxx hexadecimal number ")
        container = Frame(colorask)
        buttonOK = Button(container, text="OK", command=partial(self.getEntry, entry_1, 1, frame, colorask, padding))
        buttonSet = Button(container, text="Set", command=self.setfillvar)
        buttonClear = Button(container, text="Clear", command=self.clearfillvar)

        label_1.grid(row=0, sticky=E)
        entry_1.grid(row=0, column=1)
        label_2.grid(row=1, columnspan=2)
        buttonOK.grid(row=1, column=1)
        buttonSet.grid(row=1, column=2)
        buttonClear.grid(row=1, column=3)
        container.grid(row=2, columnspan=2)
        colorask.pack()

    def setfillvar(self):
        self.setfillbutton.select()
        self.colorfillvar = 1

    def clearfillvar(self):
        self.setfillbutton.deselect()
        self.colorfillvar = 0

    def changeGrid(self, frame, padding):
        gridask = Frame(padding)
        label_1 = Label(gridask, text="Grid Width:")
        entry_1 = Entry(gridask)
        label_2 = Label(gridask, text="Grid Height")
        entry_2 = Entry(gridask)
        buttonOK = Button(gridask, text="OK",
                          command=partial(self.getgridEntries, entry_1, entry_2, gridask, frame, padding))
        label_1.grid(row=0, sticky=E)
        entry_1.grid(row=0, column=1)
        label_2.grid(row=1, column=0)
        entry_2.grid(row=1, column=1)
        buttonOK.grid(row=2, columnspan=2)
        gridask.pack()

    def getgridEntries(self, entry1, entry2, kill, frame, padding):
        if entry1.get() == "":
            kill.destroy()
            return
        if entry2 != 1:
            self.gridwidth = int(entry1.get())
            self.gridheight = int(entry2.get())
        else:
            self.basecolor = entry1.get()
        for i in range(self.griddim):
            self.buttons[i].grid_forget()
        self.griddim = self.gridwidth * self.gridheight
        self.colors = []
        self.buttons = []
        for i in range(self.griddim):
            self.buttons.append(Button(frame, width=self.buttonw, height=self.buttonh, bg=self.basecolor,
                                       command=partial(self.buttonColor, i, frame, padding)))
            self.buttons[i].grid(row=int((i / self.gridwidth)), column=int((i % self.gridwidth)))
            self.colors.append(self.basecolor)
        frame.pack()
        kill.destroy()

    def viewImage(self, size):
        pixelI = Tk()
        canvas = Canvas(pixelI, width=self.gridwidth * size, height=self.gridheight * size)
        canvas.pack()
        for i in range(self.gridheight):
            for j in range(self.gridwidth):
                canvas.create_rectangle(j * size, i * size, j * size + size, i * size + size,
                                        fill=self.colors[i * self.gridwidth + j], width=0)

    def fillColor(self, frame, padding):
        fillAsk = Frame(padding)
        label_1 = Label(fillAsk, text="What Color?")
        entry_1 = Entry(fillAsk)
        label_2 = Label(fillAsk, text="Input takes lower case standard color, \nor #xxxxxxxxx hexadecimal number ")
        buttonOK = Button(fillAsk, text="OK", command=partial(self.getgridEntries, entry_1, 1, fillAsk, frame, padding))
        label_1.grid(row=0, sticky=E)
        entry_1.grid(row=0, column=1)
        label_2.grid(row=1, columnspan=2)
        buttonOK.grid(row=2, columnspan=2)
        fillAsk.pack()

    def expFunc(self):
        print('writing file')
        file = open("testfile.txt", "w")
        file.write("uint16_t bitmap[] = {")
        file.write(','.join([self.getButtonColor(button) for button in self.buttons]))
        file.write("}")
        file.close()

    def importpic(self, frame, padding):
        resizeask = Frame(padding)
        label_1 = Label(resizeask, text="Picture Name:")
        entry_1 = Entry(resizeask)
        label_2 = Label(resizeask, text="Resize Width")
        entry_2 = Entry(resizeask)
        label_3 = Label(resizeask, text="Resize Height")
        entry_3 = Entry(resizeask)
        buttonOK = Button(resizeask, text="OK",
                          command=partial(self.resizeandplace, entry_1, entry_2, entry_3, resizeask, frame, padding))
        label_1.grid(row=0, sticky=E)
        entry_1.grid(row=0, column=1)
        label_2.grid(row=1, column=0)
        entry_2.grid(row=1, column=1)
        label_3.grid(row=2, column=0)
        entry_3.grid(row=2, column=1)
        buttonOK.grid(row=3, columnspan=2)
        resizeask.pack()

    def resizeandplace(self, entry1, entry2, entry3, kill, frame, padding):
        if entry1.get() == "" or entry2.get() == "" or entry3.get() == "":
            kill.destroy()
            return
        self.picname = entry1.get()
        print(self.picname)
        for i in range(self.griddim):
            self.buttons[i].grid_forget()
        temp1 = self.griddim
        temp2 = self.gridwidth
        temp3 = self.griddim
        self.gridwidth = int(entry2.get())
        self.gridheight = int(entry3.get())
        self.griddim = self.gridheight * self.gridwidth
        im = Image.open(self.picname)
        im = im.resize((self.gridwidth, self.gridheight), Image.NEAREST)
        pix = im.convert('RGB')
        self.colors = []
        self.buttons = []
        for i in range(self.griddim):
            r, g, b = pix.getpixel((int(i % self.gridwidth), int(i / self.gridwidth)))
            # print(int(i%self.gridheight), int(i/self.gridheight))
            # print(r,g,b)
            rgb = (r << 16) + (g << 8) + b
            rgb = "#%0.6x" % rgb
            # print(rgb)
            self.buttons.append(Button(frame, width=self.buttonw, height=self.buttonh, bg=rgb,
                                       command=partial(self.buttonColor, i, frame, padding)))
            if self.gridwidth < 55 or self.gridheight < 30:
                self.buttons[i].grid(row=int((i / self.gridwidth)), column=int((i % self.gridwidth)))
            self.colors.append(rgb)
        print("Check")
        if self.gridwidth > 55 or self.gridheight > 30:
            print("did it work?")
            self.expFunc()
            self.viewImage(4)
            self.griddim = temp1
            self.gridwidth = temp2
            self.gridheight = temp3
            buttons = []
            for i in range(self.griddim):
                self.buttons.append(Button(frame, width=self.buttonw, height=self.buttonh, bg=self.basecolor,
                                           command=partial(self.buttonColor, i, frame, padding)))
                self.buttons[i].grid(row=int((i / self.gridwidth)), column=int((i % self.gridwidth)))
                self.colors.append(self.basecolor)
            frame.pack()
        else:
            frame.pack()
        kill.destroy()
        im.save('resized_image.png')

    def rect2square(self):
        self.buttonw = 2
        self.buttonh = 1


root = Tk()
z = ZachsButtons(root)
root.mainloop()

sys.exit()