import tkinter

#define a class for the chess-board
class ChessBoard:
    def __init__(self):
        self.x=0
        self.y=0

    def draw_board(self):
        for i in range(0,8):
            if i%2:
                color1="lavender blush"
                color2="lavender"
            else:
                color1="lavender"
                color2="lavender blush"
            for j in range(0,8):
                if j%2:
                    self.shape2 = myCanvas.create_rectangle(self.x, self.y, self.x+100, self.y+100, fill=color1)
                else:
                    self.shape2 = myCanvas.create_rectangle(self.x, self.y, self.x + 100, self.y + 100, fill=color2)
                self.x+=100
            self.x=0
            self.y+=100
# init tk
root = tkinter.Tk()
root.resizable(False,False)
# create canvas
myCanvas = tkinter.Canvas(root, bg="white", height=800, width=800)


cb_obj=ChessBoard()
cb_obj.draw_board()

#Black pieces
bf1 = tkinter.PhotoImage(file=r"C:\Users\user\PycharmProjects\OOPNotes\b-fort.png")
bf1 = bf1.subsample(5,5)
bfort = myCanvas.create_image(50,50,image=bf1)

bk1 = tkinter.PhotoImage(file=r"C:\Users\user\PycharmProjects\OOPNotes\b-knight.png")
bk1 = bk1.subsample(5,5)
bkinght1 = myCanvas.create_image(150,50, image = bk1)

bb1 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\b-bishop.png")
bb1 = bb1.subsample(5,5)
bbishop = myCanvas.create_image(250,50, image = bb1)

bk = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\b-king.png")
bk = bk.subsample(5,5)
blackking = myCanvas.create_image(350,50, image = bk)

bq = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\b-queen.png")
bq = bq.subsample(5,5)
blackqueen = myCanvas.create_image(450,50,image = bq)

bf2 = tkinter.PhotoImage(file=r"C:\Users\user\PycharmProjects\OOPNotes\b-fort.png")
bf2 = bf2.subsample(5,5)
bfort2 = myCanvas.create_image(750,50,image=bf2)

bk2 = tkinter.PhotoImage(file=r"C:\Users\user\PycharmProjects\OOPNotes\b-knight.png")
bk2 = bk2.subsample(5,5)
bkinght2 = myCanvas.create_image(650,50, image = bk2)

bb2 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\b-bishop.png")
bb2 = bb2.subsample(5,5)
bbishop2 = myCanvas.create_image(550,50, image = bb2)

bp = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\b-pawn.png")
bp = bp.subsample(5,5)
bpawn = myCanvas.create_image(50,150, image = bp)

bp2 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\b-pawn.png")
bp2 = bp2.subsample(5,5)
bpawn2 = myCanvas.create_image(150,150, image = bp)

bp3 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\b-pawn.png")
bp3 = bp3.subsample(5,5)
bpawn3 = myCanvas.create_image(250,150, image = bp)

bp4 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\b-pawn.png")
bp4 = bp4.subsample(5,5)
bpawn4 = myCanvas.create_image(350,150, image = bp)

bp5 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\b-pawn.png")
bp5 = bp5.subsample(5,5)
bpawn5 = myCanvas.create_image(450,150, image = bp)

bp6 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\b-pawn.png")
bp6 = bp6.subsample(5,5)
bpawn6 = myCanvas.create_image(550,150, image = bp)

bp7 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\b-pawn.png")
bp7 = bp7.subsample(5,5)
bpawn7 = myCanvas.create_image(650,150, image = bp)

bp8 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\b-pawn.png")
bp8 = bp8.subsample(5,5)
bpawn8 = myCanvas.create_image(750,150, image = bp)

#White pieces
wk = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\w-king.png")
wk = wk.subsample(5,5)
wking = myCanvas.create_image(350,750, image = wk)


wq = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\w-queen.png")
wq = wq.subsample(5,5)
wqueen = myCanvas.create_image(450,750, image = wq)

wb1 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\w-bishop.png")
wb1 = wb1.subsample(5,5)
wbishop = myCanvas.create_image(250,750, image = wb1)

wk1 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\w-knight.png")
wk1 = wk1.subsample(5,5)
wknight = myCanvas.create_image(150,750,image = wk1)

wf = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\w-fort.png")
wf = wf.subsample(5,5)
whitefort1 = myCanvas.create_image(50,750, image = wf)


wb2 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\w-bishop.png")
wb2 = wb2.subsample(5,5)
wbishop2 = myCanvas.create_image(550,750, image = wb2)


wk2 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\w-knight.png")
wk2 = wk2.subsample(5,5)
wknight2 = myCanvas.create_image(650,750, image = wk2)

wf2 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\w-fort.png")
wf2 = wf2.subsample(5,5)
wfort2 = myCanvas.create_image(750,750, image = wf2)

wp = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\w-pawn.png")
wp = wp.subsample(5,5)
wpawn = myCanvas.create_image(50,650, image = wp)

wp2 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\w-pawn.png")
wp2 = wp2.subsample(5,5)
wpawn2 = myCanvas.create_image(150,650, image = wp)

wp3 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\w-pawn.png")
wp3 = wp3.subsample(5,5)
wpawn3 = myCanvas.create_image(250,650, image = wp)

wp4 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\w-pawn.png")
wp4 = wp4.subsample(5,5)
wpawn4 = myCanvas.create_image(350,650, image = wp)

wp5 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\w-pawn.png")
wp5 = wp5.subsample(5,5)
wpawn5 = myCanvas.create_image(450,650, image = wp)

wp6 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\w-pawn.png")
wp6 = wp6.subsample(5,5)
wpawn6 = myCanvas.create_image(550,650, image = wp)

wp7 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\w-pawn.png")
wp7 = wp7.subsample(5,5)
wpawn7 = myCanvas.create_image(650,650, image = wp)

wp8 = tkinter.PhotoImage(file = r"C:\Users\user\PycharmProjects\OOPNotes\w-pawn.png")
wp8 = wp8.subsample(5,5)
wpawn8 = myCanvas.create_image(750,650, image = wp)




# add to window and show
myCanvas.pack()
root.mainloop()

