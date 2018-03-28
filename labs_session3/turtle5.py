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

x = int(input('nhap toa do x: '))
y = int(input('nhap toa do y: '))
length = int(input('nhap do dai canh ngoi sao: '))

draw_star(x,y,length)

mainloop()
