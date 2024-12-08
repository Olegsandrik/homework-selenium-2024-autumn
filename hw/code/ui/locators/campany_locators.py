from datetime import datetime

import now
from selenium.webdriver.common.by import By


class CampanyPageLocators:
    OPEN_CREATION_NEW_CAMPANY = (By.XPATH, "//span[text()='Создать']")
    CHOOSE_SOCIETY = (By.XPATH, "//span[text()='Сообщество и профиль']")
    DROPDOWN_ADVS_OBJECT = (By.XPATH, "//input[@data-testid='vk-owner-selector']")
    CHANGE_NAME_CAMPANY = (By.XPATH, "//div[contains(@class, 'EditableTitle_container')]")
    INPUT_NEW_CAMPANY_NAME = (By.XPATH, "//div[contains(@class, 'EditableTitle_inputContainer')]")
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
    BUTTON_SELECT_RUSSIA = (By.XPATH, "//span[contains(@class, 'vkuiButton__content') and text()='Россия']")
    SWITCH_AUDIENCE = (By.XPATH, "//label[input[@type='checkbox']]")
    BUTTON_SELECT_INTERESTS = (By.XPATH, "//div[@role='button'][.//h4[text()='Интересы']]")
    INPUT_INTERESTS = (By.XPATH, "//label[input[@placeholder='Введите название']]")
    BUTTON_SELECT_INTERESTS_AUTO = (By.XPATH, "//div[@class='vkuiCustomSelectOption__main']//div[text()='Авто премиум класс']")
    BUTTON_SELECT_SPORT_INTERESTS = (By.XPATH, "//div[contains(@class, 'vkuiCustomSelectOption__main')]//div[text()='Спорт интерес']")
    INPUT_DESCRIPTION_ADV = (By.XPATH, "//div[@data-testid='Описание 2000 знаков']")
    BUTTON_OPEN_AI = (By.XPATH, "//span[@class='vkuiButton__content' and text()='Созданное нейросетью']")
    BUTTON_SELECT_IMAGE_1 = (By.XPATH, "//div[@class='ReactVirtualized__Grid__innerScrollContainer']/div[1]/div[1]")
    BUTTON_SELECT_IMAGE_2 = (By.XPATH, "//div[@class='ReactVirtualized__Grid__innerScrollContainer']/div[1]/div[2]")
    BUTTON_ADD_IMAGE = (By.XPATH, "//span[@class='vkuiButton__in']/span[@class='vkuiButton__content' and text()='Добавить (2/8)']")
    BUTTON_NEW_VIDIO = (By.XPATH, "//button[contains(@class, 'vkuiButton--mode-link')]")
    BUTTON_PUBLISH = (By.XPATH, "//span[@class='vkuiButton__in']/span[@class='vkuiButton__content' and text()='Опубликовать']")
    BUTTON_CHECKBOX = (By.XPATH, "//input[@type='checkbox' and contains(@class, 'vkuiCheckbox__input')]")
    BUTTON_OPEN_OPTIONS = (By.XPATH, "//span[contains(@class, 'vkuiButton__content') and text()='Действия']")
    BUTTON_OPEN_OPTIONS_DELETE = (By.XPATH, "//span[text()='Удалить']")
    CREATED_CAMPANY = (By.XPATH, "//button[text()='Тестовое название']")