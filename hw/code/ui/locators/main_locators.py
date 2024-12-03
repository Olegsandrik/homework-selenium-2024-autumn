from selenium.webdriver.common.by import By


class MainPageLocators:
    OPEN_CABINET = (By.XPATH, '//a[contains(@class, "ButtonCabinet")]')


class LoginPageLocators:
    INPUT_PHONE = (By.XPATH, "//input[@name='login']")
    SUBMIT_PHONE = (By.XPATH, "//span[@class='vkuiButton__in']//span[text()='Продолжить']")
    INPUT_PASSWORD = (By.XPATH, "//input[@type='password']")
    SUBMIT_PASSWORD = (By.XPATH, "//span[@class='vkuiButton__in']")
    COUNTIUE_LOGIN = (By.XPATH, "//div[@class='vkuiSimpleCell vkuiSimpleCell--sizeY-none vkuiTappable vkuiTappable--sizeX-none vkuiTappable--hasPointer-none vkuiClickable__host vkuiClickable__realClickable vkui-focus-visible vkuiRootComponent']")