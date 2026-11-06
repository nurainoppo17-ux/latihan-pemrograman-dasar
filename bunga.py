import turtle

# Membuat layar
layar = turtle.Screen()
layar.bgcolor("lightblue")
layar.title("Gambar Bunga")

# Membuat objek turtle
bunga = turtle.Turtle()
bunga.speed(0)

# Menggambar kelopak bunga
bunga.color("red")

for i in range(36):
    bunga.circle(100)
    bunga.left(10)

# Menggambar bagian tengah bunga
bunga.penup()
bunga.goto(0, -20)
bunga.pendown()

bunga.color("yellow")
bunga.begin_fill()
bunga.circle(20)
bunga.end_fill()

# Menggambar batang
bunga.penup()
bunga.goto(0, -20)
bunga.setheading(270)
bunga.pendown()

bunga.color("green")
bunga.pensize(10)
bunga.forward(200)

# Menampilkan jendela
turtle.done()
