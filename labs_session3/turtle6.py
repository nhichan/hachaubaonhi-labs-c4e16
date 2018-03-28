from turtle import*

def draw_star(a,b,leng):

    penup()
    setx(a)
    sety(b)
    pendown()
    left(34)
    for i in range(5):
        forward(leng)
        left(144)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

mainloop()
