import tkinter

root = tkinter.Tk()
root.resizable(False,False)

myCanvas = tkinter.Canvas(root, bg = "green", height = 800, width = 800)

'''color1 = input("Enter the color for shape 1: ")
color2 = input("Enter the color for shape 2: ")
color3 = input("Enter the color for shape 3: ")'''

x = "red"
y = "blue"
head = myCanvas.create_rectangle(300,200,500,400, fill = y)
neck = myCanvas.create_rectangle(350,400,450,450, fill = x)
body = myCanvas.create_rectangle(300,450,500,650, fill = y)
leftarm = myCanvas.create_rectangle(250,475,300,600, fill = x)
lefthand = myCanvas.create_rectangle(260,600,300,625, fill = x)
rightarm = myCanvas.create_rectangle(500,475,550,600, fill = x)
righthand = myCanvas.create_rectangle(500,600,540,625, fill = x)
#rightleg = myCanvas.create_rectangle()

myCanvas.pack()
root.mainloop()