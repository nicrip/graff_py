
import numpy as np
from graff.Endpoint import Endpoint
from graff.Distribution.Normal import Normal
from graff.Distribution.SampleWeights import SampleWeights
from graff.Distribution.BallTreeDensity import BallTreeDensity

from graff.Core import MultiplyDistributions

import matplotlib.pyplot as plt

if __name__ == '__main__':
    e = Endpoint()

    e.Connect('tcp://192.168.0.102:5555')
    print(e.Status())

    N = 1000
    u1 = 0.0
    s1 = 10.0
    x1 = u1+s1*np.random.randn(N)

    u2 = 50.0
    s2 = 10.0
    x2 = u2+s2*np.random.randn(N)
    b1 = BallTreeDensity('Gaussian', np.ones(N), np.ones(N), x1)
    b2 = BallTreeDensity('Gaussian', np.ones(N), np.ones(N), x2)

    rep = MultiplyDistributions(e, [b1,b2])
    print(rep)
    x = np.array(rep['points'] )
    # plt.stem(x, np.ones(len(x)) )
    plt.hist(x, bins = int(len(x)/10.0), color= 'm')
    plt.hist(x1, bins = int(len(x)/10.0),color='r')
    plt.hist(x2, bins = int(len(x)/10.0),color='b')
    plt.show()

    e.Disconnect()
