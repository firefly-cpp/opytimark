import numpy as np
from opytimark.core import Benchmark


class Sphere(Benchmark):
    """
    """

    def __init__(self):
        """
        """

        # Override its parent class
        super(Sphere, self).__init__(name='Sphere', dims='-1', continuous=True,
                                     convex=True, differentiable=True, multimodal=False, separable=True)

    def __call__(self, x):
        """
        """

        #
        y = x ** 2

        return np.sum(y)
