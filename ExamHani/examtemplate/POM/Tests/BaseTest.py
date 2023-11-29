import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:
    def navigate_to_accessories_page(self):
        self.HomePage.click_on_accessories()

    def navigate_to_hats(self):
        self.Accessories_page.click_on_hats()


    def select_checkbox(self):
        self.Hats_page.check_checkbox()

    def text_check(self):
        self.Hats_page.assert_text
