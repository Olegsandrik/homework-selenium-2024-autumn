from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    url = "https://id.vk.com/auth"

    def __str__(self):
        return "login"