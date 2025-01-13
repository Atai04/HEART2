import math
import turtle
import random



# Kalp koordinat fonksiyonları
def xt(t):
    return 16 * math.sin(t) ** 3

def yt(t):
    return 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

# Ayarlar
t = turtle.Turtle()
t.speed(1400)  # Maksimum hız
turtle.colormode(255)
screen = turtle.Screen()
screen.bgcolor(0, 0, 0)  # Arka plan siyah
screen.tracer(0)  # Daha hızlı çizim için tracer kapalı

# Çizim parametreleri
steps = 1200 # Çizim için toplam adım sayısı
angles = [i * (2 * math.pi / steps) for i in range(steps)]  # Açı listesi
random.shuffle(angles)  # Açıları rastgele sıralayın

# Çizim
for i, angle in enumerate(angles):
    t.penup()
    t.goto(xt(angle) * 20, yt(angle) * 20)  # Rastgele bir nokta
    t.pendown()
    t.pencolor(255, 0, 0)  # Kırmızı renk
    t.goto(0, 0)  # Kalp merkezine çizgi
    screen.update()

# Çizimi tamamla
t.hideturtle()
turtle.mainloop()
 