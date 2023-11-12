# tests/runner.py
import unittest

import cube
import face
import game

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(face))
suite.addTests(loader.loadTestsFromModule(cube))
suite.addTests(loader.loadTestsFromModule(game))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)