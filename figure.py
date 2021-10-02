# draws curves
import turtle as tt

tt.bgcolor('black') #bg
tt.pensize(2)       #pen
tt.speed(10)        #speed
  
# iterate 'n' times 
for i in range(6):
    
      # color combination
    for color in ('red', 'magenta', 'blue', 
                  'cyan', 'green', 'white',
                  'yellow'):
        tt.color(color)
          
        # circle size
        tt.circle(100)
          
        # new circle direction
        tt.left(10)
      
    # hie cursor
    tt.hideturtle()