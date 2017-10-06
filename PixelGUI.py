#Developed by Zachary Williams

from tkinter import *
from functools import partial
from PIL import Image
import sys
from sys import platform


class mainclass(object):
    colorfillvar = 0
    gridwidth = 8
    gridheight = 8
    griddim = gridwidth * gridheight
    colors = []
    basecolor = "red"
    picname = []
    if platform == "linux" or platform == "linux2":
        buttonw = 2
        buttonh = 2
        toolbarw = 370
        toolbarh= 10
    elif platform == "darwin":
        buttonw = 2
        buttonh = 2
    elif platform == "win32" or "win64":
        buttonw = 2
        buttonh = 1
        toolbarw = 260
        toolbarh = 10
    COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace', 'linen', 'antique white',
              'papaya whip', 'blanched almond', 'bisque', 'peach puff', 'navajo white', 'lemon chiffon', 'mint cream',
              'azure', 'alice blue', 'lavender', 'lavender blush', 'misty rose', 'dark slate gray', 'dim gray',
              'slate gray', 'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue',
              'dark slate blue', 'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',
              'blue', 'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
              'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise', 'cyan',
              'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
              'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
              'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green', 'forest green',
              'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow', 'light yellow', 'yellow',
              'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown', 'indian red', 'saddle brown',
              'sandy brown', 'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange', 'coral', 'light coral',
              'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink', 'pale violet red', 'maroon',
              'medium violet red', 'violet red', 'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple',
              'medium purple', 'thistle', 'snow2', 'snow3', 'snow4', 'seashell2', 'seashell3', 'seashell4',
              'AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4',
              'PeachPuff2', 'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4', 'LemonChiffon2',
              'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'ivory2', 'ivory3', 'ivory4',
              'honeydew2', 'honeydew3', 'honeydew4', 'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2',
              'MistyRose3', 'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
              'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4', 'DodgerBlue2',
              'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2',
              'DeepSkyBlue3', 'DeepSkyBlue4', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1',
              'LightSkyBlue2', 'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3', 'SlateGray4',
              'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4', 'LightBlue1', 'LightBlue2',
              'LightBlue3', 'LightBlue4', 'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
              'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3', 'CadetBlue4', 'turquoise1',
              'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3', 'cyan4', 'DarkSlateGray1', 'DarkSlateGray2',
              'DarkSlateGray3', 'DarkSlateGray4', 'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2',
              'DarkSeaGreen3', 'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
              'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4', 'green2', 'green3', 'green4',
              'chartreuse2', 'chartreuse3', 'chartreuse4', 'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1',
              'DarkOliveGreen2', 'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
              'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4', 'LightYellow2',
              'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4', 'gold2', 'gold3', 'gold4', 'goldenrod1',
              'goldenrod2', 'goldenrod3', 'goldenrod4', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3',
              'DarkGoldenrod4', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
              'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1', 'burlywood2',
              'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1', 'tan2', 'tan4', 'chocolate1',
              'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'brown1', 'brown2',
              'brown3', 'brown4', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3',
              'LightSalmon4', 'orange2', 'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3',
              'DarkOrange4', 'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
              'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'HotPink1',
              'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4', 'LightPink1', 'LightPink2',
              'LightPink3', 'LightPink4', 'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4',
              'maroon1', 'maroon2', 'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
              'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1', 'plum2', 'plum3',
              'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2',
              'DarkOrchid3', 'DarkOrchid4', 'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1',
              'MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
              'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10', 'gray11',
              'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray20', 'gray21',
              'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28', 'gray29', 'gray30', 'gray31',
              'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37', 'gray38', 'gray39', 'gray40', 'gray42',
              'gray43', 'gray44', 'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray50', 'gray51', 'gray52',
              'gray53', 'gray54', 'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62',
              'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72',
              'gray73', 'gray74', 'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82',
              'gray83', 'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
              'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

    def __init__(self, master):

        self.fillbutton = "0"
        menu = Menu(master)
        master.config(menu=menu)
        bFrame = Frame(master)
        subMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=subMenu)
        topPadding = Frame(master, width=self.toolbarw, height=self.toolbarh)
        subMenu.add_command(label="New File", command=partial(self.importpic, bFrame, topPadding))
        subMenu.add_command(label="Placeholder", command=self.doNothing)
        subMenu.add_separator()
        subMenu.add_command(label="Placeholder", command=self.doNothing)

        editMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Remove Row", command=partial(self.removeRow, bFrame, topPadding))
        editMenu.add_command(label="Remove Col", command=partial(self.removeCol, bFrame, topPadding))
        viewMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="View", menu=viewMenu)
        viewMenu.add_command(label="Color Chart", command=self.viewColorChart)

        toolbar = Frame(master, width=self.toolbarw, height=20, bg="grey")
        frameSep = Frame(master, width=self.toolbarw, height=3, bg="black")
        bottomPadding = Frame(master, width=self.toolbarw, height=40)
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
            try:
                temp = Button(frame, width=self.buttonw, height=self.buttonh, bg=self.fillbutton,
                              command=partial(self.buttonColor, position, frame, padding))
            except:
                self.buttons[position] = Button(frame, width=self.buttonw, height=self.buttonh, bg='red',
                                                command=partial(self.buttonColor, position, frame, padding))
                self.buttons[position].grid(row=int(position / self.gridwidth), column=int(position % self.gridwidth))
                self.colors[position] = "red"
                print("Color entered is not recognized by tkinter. Please format the color as either a recognized tkinter string or #RGB or #RRGGBB or #RRRGGGBBB or #RRRRGGGGBBBB")
                return
            self.buttons[position] = Button(frame, width=self.buttonw, height=self.buttonh, bg=self.fillbutton,
                                            command=partial(self.buttonColor, position, frame, padding))
            self.buttons[position].grid(row=int(position / self.gridwidth), column=int(position % self.gridwidth))
            self.colors[position] = self.fillbutton

    def getEntry(self, entry, position, frame, colorask, padding):
        self.colorentry = entry.get()
        padding.config(width=self.toolbarw, height=self.toolbarh)
        colorask.destroy()
        if self.colorfillvar == 0:
            self.buttons[position].grid_forget()
            try:
                temp = Button(frame, width=self.buttonw, height=self.buttonh, bg=self.colorentry,
                              command=partial(self.buttonColor, position, frame, padding))
            except:
                self.buttons[position] = Button(frame, width=self.buttonw, height=self.buttonh, bg='red',
                                                command=partial(self.buttonColor, position, frame, padding))
                self.buttons[position].grid(row=int(position / self.gridwidth), column=int(position % self.gridwidth))
                self.colors[position] = "red"
                print("Something went wrong")
                return
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
            padding.config(width=self.toolbarw, height=self.toolbarh)
            return
        if entry2 != 1:
            try:
                temp1 = int(entry1.get())
                temp2 = int(entry2.get())
            except:
                kill.destroy()
                padding.config(width=self.toolbarw, height=self.toolbarh)
                return
            if int(entry1.get()) >30 or int(entry2.get()) >30:
                kill.destroy()
                padding.config(width=self.toolbarw, height=self.toolbarh)
                return
            self.gridwidth = int(entry1.get())
            self.gridheight = int(entry2.get())
        else:
            if entry1.get in self.COLORS:
                self.basecolor = entry1.get()
            else:
                kill.destroy()
                padding.config(width=self.toolbarw, height=self.toolbarh)
                return
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
        padding.config(width=self.toolbarw, height=self.toolbarh)

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
        file.write(
            "uint16_t bitmap[] = {" + ','.join([self.getButtonColor(button) for button in self.buttons]) + "};\n\n")
        file.write("int idx = 0;\nfor (int i=0; i< " + str(self.gridheight) + "; i++){\n" + "\tfor (int j=0; j< " + str(
            self.gridwidth) +
                   "; j++){\n\t\tST7735_DrawPixel(j,i,bitmap[idx]);\n\t\tidx++;\n\t}\n}")
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
            padding.config(width=self.toolbarw, height=self.toolbarh)
            return
        self.picname = entry1.get()
        print(self.picname)
        try:
            im = Image.open(self.picname)
        except:
            kill.destroy()
            padding.config(width=self.toolbarw, height=self.toolbarh)
            return
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
        padding.config(width=self.toolbarw, height=self.toolbarh)

    def viewColorChart(self):
        MAX_ROWS = 36
        FONT_SIZE = 10  # (pixels)
        ColorChart = Tk()
        ColorChart.title("Named colour chart")
        row = 0
        col = 0
        for color in self.COLORS:
            e = Label(ColorChart, text=color, background=color,
                      font=(None, -FONT_SIZE))
            e.grid(row=row, column=col, sticky=E + W)
            row += 1
            if (row > 36):
                row = 0
                col += 1

    def removeRow(self, frame, padding):
        gridask = Frame(padding)
        label_1 = Label(gridask, text="Row: ")
        entry_1 = Entry(gridask)
        buttonOK = Button(gridask, text="OK",
                          command=partial(self.manMatRow, entry_1, gridask, frame, padding))
        label_1.grid(row=0, sticky=E)
        entry_1.grid(row=0, column=1)
        buttonOK.grid(row=1, columnspan=2)
        gridask.pack()

    def removeCol(self, frame, padding):
        gridask = Frame(padding)
        label_1 = Label(gridask, text="Column: ")
        entry_1 = Entry(gridask)
        buttonOK = Button(gridask, text="OK",
                          command=partial(self.manMatCol, entry_1, gridask, frame, padding))
        label_1.grid(row=0, sticky=E)
        entry_1.grid(row=0, column=1)
        buttonOK.grid(row=1, columnspan=2)
        gridask.pack()

    def manMatRow(self, entry_1, gridask, frame, padding):
        try:
            temp1 = int(entry_1.get())
        except:
            print("Value given failed integer conversion")
            gridask.destroy()
            padding.config(width=self.toolbarw, height=self.toolbarh)
            return
        if int(entry_1.get()) <=0 or int(entry_1.get()) >self.gridheight:
            print("Integer given is out of bounds")
            gridask.destroy()
            padding.config(width=self.toolbarw, height=self.toolbarh)
            return
        rowID = int(entry_1.get())-1
        for i in range(self.griddim):
            self.buttons[i].grid_forget()
        self.buttons = []
        for i in range(self.gridwidth):
            del self.colors[self.gridwidth*rowID]
            print(i)
        self.gridheight = self.gridheight - 1
        self.griddim = self.gridheight*self.gridwidth
        for i in range(self.griddim):
            self.buttons.append(Button(frame, width=self.buttonw, height=self.buttonh, bg=self.colors[i],
                                       command=partial(self.buttonColor, i, frame, padding)))
            self.buttons[i].grid(row=int((i / self.gridwidth)), column=int((i % self.gridwidth)))
        gridask.destroy()
        padding.config(width=self.toolbarw, height=self.toolbarh)
        frame.pack()

    def manMatCol(self, entry_1, gridask, frame, padding):
        try:
            temp1 = int(entry_1.get())
        except:
            print("Value given failed integer conversion")
            gridask.destroy()
            padding.config(width=self.toolbarw, height=self.toolbarh)
            return
        if int(entry_1.get()) <=0 or int(entry_1.get()) >self.gridwidth:
            print("Integer given is out of bounds")
            gridask.destroy()
            padding.config(width=self.toolbarw, height=self.toolbarh)
            return
        colID = int(entry_1.get())-1
        for i in range(self.griddim):
            self.buttons[i].grid_forget()
        self.buttons = []
        temp = []
        j=0
        for i in range(self.griddim):
            if (i%self.gridwidth == colID):
                continue
            else:
                temp.append(self.colors[i])
                j=j+1
        self.colors = temp
        self.gridwidth = self.gridwidth - 1
        self.griddim = self.gridheight*self.gridwidth
        for i in range(self.griddim):
            self.buttons.append(Button(frame, width=self.buttonw, height=self.buttonh, bg=self.colors[i],
                                       command=partial(self.buttonColor, i, frame, padding)))
            self.buttons[i].grid(row=int((i / self.gridwidth)), column=int((i % self.gridwidth)))
        gridask.destroy()
        padding.config(width=self.toolbarw, height=self.toolbarh)
        frame.pack()




root = Tk()
z = mainclass(root)
root.mainloop()
sys.exit()
