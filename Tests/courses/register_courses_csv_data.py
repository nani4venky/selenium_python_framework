from selenium import webdriver
from Pages.courses.register_courses_page import RegisterCoursesPage
from Pages.home.navigation_page import NavigationPage
from Utilities.teststaus import TestStatus
import unittest
import pytest
import time
from ddt import ddt, data, unpack
from Utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.driver.get("https://letskodeit.teachable.com/courses")

    @pytest.mark.run(order=1)
    @data(*getCSVData("C:/Users/VenkyAB/workspace_python/Frameworks/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV, postal):
        self.courses.enterCourseName(courseName)
        time.sleep(2)
        self.courses.selectCourseToEnroll(courseName)
        time.sleep(2)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV, zip=postal)
        time.sleep(2)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")

        # self.driver.find_element_by_link_text("All courses").click().perform()
