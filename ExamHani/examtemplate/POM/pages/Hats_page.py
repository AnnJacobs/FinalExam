from ExamHani.examtemplate.POM.lib import helpers
from selenium.webdriver.common.by import By


class FirstCheckbox(helpers):
    checkbox=(By.XPATH, "(//*[@id='searchFilters']/div[1]/div[2]/section[3]/div[2]/ul/li[1]/a)")


    def check_checkbox(self):
        self.find_and_click(self.check_checkbox())


    def assert_text(self,check_text="Filters were included based on your selections."):
       actual_text=self.find(self.your_selection,get_text=True)
       assert actual_text==check_text