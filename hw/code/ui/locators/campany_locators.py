from datetime import datetime

# import now
from selenium.webdriver.common.by import By


class CampanyPageLocators:
    OPEN_CREATION_NEW_CAMPANY = (By.XPATH, "//span[text()='Создать']")
    CHOOSE_SOCIETY = (By.XPATH, "//span[text()='Сообщество и профиль']")
    DROPDOWN_ADVS_OBJECT = (By.XPATH, "//input[@data-testid='vk-owner-selector']")
    CHANGE_NAME_CAMPANY = (By.XPATH, "//div[contains(@class, 'EditableTitle_container')]")
    INPUT_NEW_CAMPANY_NAME = (By.XPATH, "textarea//[starts-with(@class, 'EditableTitle_input')]")
    INPUT_NEW_NAME = (By.CLASS_NAME, 'EditableTitle_inputContainer')
    INPUT_DESCRIPTION_APP = (By.XPATH, "//textarea[@placeholder='Опишите ваше предложение']")
    INPUT_END_DATA_CAMPANY = (By.XPATH, "//span[@data-testid='end-date']")
    INPUT_SELECT_END_DATA = (By.XPATH, "//div[contains(@class, 'vkuiCalendarDay__hinted')]//div[contains(@class, 'vkuiCalendarDay__day-number') and text()='20']")
    DROPDOWN_MAIN_MOVEMENT = (By.XPATH, "//input[@data-testid='priced-goal']")
    SWITCH_OPTIMIZATION = (By.XPATH, "//label[input[@data-testid='budget-optimization']]")
    DROPDOWN_STRATEGY = (By.XPATH, "//input[@data-testid='autobidding-mode']")
    INPUT_TARGETING = (By.XPATH, "//input[@data-testid='targeting-not-set']")
    DROPDOWN_TIME_STRATEGY = (By.XPATH, "//input[@data-testid='budget']")
    BUTTON_CONTINUE = (By.XPATH, "//span[contains(@class, 'vkuiButton__content') and text()='Продолжить']")
    BUTTON_SELECT_MOSCOW = (By.XPATH, "//span[contains(@class, 'vkuiButton__content') and text()='Москва']")
    SWITCH_AUDIENCE = (By.XPATH, "//label[input[@type='checkbox']]")
    BUTTON_SELECT_INTERESTS = (By.XPATH, "//div[@role='button'][.//h4[text()='Интересы']]")
    INPUT_INTERESTS = (By.XPATH, "//label[input[@placeholder='Введите название']]")
    BUTTON_SELECT_INTERESTS_AUTO = (By.XPATH, "//div[@class='vkuiCustomSelectOption__main']//div[text()='Авто премиум класс']")
    BUTTON_SELECT_SPORT_INTERESTS = (By.XPATH, "//div[contains(@class, 'vkuiCustomSelectOption__main')]//div[text()='Спорт интерес']")
    INPUT_DESCRIPTION_ADV = (By.XPATH, "//div[@data-testid='Описание 2000 знаков']")
    INPUT_TITLE_ADV = (By.XPATH, "//div[@data-testid='заголовок, макс. 40 символов']")
    INPUT_TITLE_ADV_CLICK = (By.XPATH, "//div[starts-with(@class, 'TextRole_textFieldWrap')]//div[contains(@class, 'EditableTextField__wrapper')]//div[@data-testid='заголовок, макс. 40 символов']")
    INPUT_DESCRIPTION_ADV_CLICK = (By.XPATH, "//div[starts-with(@class, 'TextRole_textFieldWrap')]//div[contains(@class, 'EditableTextField__wrapper')]//div[@data-testid='Описание 2000 знаков']")
    BUTTON_OPEN_AI = (By.XPATH, "//span[@class='vkuiButton__content' and text()='Созданное нейросетью']")
    BUTTON_SELECT_IMAGE = (By.XPATH, "//div[@class='ReactVirtualized__Grid__innerScrollContainer']/div[1]/div[1]")
    BUTTON_ADD_IMAGE = (By.XPATH, "//span[@class='vkuiButton__in']/span[@class='vkuiButton__content' and text()='Добавить (1/8)']")
    BUTTON_NEW_VIDIO = (By.XPATH, "//div[starts-with(@data-name, 'content')]")
    BUTTON_PUBLISH = (By.XPATH, "//span[@class='vkuiButton__in']/span[@class='vkuiButton__content' and text()='Опубликовать']")
    BUTTON_PUBLISH_SUBMIT = (By.XPATH, "//span[@class='vkuiButton__content' and text()='Отправить']")
    BUTTON_CHECKBOX = (By.XPATH, "//label[input[@type='checkbox' and contains(@class, 'vkuiCheckbox__input')]]")
    BUTTON_OPEN_OPTIONS = (By.XPATH, "//button//span[contains(@class, 'vkuiButton__content') and text()='Действия']")
    BUTTON_OPEN_OPTIONS_DELETE = (By.XPATH, "//span[text()='Удалить']")
    CREATED_CAMPANY = (By.XPATH, "//button[text()='Кампания 2024-12-17']")
    DIV_CREATE_CAMPANY_NEW_BUDGET = (By.XPATH, "//div[text()='101,00 ₽']")
    DIV_CREATE_CAMPANY_NEW_ACTION = (By.XPATH, "//span[text()='Подписка на сообщество']")
    BUTTON_CREATE_CAMPANY_CLOSE_EDIT = (By.XPATH, "//button[@aria-label='Close']")

    BUTTON_EDIT_CAMPANY = (By.XPATH, "//a[@data-testid='edit']")
    INPUT_EDIT_CAMPANY_ADD_NEW_CITY = (By.XPATH, "//input[@data-testid='search']")
    BUTTON_EDIT_CAMPANY_ADD_SAINT_P = (By.XPATH, "//span/b[text()='Санкт-Петербург']")
    BUTTON_EDIT_CAMPANY_SELECT_END_DATE = (By.XPATH, "//span[@data-testid='end-date']")
    BUTTON_EDIT_CAMPANY_SELECT_DATE_27 = (By.XPATH, "//div[@class='vkuiCalendarDay__hinted']//div[@class='vkuiCalendarDay__day-number' and text()='27']")
    INPUT_EDIT_CAMPANY_ADD_NEW_BUDGET = (By.XPATH, "//input[@data-testid='targeting-not-set']")
    BUTTON_EDIT_CAMPANY_OPEN_GROUPS = (By.XPATH, "//div[@data-testid='menu-item']//span[text()='Группа 2024-12-17']")
    BUTTON_EDIT_CAMPANY_OPEN_ADV = (By.XPATH, "//div[@data-testid='menu-item']//span[text()='Объявление 2024-12-17']")
    BUTTON_EDIT_CAMPANY_SUBMIT = (By.XPATH, "//button[@data-testid='submit']")
    DIV_EDIT_CAMPANY_NEW_BUDGET = (By.XPATH, "//div[text()='121,00 ₽']")
    DIV_EDIT_BUDGET_NEW_CAMPANY_NAME = (By.XPATH, "//button[text()='Кампания 2024-12-17']")
    DIV_EDIT_BUDGET_NEW_END_DATE = (By.XPATH, "//button[text()='27.12.2024']")
    DIV_EDIT_BUDGET_NEW_CITY = (By.XPATH, "//h4[text()='Санкт-Петербург']")
    DIV_EDIT_BUDGET_NEW_DESCR = (By.XPATH, "//p[text()='Тестовое описание после редактирования']")
