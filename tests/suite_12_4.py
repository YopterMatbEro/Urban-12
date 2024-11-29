import unittest
import tests_12_4

loggingST = unittest.TestSuite()
loggingST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_4.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(loggingST)
