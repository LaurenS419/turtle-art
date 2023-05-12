# Lauren Spee
# 261008497

def my_artwork():
    """() -> NoneType
    Draws a picture of a sailboat 
    """
    
    ### Imports/Initial Settings ###
    
    import math
    import turtle
    mark = turtle.Turtle() #the turtle's name is mark
                           #the name makes sense because it marks the window
    mark.speed(10)
    
    ### Sail Function ###
    
    def sail(width, height):
        """(float, float) -> NoneType
        Draws a right-angle triangle with width as the base length
        and height as the height length
        """
        width = abs(width)
        height = abs(height)
        
        mark.penup()
        mark.goto(-50,300)
        mark.pensize(2)
        mark.color("red")
        mark.pendown()
    
        mark.left(math.degrees(math.atan(width/height)))
        
        mark.begin_fill()
        
        mark.forward(math.sqrt(width**2 + height**2))
        mark.right(90+(90-math.degrees(math.atan(height/width))))
        
        mark.forward(width)
        
        mark.right(90)
        mark.forward(height)
        
        mark.end_fill()
        
        #Setup for initial while height is a variable
        mark.penup()
        mark.goto(-30,340-height)
        mark.pensize(3)
        mark.color("gainsboro")
        mark.pendown()
    
    ### Boat ###
    
    mark.penup()
    mark.right(180)
    mark.goto(200,0)
    
    mark.pensize(3)
    mark.color("dim gray")
    mark.begin_fill()
    
    mark.pendown()
    mark.forward(400)
    
    mark.left(120)
    mark.forward(125)
    mark.left(60)
    mark.forward(275)
    mark.left(60)
    mark.forward(125)
    mark.left(120)
    
    mark.end_fill()
    
    ### Mast ###
    
    mark.penup()
    mark.goto(-75,0)
    mark.pensize(2)
    
    mark.pendown()
    mark.right(90)
    mark.forward(300)
    mark.right(90)
    mark.forward(25)
    mark.right(90)
    mark.forward(300)
    
    ### Sail ###
    
    #height = 200.0
    #width = 200.0
    
    sail(200.0, 200.0)
    
    ## First initial (L) ###
    
    mark.backward(15)
    mark.right(90)
    mark.forward(15)
    
    ### Waves ###
    
    mark.penup()
    mark.goto(-355,-50)
    mark.pensize(4)
    mark.color("deep sky blue")
    mark.pendown()
    mark.right(90)
    
    for i in range(14):
        mark.circle(25,180)
        mark.left(180)
       
    
    