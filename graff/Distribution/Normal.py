import numpy as np

class Normal(object):
    """
    """

    def __init__(self, mean, cov):
        """
        """
        # assert types
        assert (isinstance(mean, np.ndarray))
        assert (isinstance(cov, np.ndarray))

        # assert shape
        assert (len(mean) == cov.shape[0])
        assert (len(mean) == cov.shape[1])

        # we're good!
        self.mean = mean
        self.cov = cov

    def dict(self):
        d = {}
        if 1==len(self.mean):
            d['distType'] = 'Normal'
        else:
            d['distType'] = 'MvNormal'

        d['mean'] = self.mean
        d['cov'] = self.cov

        return(d)
