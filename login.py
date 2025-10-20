# Import libraries and packages for the project 

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Task 1: Login to Linkedin
def login_linkedin(username, password):
    # Task 1.1: Open Chrome and Access Linkedin login site
    driver = webdriver.Chrome()
    sleep(2)
    url = "https://www.linkedin.com/login"
    driver.get(url)
    driver.maximize_window()
    print("- Finish initializing a driver")
    sleep(2)
    
    # Task 1.2: Key in login credentials
    email_field = driver.find_element("id","username")
    email_field.send_keys(username)
    print("- Finish keying in email")
    sleep(3)

    password_field  = driver.find_element("id","password")
    password_field.send_keys(password)
    print('- Finish keying in password')
    sleep(2)

    # Task 1.2: Click the Login button
    signin_field = driver.find_element("class name", 'login__form_action_container')

    # dar scroll (colocar um elemento na tela)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", signin_field)

    # Espera dinâmica

    espera = WebDriverWait(driver, 10)
    espera.until(EC.element_to_be_clickable(signin_field))
    signin_field.click()
    sleep(3)

    print('- Finish Task 1: Login to Linkedin')    

    return driver


if __name__ == "__main__":
    login_linkedin()
