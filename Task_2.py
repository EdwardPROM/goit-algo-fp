import turtle

def pifagorian_tree(branch_length, t, angle, depth):
    if depth == 0:
        return
    else:
        t.forward(branch_length)
        t.right(angle)
        pifagorian_tree(0.8 * branch_length, t, angle, depth - 1)
        t.left(2 * angle)
        pifagorian_tree(0.8 * branch_length, t, angle, depth - 1)
        t.right(angle)
        t.backward(branch_length)

def draw_pifagorian_tree():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.color("green")
    t.width(2)

    depth = int(turtle.textinput("Введіть глибину дерева:", "Глибина"))

    t.left(90)
    pifagorian_tree(100, t, 45, depth)

    turtle.done()

draw_pifagorian_tree()
