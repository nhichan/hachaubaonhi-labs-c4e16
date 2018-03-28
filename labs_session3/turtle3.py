from turtle import*

def draw_square(length,colour):

    color(colour)
    for i in range(4):
        forward(length)
        left(90)

co = str(input('write down a color: '))
le = int(input('write down the length: '))

draw_square(le,co)


mainloop()
