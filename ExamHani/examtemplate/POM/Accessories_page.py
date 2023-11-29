from ExamHani.examtemplate.POM.lib  import helpers
from selenium.webdriver.common.by import By

class AccPage(helpers):
    hats=(By.XPATH, "(//*[@id='main']/div/div/div[2]/div/div[2]/div/div[4]/article/a}")
    your_selection=(By.XPATH, "(//*[@id='main']/div/div/div/div[4]/div/div/div/div/div/div")

    def click_on_hats(self):
        self.find_and_click(self.click_on_hats)

