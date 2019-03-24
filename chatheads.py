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
    plt.savefig('templates/'+ name + '.png')
    plt.clf()


def chatheads():
    chatheads = [
        {
            'name': 'Adam',
            'student': "Adrian",
            'description': 'Adrian is the child of Adam',
            'last_update': random.randint(1, 40),
            'recent_graph': generate_graph('Adrian')
        },
        {
            'name': 'Bob',
            'student': "Barry",
            'description': 'Barry is the child of Bob',
            'last_update': random.randint(1, 40),
            'recent_graph': generate_graph('Barry')


        },
        {
            'name': 'Carol',
            'student': "Corrin",
            'description': 'Corrin is the child of Carol',
            'last_update': random.randint(1, 40),
            'recent_graph': generate_graph('Corrin')
        }
    ]
    return chatheads