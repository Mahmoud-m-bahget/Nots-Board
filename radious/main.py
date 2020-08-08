from circle import circle
from rectangle import rectangle
from cylinder import cylinder

while True :
    shape = input('enter the shape from [circels ,rectaqngle,cylinder]\n')

    if shape == 'circle':
        c = circle()
        c.printcharateristic()

    elif shape == 'rectangle':
        r = rectangle()
        r.printcharateristic()

    elif shape == 'cylinder':
        s = cylinder()
        s.printcharateristic()
