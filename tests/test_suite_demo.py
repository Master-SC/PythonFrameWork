import unittest
from tests.home.login_test import login_test
from tests.courses.couresddtcsv_test import courseCsvData_test

# Get all the tests from the test classes

tc1 = unittest.TestLoader().loadTestsFromTestCase(login_test)
tc2 = unittest.TestLoader().loadTestsFromTestCase(courseCsvData_test)

# Create a Test Suite
demoTest = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(demoTest)
