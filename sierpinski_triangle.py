#########################################
## Copyright(C) 2024, Charles T.       ##
#########################################

################################################################################

""" Sierpinski Triangle """

################################################################################

import  argparse
import  sys

from    turtle import Turtle

################################################################################

triangle = []

################################################################################

def draw(turtle):
    """ draw function """
    i = 0

    while i < len(triangle):
        first_point = triangle[i]
        turtle.up()
        turtle.goto(first_point)
        turtle.down()
        turtle.goto(triangle[i + 1])
        turtle.goto(triangle[i + 2])
        turtle.goto(first_point)
        i += 3

################################################################################

def build(p_a, p_b, p_c, iterations):
    """build function"""
    if iterations > 0:
        new_points = [ ((p_a[0] + p_b[0]) / 2, (p_a[1] + p_b[1]) / 2),
                       ((p_a[0] + p_c[0]) / 2, (p_a[1] + p_c[1]) / 2),
                       ((p_b[0] + p_c[0]) / 2, (p_b[1] + p_c[1]) / 2) ]

        for i in range(0, 3):
            triangle.append(new_points[i])

        build(p_a, new_points[0], new_points[1], iterations - 1)
        build(new_points[0], p_b, new_points[2], iterations - 1)
        build(new_points[1], new_points[2], p_c, iterations - 1)

################################################################################

def check_args():
    """ check_args function """
    parser = argparse.ArgumentParser()

    parser.add_argument("ITERATIONS", help = "values in {0... 7}.", type = int)
    parser.add_argument("DELAY",  help = "values in {0, 10}.", type = int)

    args = parser.parse_args()

    try:
        if args.ITERATIONS not in range(0, 8):
            raise argparse.ArgumentTypeError(f"ITERATIONS : {args.ITERATIONS} is an invalid value.")
        if args.DELAY not in range(0, 11):
            raise argparse.ArgumentTypeError(f"DELAY : {args.DELAY} is an invalid value.")
    except argparse.ArgumentTypeError as e:
        print(f"Argument Error - {e}\n")
        parser.print_help()
        sys.exit(-1)

################################################################################

def main():
    """ main function """
    check_args()

    iterations  = int(sys.argv[1])
    delay       = int(sys.argv[2])

    turtle  = Turtle()
    ws      = turtle.getscreen()

    ws.title("Sierpinski Triangle")
    ws.setup(1000, 1000)
    ws.bgcolor("#212F3C")

    turtle.speed(delay)
    turtle.ht()
    turtle.pensize(width = 2)
    turtle.pencolor("#FFFFFF")

    p_a = [-400, -350]
    p_b = [400, -350]
    p_c = [0, 400]

    triangle.append(p_a)
    triangle.append(p_b)
    triangle.append(p_c)

    build(p_a, p_b, p_c, iterations)
    draw(turtle)

    ws.exitonclick()

################################################################################

if __name__ == "__main__":
    main()

################################################################################
