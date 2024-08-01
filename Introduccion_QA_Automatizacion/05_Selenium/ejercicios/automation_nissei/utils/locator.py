from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    USER_SELECT = (By.ID, 'userSelect')
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    OPTIONS = (By.XPATH, '/html/body/div/div/div[2]/div/form/div/select/option')
    HOME_BUTTON = (By.CLASS_NAME, "home")

class MainPageLocators(object):
    USER_NAME = (By.CSS_SELECTOR, ".fontBig.ng-binding")
    ACCOUNT_SELECT = (By.ID, 'accountSelect')
    ACCOUNT_NUMBER = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/strong[1]")
    BALANCE = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/strong[2]")
    CURRENCY = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/strong[3]")
    HOME_BUTTON = (By.CLASS_NAME, "home")
    LOGOUT_BUTTON = (By.CLASS_NAME, "logout")
    TRANSACTIONS_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div/div[3]/button[1]")
    DEPOSIT_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div/div[3]/button[2]")
    WITHDRAW_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div/div[3]/button[3]")
    AMOUNT_INPUT_FIELD = (By.XPATH, "//input[@ng-model='amount']")
    CONFIRM_BUTTON = (By.XPATH, "//button[@type='submit']")
    RESULT_MESSAGE = (By.XPATH, "//span[@class='error ng-binding']")
 
class TransactionPageLocators(object):
    TRANSACTIONS_BUTTON = (By.XPATH, "//button[text()='Transactions']")
    DEPOSIT_BUTTON = (By.XPATH, "//button[text()='Deposit']")
    WITHDRAW_BUTTON = (By.XPATH, "//button[text()='Withdrawl']")
    ACCOUNT_SELECT = (By.ID, 'accountSelect')

class HomePageLocators(object):
    HOME_BUTTON = (By.CLASS_NAME, "home")
    MAIN_HEADING = (By.CSS_SELECTOR, "strong.mainHeading")
    LOGOUT_BUTTON = (By.CLASS_NAME, "logout")
    CUSTOMER_LOGIN_BUTTON = (By.XPATH, "//button[@ng-click='customer()']")
    MANAGER_LOGIN_BUTTON = (By.XPATH, "//button[@ng-click='manager()']")
