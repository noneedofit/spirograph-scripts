# This python script demonstrates the use of a python library to make geometrical figures and shapes in the console/terminal.
# Spirograph is a device for creating geometrical figures and shapes by the use of a spirograph,
# Using python as a computer language that interacts with the machine and a spirograph software,
# We will be presenting some figures that were made by us.
# Presented by Dhruv - silver_angles, purple_pentagons, blue_shades 

import sys
import turtle

# ---------------------------
# Main program starts here
# ---------------------------

def blue_shades(t):
    """ Draw cicles in consecutively lighter shades of blue """
    clrs = ["MidnightBlue", "Navy", "DarkBlue", "MediumBlue", "RoyalBlue",
            "MediumSlateBlue", "CornflowerBlue", "DodgerBlue", "DeepskyBlue",
            "LightSkyBlue", "SkyBlue", "LightBlue"]

    for i in range(120):
        t.forward(5)
        t.right(3)
        c = 30
        f = 70
        for i in clrs:
            t.pencolor(i)
            t.circle(c)
            t.left(90)
            t.penup()
            t.forward(f)
            t.right(90)
            t.pendown()
            c *= 0.8
            f *= 0.8
            t.circle(c)
        t.penup()
        t.goto(0, 0)
        t.pendown()


def donut(t):
    """ Draw an orange torus-like object """
    for i in range(120):
        t.forward(3)
        t.left(3)
        t.pendown()
        t.pencolor("coral")
        t.circle(100)
        t.right(180)
        t.pencolor("peachpuff")
        t.circle(100)
        t.right(180)
        t.penup()


def hurricane(t):
    """ Draw a red hurricane """
    clrs = ["Darkred", "Firebrick", "Crimson", "IndianRed"]

    for i in range(120):
        t.forward(5)
        t.right(3)
        c = 40
        f = 70
        h = 3
        t.pencolor(clrs[i % 4])
        for i in range(14):
            t.circle(c)
            t.left(90)
            t.penup()
            t.forward(f)
            t.right(90)
            t.forward(h)
            t.pendown()
            c *= 0.8
            f *= 0.8
            h *= 1.2
            t.circle(c)
        t.penup()
        t.goto(0, 0)
        t.pendown()


def purple_pentagons(t):
    """ Draw several layers of concentric pentagons """
    h = 15
    for i in range(18):
        for j in range(5):
            t.forward(h)
            t.right(75)
        t.forward(10)
        t.right(5)
    t.penup()
    t.goto(-33, 40)
    t.pendown()
    h = 100
    t.pencolor("plum")
    for i in range(18):
        for j in range(5):
            t.forward(h)
            t.right(75)
        t.forward(10)
        t.right(5)
    t.penup()
    t.goto(-72, 88)
    t.pendown()
    h = 200
    t.pencolor("indigo")
    for i in range(18):
        for j in range(5):
            t.forward(h)
            t.right(75)
        t.forward(10)
        t.right(5)
    t.penup()
    t.goto(-143, 173)
    t.pendown()
    h = 380
    t.pencolor("blueviolet")
    for i in range(18):
        for j in range(5):
            t.forward(h)
            t.right(75)
        t.forward(10)
        t.right(5)


def silver_angles(t):
    """ Draw a spiral of silver triangles """
    clrs = ["Black", "Dimgray", "Gray", "Darkgray",
            "Silver", "Lightgrey", "Gainsboro"]
    h = 20
    a = 10
    for i in range(420):
        t.pencolor(clrs[i % len(clrs)])
        for j in range(3):
            t.forward(h)
            t.left(120)
        t.penup()
        t.forward(5)
        t.right(a)
        t.pendown()
        h *= 1.008
        a *= 0.995


def square_shell(t):
    """ Draw a spiral shell (like a snail) out of squares """
    t.pencolor("MediumAquamarine")
    h = 10
    for i in range(360):
        for j in range(4):
            t.forward(h)
            t.right(90)
        t.right(3)
        h *= 1.01


def sunflower(t):
    """ Draw a sunflower """
    clrs = ["saddlebrown", "saddlebrown", "gold", "gold",
            "darkorange", "forestgreen", "forestgreen"]
    length = 280
    a = 5

    for i in range(7):
        t.pencolor(clrs[0 - (i % len(clrs) + 1)])
        for j in range(72):
            t.left(90)
            t.forward(length)
            t.circle(15)
            t.right(180)
            t.forward(length)
            t.left(90)
            t.forward(2)
            t.right(a)
        length /= 1.5


def windmill(t):
    """ Draw a circle of windmills, moving from brown to orange """
    r = 108
    g = 45
    b = 12
    for i in range(18):
        t.pencolor((r, g, b))
        for j in range(36):
            t.forward(100)
            t.right(90)
            t.forward(30)
            t.right(100)
            t.forward(101.118742)
        t.penup()
        t.forward(45)
        t.right(20)
        t.pendown()
        r += 8
        g += 4


def print_usage():
    """ Print a usage statement for python-turtle-spirograph """
    print("Usage: python[3] " + sys.argv[0] + " [-a] " + "<drawing>")
    print("    -a      : animate the drawing (default: no animation)")
    print("    drawing : one of")
    print("        blue_shades")
    print("        donut")
    print("        hurricane")
    print("        purple_pentagons")
    print("        silver_angles")
    print("        square_shell")
    print("        sunflower")
    print("        windmill")
    sys.exit()


if __name__ == "__main__":
    if (len(sys.argv) < 2 or
            (sys.argv[1] == '-a' and len(sys.argv) < 3) or
            (len(sys.argv) > 3)):
        print_usage()

    PAD = turtle.Screen()
    PAD.colormode(255)
    PEN = turtle.Turtle()
    PEN.speed(0)
    PEN.hideturtle()

    if sys.argv[1] == '-a':
        DRAW = sys.argv[2]
    else:
        PAD.tracer(0)
        DRAW = sys.argv[1]

    locals()[DRAW](PEN)

    PAD.update()
    PAD.exitonclick()