import numpy as np

class SampleWeights(object):
    """
    """

    def __init__(self, samples, weights):
        """
        """

        # assert types
        assert (isinstance(samples, np.ndarray))
        assert (isinstance(weights, np.ndarray))

        # assert shape
        assert (samples.shape[0] == weights.shape[0])
        assert (len(samples.shape)==1)
        assert (len(weights.shape)==1)

        # we're good!
        self.samples = samples
        self.weights = weights

    def dict(self):
        """
        """
        d = {}
        d['distType'] = 'SampleWeights'
        d['samples'] = self.samples.tolist()
        d['weights'] = self.weights.tolist()

        return(d)
