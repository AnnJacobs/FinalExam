from ExamHani.examtemplate.POM.Tests import BaseTest


class TestExam(BaseTest):
    def test_filter_text(self):
     self.navigate_to_accessories_page()
     self.navigate_to_hats()
     self.select_checkbox()
     self.text_check
