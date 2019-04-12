import sys
sys.path.append('..')

import numpy as np
from graff.Endpoint import Endpoint
from graff.Variable import Variable
from graff.Factor import Factor
from graff.Distribution.Normal import Normal
from graff.Distribution.SampleWeights import SampleWeights
from graff.Distribution.BallTreeDensity import BallTreeDensity

from graff.Core import MultiplyDistributions


if __name__ == '__main__':
    """

    """
    e.Connect('tcp://127.0.0.1:5555')
    print(e.Status())

    # Add the first pose x0
    x0 = Variable('x0', 'Pose2')
    e.AddVariable(x0)

    # Add at a fixed location PriorPose2 to pin x0 to a starting location
    prior = Factor('PriorPose2', ['x0'], Normal(np.zeros(3,3), 0.01*np.eye(3)) )
    e.AddFactor(prior)

    for i in range(1,5):
        lpx = 'x'+str(i-1)
        lx = 'x'+str(i)
        x = Variable(lx, 'Pose2')
        e.AddVariable(x)

        z =  Normal (np.array([10.0;0;np.pi/3]), 0.1*np.eye(3))
        odometry = Factor('Pose2Pose2', [lpx, lx],z )
        addFactor(odometry)

    e.RequestSolve()

    # TODO: get data back

    e.Disconnect()
