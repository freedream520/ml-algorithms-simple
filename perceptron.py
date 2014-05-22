#-*- coding: utf-8 -*-

import numpy as np
from pylab import rand
from itertools import repeat


class Perceptron(object):
    """
    Perceptron Class
    """

    def __init__(self, inputs, targets, T=6, eta=0.1):
        """
        T: number of iterations
        eta: learning rate
        N: number of training data
        m: number of inputs(exclude bias node)
        n: number of neurons
        w: m x n array
        inputs: N x m array
        targets: N x n array
        """
        self._T = T
        self._eta = eta
        self._N = inputs.shape[0]
        self._m = inputs.shape[1]
        self._n = targets.shape[1]
        self._w = np.random.rand(self._m+1, self._n) * 0.1 - 0.05

        bias = - np.ones((self._N, 1))
        self._inputs = np.concatenate((bias, inputs), axis=1)
        self._targets = targets
        self._outputs = np.zeros((self._N, self._n))

        print 'Num of training data: %d' % self._N
        print 'Num of input dim.: %d' % self._m
        print 'Num of output dim.: %d' % self._n

    def fit(self):
        """
        a training phase
        """
        for t in xrange(self._T):
            self._outputs = self.predict(self._inputs)
            self._w += self._eta * np.dot(self._inputs.T, self._targets - self._outputs)
        print '--- training phase ---'
        print 'weights:'
        print self._w

    def predict(self, x):
        """
        activataion function

        x: N x m array
        w: m x n array
        """
        y = np.dot(x, self._w)
        return np.where(y > 0, 1, 0)


def gen_data(n):
    xb = (rand(n)*2-1)/2-0.5
    yb = (rand(n)*2-1)/2+0.5
    inputs = [[xb[i], yb[i]] for i in xrange(len(xb))]
    targets = [[i] for i in repeat(1, len(xb))]

    xr = (rand(n)*2-1)/2+0.5
    yr = (rand(n)*2-1)/2-0.5
    inputs = inputs + [[xr[i], yr[i]] for i in xrange(len(xr))]
    targets = targets + [[i] for i in repeat(-1, len(xr))]

    return np.array(inputs), np.array(targets)


def main():
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    targets = np.array([[0], [1], [1], [1]])

    p = Perceptron(inputs, targets)
    p.fit()

    print '--- predict phase ---'
    inputs_bias = np.concatenate((-np.ones((inputs.shape[0], 1)), inputs), axis=1)
    print p.predict(inputs_bias)

    print '\n'
    inputs2, targets2 = gen_data(10)
    p2 = Perceptron(inputs2, targets2)
    p2.fit()

    print '\n--- predict phase ---'
    inputs_bias2 = np.concatenate((-np.ones((inputs2.shape[0], 1)), inputs2), axis=1)
    print p2.predict(inputs_bias2)

if __name__ == '__main__':
    main()
