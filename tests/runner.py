# tests/runner.py
import unittest
from unittest.loader import getTestCaseNames

import test_face
import test_cube
import test_game

from test_face import TestFace
from test_cube import TestCube
from test_game import TestGame

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_face))
suite.addTests(loader.loadTestsFromModule(test_cube))
suite.addTests(loader.loadTestsFromModule(test_game))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)


face_tests = getTestCaseNames(TestFace, prefix='test_')
cube_tests = getTestCaseNames(TestCube, prefix='test_')
game_tests = getTestCaseNames(TestGame, prefix='test_')

total_test_count = len(face_tests) + len(cube_tests) + len(game_tests)
failed_test_count = len(result.failures)
successful_test_count = total_test_count - failed_test_count

print("===[Test Suite Summary]===\n")
print(f"Total Tests: {total_test_count}\n")
print(f"Successful Tests:\n Count: {successful_test_count}/{total_test_count} \t Percentage: {successful_test_count/total_test_count}%\n")
print(f"Failed Tests:\n Count: {failed_test_count}/{total_test_count} \t Percentage: {failed_test_count/total_test_count}%\n")