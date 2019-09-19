import matplotlib.pyplot as plt
import numpy as np
import random
import math



def one():
    x = range(1, 10)
    y = [(n ** 2) - n + 2 for n in x]
    plt.plot(x, y)
    plt.show()


def four_list_one():
    x = range(1, 6)
    print(x)
    y = [math.sqrt(n) for n in x]
    return x, y
    plt.plot(x, y)
    plt.show()

def four_list_two():
    x = range(1, 6)
    y = [n ** 3 for n in x]
    return x, y
    plt.plot(x, y)
    plt.show()

def four_list_three():
    x = range(1, 6)
    y = [math.tan(n) for n in x]
    return x, y
    plt.plot(x, y)
    plt.show()

def four_list_four():
    x = range(1, 6)
    y = [2 ** n for n in x]
    return x, y
    plt.plot(x, y)
    plt.show()


def the_four_charts():
    x1, y1 = four_list_one()
    x2, y2 = four_list_two()
    x3, y3 = four_list_three()
    x4, y4 = four_list_four()
    fig, axis = plt.subplots(2, 2)
    axis[0, 0].plot(x1, y1)
    axis[0, 0].set_title('First Equation')
    axis[0, 1].plot(x2, y2, 'tab:blue')
    axis[0, 1].set_title('Second Equation')
    axis[1, 0].plot(x3, y3, 'tab:green')
    axis[1, 0].set_title('Third Equation')
    axis[1, 1].plot(x4,y4, 'tab:cyan')
    axis[1, 1].set_title('Fourth Equation')
    for ax in axis.flat:
        ax.set(xlabel='x-label', ylabel='y-label')
    for ax in axis.flat:
        ax.label_outer()
    plt.show()

    
def the_four_lines():
    x1, y1 = four_list_one()
    x2, y2 = four_list_two()
    x3, y3 = four_list_three()
    x4, y4 = four_list_four()
    plt.plot( x1, y1, marker='', markerfacecolor='blue', markersize=12, color='blue', linewidth=2, label = 'one')
    plt.plot( x2, y2, marker='', color='red', linewidth=2, label = 'two')
    plt.plot( x3, y3, marker='', color='green', linewidth=2, label = 'three')
    plt.plot(x4, x4, marker = '', color = 'brown', linewidth = 2, label = 'four')
    plt.legend()
    plt.show()