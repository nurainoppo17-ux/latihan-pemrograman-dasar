import turtle
import random
import time

# Membuat layar
layar = turtle.Screen()
layar.bgcolor("black")
layar.title("Bintang Bercahaya")
layar.setup(width=800, height=600)

# Membuat turtle
bintang = turtle.Turtle()
bintang.hideturtle()
bintang.speed(0)

# Fungsi menggambar bintang
def gambar_bintang(x, y, ukuran, warna):
    bintang.penup()
    bintang.goto(x, y)
    bintang.setheading(90)
    bintang.pendown()

    bintang.color(warna)
    bintang.begin_fill()

    for i in range(5):
        bintang.forward(ukuran)
        bintang.right(144)

    bintang.end_fill()


# Membuat banyak bintang kecil di langit
for i in range(30):
    x = random.randint(-380, 380)
    y = random.randint(-250, 250)

    ukuran = random.randint(2, 6)

    gambar_bintang(x, y, ukuran, "white")


# Bintang utama
gambar_bintang(0, 50, 120, "yellow")

# Efek cahaya di sekitar bintang
cahaya = turtle.Turtle()
cahaya.hideturtle()
cahaya.speed(0)

for ukuran in range(180, 120, -5):
    cahaya.penup()
    cahaya.goto(0, 50 - ukuran / 2)
    cahaya.setheading(90)
    cahaya.pendown()

    # Warna cahaya dibuat semakin terang
    cahaya.color(
        1,
        1,
        random.uniform(0.1, 0.8)
    )

    for i in range(5):
        cahaya.forward(ukuran)
        cahaya.right(144)


# Animasi cahaya berkedip
for i in range(10):
    bintang.clear()

    # Bintang utama
    gambar_bintang(
        0,
        50,
        random.randint(100, 130),
        "yellow"
    )

    # Efek sinar
    cahaya.clear()

    cahaya.penup()
    cahaya.goto(0, 50)
    cahaya.pendown()

    cahaya.color("orange")
    cahaya.pensize(random.randint(2, 8))

    # Sinar horizontal
    cahaya.goto(-180, 50)
    cahaya.goto(180, 50)

    # Sinar vertikal
    cahaya.penup()
    cahaya.goto(0, -130)
    cahaya.pendown()
    cahaya.goto(0, 230)

    layar.update()
    time.sleep(0.3)


turtle.done()
