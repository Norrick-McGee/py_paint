import tkinter as tk 
import tkinter.font as font

#Class

class painty:

#Variables

    drawing_tool = "line"

    mouse1 = "up"

    xpos = None
    ypos = None

    x1_point,y1_point,x2_point,y2_point = None, None, None, None

#mouse up
    def m1_but_up(self, event = None):
        self.mouse1 = "up"

        self.x_pos = None
        self.y_pos = None

        self.x_point = event.x
        self.y_point = event.y

        if self.drawing_tool == "line":
            self.line_draw(event)
        

#mouse down

    def m1_but_down(self, event = None):
        self.mouse1 = "down"

        self.x1_point = event.x
        self.y1_point = event.y
        
#mouse move

    def motion(self, event = None):

        if self.drawing_tool == "pencil":

            if self.x_pos is not None and self.y_pos is not None:

                event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth = TRUE)

            self.x_pos = event.x
            self.y_pos = event.y
            
                
#pencil draw

#line draw

#arc draw

#oval draw

#Rect draw

#Text draw

#init

    def __init__(self, root):
        drawing_area = Canvas(root)

        drawing_area.pack()

        drawing.area.bind("<Motion>", self.motion)
        drawing.area.bind("<ButtonPress-1>", self.m1_but_down)
        drawing.area.bind("<ButtonRelease-1>", self.m1_but_up)

root = Tk() 
painty = PaintApp(root)
root.mainloop()

        
