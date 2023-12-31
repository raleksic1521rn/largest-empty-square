import time
import bisect
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from helper import MergeSortTree

max_iterations = 32
liml = -100.0 
limr = 200.0

def draw_square(x, y, r):
    square = Rectangle((x - r/2, y - r/2), r, r, fill=False, edgecolor='black')
    plt.gca().add_patch(square)
    plt.draw()
    return square

def draw_point(point):
    plt.scatter(point[0], point[1], color='black', s=10) 
    plt.draw()

def main():
    points = []
    fpath = input("Enter file path or leave empty for randomized input: ")
    if (fpath):
        with open(fpath, 'r') as file:
            for line in file:
                x, y = map(float, line.strip().split())
                points.append((x, y))
        points = sorted(points)
    else:
        points = sorted([(np.random.uniform(liml * 0.75, limr * 0.75), np.random.uniform(liml * 0.66, limr * 0.66)) for _ in range(100)])

    plt.ion()  
    plt.figure()
    plt.axis('equal') 
    plt.xlim(liml, limr)  
    plt.ylim(liml, limr)  
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Largest Empty Square')
    plt.get_current_fig_manager().window.title('Largest Empty Square')

    x_array = list(map(lambda point: point[0], points))
    y_array = list(map(lambda point: point[1], points))
    seg_tree = MergeSortTree(y_array)
    counter = 1

    for point in points:
        draw_point(point)

    while True:
        x_query = input("Enter x-coordinate for the query point (or type 'exit' to quit): ")
        if x_query == 'exit':
            break
        x_query = float(x_query)
        y_query = float(input("Enter y-coordinate for the query point: "))
        plt.scatter(x_query, y_query, color='black', s=1) 
        plt.text(x_query + 0.25, y_query + 0.25, 'q{}'.format(counter), fontsize=10, color='black')
        plt.draw()
        plt.pause(0.1)
        square = None
        l = 0.0 
        r = limr - liml
        res = l
        for _ in range(max_iterations):
            d = (l + r) / 2
            l_query = bisect.bisect_right(x_array, x_query - d / 2)
            r_query = bisect.bisect_left(x_array, x_query + d / 2) - 1
            print("Trying {}".format(d), end = " ")
            if (l_query > r_query):
                print("Valid")
                if (not square == None):
                    square.remove()
                    plt.draw()
                square = draw_square(x_query, y_query, d)
                plt.pause(0.5)
                res = max(res, d)
                l = d
            else:
                query = seg_tree.query(l_query, r_query, y_query - d / 2, y_query + d / 2)
                if (query == 0):
                    print("Valid")
                    if (not square == None):
                        square.remove()
                        plt.draw()
                    square = draw_square(x_query, y_query, d)
                    plt.pause(0.5)
                    res = max(res, d)
                    l = d
                else:
                    print("Invalid")
                    r = d
            time.sleep(0.5)
        counter = counter + 1
        square = draw_square(x_query, y_query, res)
        plt.pause(0.5)
        print("Largest empty square at ({}, {}) side length = {}".format(x_query, y_query, res))

    plt.ioff() 

if __name__ == "__main__":
    main()