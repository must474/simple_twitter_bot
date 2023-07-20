from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from email.message import EmailMessage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .email_service import sending_email
from .tweet_handling import choosing_todays_tweet

#In these two lines of code are for keeping the Chrome open after the execution of the code
# if you wanna close the Chrome window after the execution,you can comment out these lines
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
tweet=choosing_todays_tweet()
if tweet:
    #setting uo our driver
    driver=webdriver.Chrome(options=options)
    driver.get("https://twitter.com/i/flow/login")
    sleep(5)
    #your twitter account
    username="twitter_account_username"
    password="twitter_account_password"

    #Logining
    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME,"input")))
    username_input.send_keys(username)
    sleep(5)
    all_buttons = driver.find_elements(By.XPATH,"//div[@role='button']")
    all_buttons[-2].click()
    sleep(10)
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@type='password']")))
    password_input.send_keys(password)

    login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@data-testid='LoginForm_Login_Button']")))
    login.click()
    sleep(5)

    #tweeting
    tweet_text_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']")))
    tweet_text_box.send_keys(tweet)
    tweet_button = driver.find_element(By.XPATH,"//div[@data-testid='tweetButtonInline']")
    tweet_button.click()
    message = EmailMessage()
    message['Subject'] = 'Tweeted'
    message.set_content("Successfully tweeted!Today's tweet is {}".format(tweet))
    sending_email(message)

else:
        # Create the email message
        message = EmailMessage()
        message['Subject'] = 'No tweets'
        message.set_content("You should add some tweets into tweets file")  
        sending_email(message)

