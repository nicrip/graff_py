
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

    N = 100
    u1 = 0.0
    s1 = 3.0

    u2 = 50.0
    s2 = 3.0
    b1 = BallTreeDensity('Gaussian', np.ones(N), np.ones(N), u1+s1*np.random.randn(N))
    b2 = BallTreeDensity('Gaussian', np.ones(N), np.ones(N), u2+s2*np.random.randn(N))

    rep = MultiplyDistributions(e, [b1,b2])
    print(rep)
    x = np.array(rep['points'] )
    # plt.stem(x, np.ones(len(x)) )
    plt.hist(x, bins = int(len(x)/10.0))
    plt.show()

    e.Disconnect()
