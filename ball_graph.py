# ball_graph.py
from matplotlib import pyplot as plt
import math

'''
  simulating ball movement 
  given time, using ...
  projectile motion formula
'''

def frange(start, final, increment):
    '''
    generating equally spaced
    floating numbers given *start* to *final*
    with a steps by given *increment* values
    '''
    numbers = []
    while start < final:
        numbers.append(start)
        start += increment
    return numbers

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x cordinate')
    plt.ylabel('y cordinate')
    plt.title('Projectile motion simulation')

def draw_trajectory(u, theta):
    '''
    calculating trajectory of a ball given
    starting velocity *u* with a angle of *theta*
    '''
    theta = math.radians(theta)
    g = 9.8

    # Time of flight
    t_flight = 2*u*math.sin(theta)/g
    # Find the time interval
    intervals = frange(0, t_flight, 0.001)
    # List of x and y cordinates
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)

    draw_graph(x, y)

if __name__ == '__main__':
    try:
        k = []
        ball_number = int(input('Enter The Number of Object eg. 3: '))
        for i in range(ball_number):
            u = float(input('Enter the initial velocity (m/s) eg. 25 : '))
            theta = float(input('Enter the angle of projection (degrees): eg. 60: '))
            k.append( (u, theta) )

    except ValueError as err:
        print('You enter an invaild input')
    else:
        for i in k:
            draw_trajectory(*i)
        plt.show()
