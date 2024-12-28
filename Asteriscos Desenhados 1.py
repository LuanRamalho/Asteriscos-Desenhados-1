import turtle
import random

def draw_asterisk(t, x, y, size, color):
    """Desenha um asterisco na posição (x, y) com o tamanho e a cor especificados."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(8):
        t.forward(size)
        t.backward(size)
        t.right(45)

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Asteriscos Aleatórios")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    num_asterisks = random.randint(10, 50)  # Quantidade aleatória de asteriscos

    for _ in range(num_asterisks):
        x = random.randint(-300, 300)  # Posição x aleatória
        y = random.randint(-300, 300)  # Posição y aleatória
        size = random.randint(10, 50)  # Tamanho aleatório do asterisco
        color = random.choice(["red", "blue", "green", "yellow", "purple", "orange", "white"])
        draw_asterisk(t, x, y, size, color)

    screen.mainloop()

if __name__ == "__main__":
    main()
