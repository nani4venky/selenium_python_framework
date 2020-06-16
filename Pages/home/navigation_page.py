from Base.selenium_driver import SeleniumDriver
import Utilities.custom_logger as cl
import logging
import time


class NavigationPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "All Courses"
    _all_courses = "My Courses"
    _practice = "Practice"
    _user_icon = "//div[@id='navbar']//span[text()='Test']"

    def navigateToAllCourses(self):
        self.elementClick(self._all_courses, locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(self._my_courses, locatorType="link")

    def navigateToPractice(self):
        self.elementClick(self._practice, locatorType="link")

    def navigateToUserSettings(self):
        self.elementClick(self._user_icon, locatorType="xpath")

