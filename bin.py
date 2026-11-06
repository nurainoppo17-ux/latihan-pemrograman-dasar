import turtle
import time

# Layar
layar = turtle.Screen()
layar.bgcolor("black")
layar.title("Bintang Bercahaya")

# Bintang
bintang = turtle.Turtle()
bintang.speed(0)

# Menggambar bintang
def buat_bintang(ukuran, warna):
    bintang.color(warna)
    bintang.begin_fill()

    for i in range(5):
        bintang.forward(ukuran)
        bintang.right(144)

    bintang.end_fill()


# Posisi bintang
bintang.penup()
bintang.goto(-60, -50)
bintang.pendown()

# Efek berkedip
for i in range(8):
    bintang.clear()

    if i % 2 == 0:
        buat_bintang(120, "yellow")
    else:
        buat_bintang(130, "orange")

    time.sleep(0.3)

turtle.done()
