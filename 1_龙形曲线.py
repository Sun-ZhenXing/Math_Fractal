import turtle as t

def dragon(level=4, size=200, zig=t.right, zag=t.left):
    if level <= 0:
        t.forward(size)
        return

    size /= 1.285
    zig(45)
    dragon(level-1, size, t.right, t.left)
    zag(90)
    dragon(level-1, size, t.left, t.right)
    zig(45)

t.speed(0.001)
t.hideturtle()
dragon(12)
t.exitonclick()
