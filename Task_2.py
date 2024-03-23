import turtle

# Рекурсивна функція для дерева Піфагора
def pifagorian_tree(t, deepth, size, angle):
    if deepth == 0:
        t.backward(size/0.8)
    else:
        t.right(angle)
        t.forward(size)
        pifagorian_tree(t, deepth - 1, size*0.8, angle)
        t.left(angle*2)
        t.forward(size)
        pifagorian_tree(t, deepth - 1, size*0.8, angle)
        t.right(angle)
        t.backward(size/0.8)

def draw_pifagorian_tree(depth):
    window = turtle.Screen()
    window.bgcolor("white")
    size = 128
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -200)
    t.left(90)
    t.pendown()
    pifagorian_tree(t, depth, size, 45)
    window.mainloop()

# Ввід глубини дерева
def main():
    user_input = input('Введіть глибину дерева: ')
    try:
        depth = int(user_input)
        if depth > 0:
            draw_pifagorian_tree(depth)
        else:
            print('Введіть додатне ціле число.')
    except ValueError:
        print('Введіть коректне ціле число.')

if __name__ == "__main__":
    main()
