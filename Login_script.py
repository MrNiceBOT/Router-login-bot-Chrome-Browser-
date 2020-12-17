from selenium import webdriver            # pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Login():

    usernameStr = 'admin'
    passwordStr = 'admin'

    browser = webdriver.Chrome(executable_path='C:/Users/...../...../....../...../chromedriver.exe')
    ## executable path is chrome driver.exe folder  
    
    LOGIN_URL ='http://192.168.1.1/' # or your special router login URL

    browser.get(LOGIN_URL)

    # fill in username and hit the next button

    username = browser.find_element_by_name('Login_Name')
    username.send_keys(usernameStr)
    

    password = browser.find_element_by_name('Login_Pwd')

    
    password.send_keys(passwordStr)

    signInButton = browser.find_element_by_name('texttpLoginBtn')
    signInButton.click()

    

    add_experimental_option("detach", True)

    ## this line doing deteach the chrome window for not close 
    ## if you close python command line or close chrome window code be deactive
    
    if __name__ == "__main__":
        Login()
    
