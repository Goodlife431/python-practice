import math

if __name__=='__main__':
    radius_str = input('enter the radius of your circle: ')
    radius_int = int(radius_str)

    circumference = 2 * math.pi * radius_int
    area = math.pi * math.pow(radius_int, 2)

    print('circumference of the circle is: ', circumference, '\n' 'area of the circle is:', area)


