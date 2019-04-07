
import numpy as np
from graff.Endpoint import Endpoint
from graff.Distribution.Normal import Normal
from graff.Distribution.SampleWeights import SampleWeights
from graff.Distribution.BallTreeDensity import BallTreeDensity

from graff.Core import MultiplyDistributions

if __name__ == '__main__':
    e = Endpoint()

    e.Connect('tcp://192.168.0.102:5555')

    print(e.Status())

    # a = SampleWeights(np.ones(10),np.ones(10))
    # b = SampleWeights(np.ones(10),np.ones(10))
    b1 = BallTreeDensity('Gaussian', np.zeros(10), np.ones(10), np.random.randn(10))
    b2 = BallTreeDensity('Gaussian', np.zeros(10), np.ones(10), np.random.randn(10))

    MultiplyDistributions(e, [b1,b2])

    e.Disconnect()

    g = Normal(np.zeros(10), np.eye(10,10))
    print(g.dict())
