import random

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def generate_graph(name):
    xx = np.arange(1,14)
    yy = np.arange(1,14)
    np.random.shuffle(yy)
    plt.plot(xx, yy)
    plt.xlabel('Days')
    plt.ylabel('Time Spent online')
    strFile = './static/' + name + '.png'
    plt.savefig(strFile)
    plt.clf()
    # could return instead

def generate_scatter(name):
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = (30 * np.random.rand(N)) ** 2  # 0 to 15 point radii

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    strFile = './static/' + name + '_scatter.png'
    plt.xlabel('Time of Day')
    plt.ylabel('School Attendance')
    plt.savefig(strFile)
    plt.clf()
    # could return instead

def chatheads():
    chatheads = [
        {
            'name': 'Adam',
            'student': "Adrian",
            'description': 'Adrian is the child of Adam',
            'last_update': random.randint(1, 40),
            'recent_graph': generate_graph('Adrian'),
            'scatter': generate_scatter('Adrian')
        },
        {
            'name': 'Bob',
            'student': "Barry",
            'description': 'Barry is the child of Bob',
            'last_update': random.randint(1, 40),
            'recent_graph': generate_graph('Barry'),
            'scatter': generate_scatter('Barry')


        },
        {
            'name': 'Carol',
            'student': "Carl",
            'description': 'Carl is the child of Carol',
            'last_update': random.randint(1, 40),
            'recent_graph': generate_graph('Carl'),
            'scatter': generate_scatter('Carl')
        }
    ]
    return chatheads