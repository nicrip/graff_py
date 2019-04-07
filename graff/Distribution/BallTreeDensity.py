import numpy as np

class BallTreeDensity(object):
    """
    """
    def __init__(self, kernel, bandwidth, weights, points):
        """
        dim::Int  # point dimension
        kernelType::String
        bandwidth::Vector{Float64}
        weights::Vector{Float64}
        points::Vector{Float64} # Stack points as a 1D vector.

        Note: current implementation only supports one-dimensional points!
        """

        # assert types
        assert (isinstance(bandwidth, np.ndarray))
        assert (isinstance(weights, np.ndarray))
        assert (isinstance(points, np.ndarray))

        # assert shape
        # assert (samples.shape[0] == weights.shape[0])
        assert (len(bandwidth.shape)==1)
        assert (len(weights.shape)==1)
        assert (len(weights.shape)==1)

        # we're good!
        self.kernel = kernel
        self.bandwidth = bandwidth
        self.weights = weights
        self.points = points

    def dict(self):
        """
        """
        d = {}
        d['distType'] = 'BallTreeDensity'
        d['dim'] = 1
        d['kernelType'] = self.kernel
        d['bandwidth'] = self.bandwidth.tolist()
        d['weights'] = self.weights.tolist()
        d['points'] = self.points.tolist()

        return(d)




