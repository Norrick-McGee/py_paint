from tkinter import * 
import tkinter.font as font

#Class

class painty:


    ##### TO DO ######
    #fix Oval, Text and Arc

#Variables

    drawing_tool = "rectangle"

    mouse1 = "up"

    x_pos = None
    y_pos = None

    x1_point,y1_point,x2_point,y2_point = None, None, None, None

#mouse up
    def m1_but_up(self, event = None):
        self.mouse1 = "up"

        self.x_pos = None
        self.y_pos = None

        self.x2_point = event.x
        self.y2_point = event.y

        if self.drawing_tool == "line":
            self.line_draw(event)
        elif self.drawing_tool == "arc":
            self.arc_draw(event)
        elif self.drawing_tool == "oval":
            self.oval_draw(event)
        elif self.drawing_tool == "rectangle":
            self.rect_draw(event)
        elif self.drawing_tool == "text":
            self.text_draw(event)
        

#mouse down

    def m1_but_down(self, event = None):
        self.mouse1 = "down"

        self.x1_point = event.x
        self.y1_point = event.y
        
#mouse move

    def motion(self, event = None):

        if self.drawing_tool == "pencil":

            self.pencil_draw(event)           
                
#pencil draw
    def pencil_draw(self, event = None):
        if self.mouse1 == "down":


            if self.x_pos is not None and self.y_pos is not None:

                event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth = TRUE)

            self.x_pos = event.x
            self.y_pos = event.y

#line draw

    def line_draw(self, event=None):

        if None not in (self.x1_point, self.y1_point, self.x2_point, self.y2_point):
            event.widget.create_line(self.x1_point, self.y1_point, self.x2_point, self.y2_point, smooth = TRUE)


#arc draw

    def arc_draw(self, event = None):
        if None not in (self.x1_point, self.y1_point, self.x2_point, self.y2_point):
            event.widget.create_arc(self.x1_point, self.y1_point, self.x2_point, self.y2_point, smooth = TRUE)

#oval draw

    def oval_draw(self, event = None):
        if None not in (self.x1_point, self.y1_point, self.x2_point, self.y2_point):
            event.widget.create_oval(self.x1_point, self.y1_point, self.x2_point, self.y2_point, smooth = TRUE)

#Rect draw

    def rect_draw(self, event = None):
        if None not in (self.x1_point, self.y1_point, self.x2_point, self.y2_point):
            event.widget.create_rectangle(self.x1_point, self.y1_point, self.x2_point, self.y2_point)

#Text draw

#init

    def __init__(self, root):
        drawing_area = Canvas(root)

        drawing_area.pack()

        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.m1_but_down)
        drawing_area.bind("<ButtonRelease-1>", self.m1_but_up)

root = Tk() 
Painty = painty(root)
root.mainloop()

        
