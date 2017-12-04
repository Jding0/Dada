import unittest

import sys
sys.path.append('./src/')

from evaluation import mean_accuracy
from network import line_network
from optimization import centralized_FW
from utils import load_iris_dataset


class TestCentralized(unittest.TestCase):

    def test_iris(self):
        X, Y = load_iris_dataset()
        N = X.shape[1]

        # set graph
        nodes = line_network(X, Y, nb_nodes=1)
        self.assertEqual(nodes[0].sample.shape[1], 5)

        centralized_FW(nodes, N, nb_iter=10, callbacks={})
        self.assertEqual(nodes[0].clf.shape, (1, 5))

        acc = mean_accuracy(nodes)
        self.assertGreaterEqual(acc[0], 0.95)


if __name__ == '__main__':
    unittest.main()