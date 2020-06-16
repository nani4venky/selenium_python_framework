from selenium import webdriver
from Pages.courses.register_courses_page import RegisterCoursesPage
from Utilities.teststaus import TestStatus
import unittest
import pytest
import time
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "1234 5678 9012 3456", "1220", "444", "12345"),
          ("Learn Python 3 from scratch", "1234 5678 9012 3456", "1220", "444", "12345"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV, postal):
        self.courses.enterCourseName(courseName)
        time.sleep(5)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV, zip=postal)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")
        self.driver.get("https://letskodeit.teachable.com/courses")
        # self.driver.find_element_by_link_text("All courses").click().perform()
