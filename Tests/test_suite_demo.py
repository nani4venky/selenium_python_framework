import unittest
from Tests.home_page.login_test import LoginTests
from Tests.courses.register_courses_csv_data import RegisterCoursesCSVDataTests

# get all tests from test classes

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)

# Test Suite creation
smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)