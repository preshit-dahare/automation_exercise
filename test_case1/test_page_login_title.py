from test_utilities1.login_page_utilities import LoginPageActions


class TestLoginTitle:


    def test_login_page_title(self):
        """
        test case to test the title of our webpage
        :return:
        """
        _expected_title = "Automation Exercise - Signup / Login"
        assert LoginPageActions().title_of_page() == _expected_titlegit