import tkinter
root = tkinter.Tk()
root.resizable(False, False)
myCanvas = tkinter.Canvas(root, bg = "white", height = 600, width = 800)
shape1 = myCanvas.create_oval(20,20,100,100,fill="blue")
shape2 = myCanvas.create_rectangle(70,70,90,90 , fill = "teal")
#initializing
xx = yy = 3
aa = bb = 5
def move_shape():
    global xx, yy
    myCanvas.move(shape1,xx,yy)
    (x1, y1, x2, y2) = myCanvas.coords(shape1)
    if x1 <= 0 or x2 >= 800:
        xx = -xx
    if y1 <= 0 or y2 >= 600:
        yy = -yy

    global aa, bb
    myCanvas.move(shape2, aa, bb)
    (a1, b1, a2, b2) = myCanvas.coords(shape2)
    if a1 <= 0 or a2 >= 800:
        aa = -aa
    if b1 <= 0 or b2 >= 600:
        bb = -bb
    myCanvas.after(20, move_shape)
myCanvas.after(3,move_shape)

myCanvas.pack()
root.mainloop()

#0 is left wall 800 right for x
#o and 600 for y