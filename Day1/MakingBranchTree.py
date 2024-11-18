import turtle


def draw_fractal_tree(branch_len, angle):
    if branch_len < 3:
        return
    else:
        turtle.forward(branch_len)
        turtle.left(angle)
        draw_fractal_tree(branch_len - 15, angle)
        turtle.right(angle * 2)
        draw_fractal_tree(branch_len - 15, angle)
        turtle.left(angle)
        turtle.backward(branch_len)


turtle.speed(0)
turtle.left(90)
turtle.up()
turtle.backward(200)
turtle.down()
turtle.color('red')
draw_fractal_tree(100 , 30)
turtle.done

