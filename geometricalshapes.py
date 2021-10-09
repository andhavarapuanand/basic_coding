a = True
while(a):
    print("Choose from the following shapes of which you want area")
    print("1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Cube")
    n = int(input())
    pi = 22/7
    if n == 1:
        print("Enter the base and height of triangle")
        x, y = map(int, input().split())
        area = 0.5 * x * y
        print("Area of triangle is {0}".format(area))
    elif n == 2:
        print("Enter the length and breadth of Rectangle")
        x, y = map(int, input().split())
        area = x * y
        print("Area of rectangle is {0}".format(area))
    elif n == 3:
        print("Enter the side of square")
        s = int(input())
        area = s * s
        print("Area of square is {0}".format(area))
    elif n == 4:
        print("Enter the radius of circle")
        r = int(input())
        area = pi * (r**2)
        print("Area of circle is {0}".format(area))
    elif n == 5:
        print("Enter the edge of cube")
        e = int(input())
        area = 6 * (e**2)
        print("Surface Area of cube is {0}".format(area))
    print("Do you want to run the program again Y/N")
    b = input()
    f = b.lower()
    if f == "no" or f == "n":
        print("The program has ended")
        a = False
    else:
        a = True
