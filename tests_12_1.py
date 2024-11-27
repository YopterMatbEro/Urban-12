from module_12_1 import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = Runner('Zombie')

        for _ in range(10):
            walker.walk()

        self.assertEqual(walker.distance, 50)

    def test_run(self):
        forest = Runner('Forest')

        for _ in range(10):
            forest.run()

        self.assertEqual(forest.distance, 100)

    def test_challenge(self):
        bolt = Runner('Usain Bolt')
        gepard = Runner('Just_gepard')

        for _ in range(10):
            bolt.walk()
            gepard.run()

        self.assertNotEqual(bolt.distance, gepard.distance)


if __name__ == '__main__':
    unittest.main()
