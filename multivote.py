import time
import os
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

BOT_ID = 571027211407196161
DELAY = 2
TIMEOUT = 10
AD_TIMEOUT = 30


def main(token, bot):
    # Initialize Chrome browser
    options = uc.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_experimental_option('useAutomationExtension', False)
    browser = uc.Chrome(options=options)

    # Go to top.gg page
    browser.get('https://top.gg/bot/%s/vote' % bot)

    # Cloudflare anti-bot
    time.sleep(5)

    # Find Login to Vote and click
    loginElem = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Login to vote"))
    )
    loginElem.click()
    print('[click] Login to Vote')

    # Wait for redirects
    try:
        # Wait until login page
        WebDriverWait(browser, TIMEOUT).until(
            EC.url_contains('https://discord.com/login')
        )
        print('[wait] Login page')

        # Add token
        time.sleep(DELAY)
        add_token(browser, browser.current_url, token)

        time.sleep(DELAY)
        browser.refresh()

        # Wait for redirects until authorize page
        WebDriverWait(browser, TIMEOUT).until(
            EC.url_contains('https://discord.com/oauth2/authorize')
        )
        print('[wait] Authorize page')

        # Find and click Authorize button
        authorizeElem = WebDriverWait(browser, TIMEOUT).until(
            EC.presence_of_element_located(
                (By.XPATH, ".//button/div[contains(text(),'Author')]"))
        )
        time.sleep(DELAY)
        authorizeElem.click()
        print('[click] Authorize')

        # Wait for redirects
        WebDriverWait(browser, TIMEOUT).until(
            EC.url_contains('https://top.gg/bot/%s/vote' % bot)
        )
        print('[wait] Redirects')

        # Find vote button
        voteBtn = WebDriverWait(browser, AD_TIMEOUT).until(
            EC.element_to_be_clickable(
                (By.XPATH, ".//button[contains(text(),'Vote')]"))
        )
        time.sleep(DELAY)
        print('[clickable] Vote')

        # Move mouse to button, then click
        action_chain = ActionChains(browser)
        action_chain.move_to_element(voteBtn)
        action_chain.click(voteBtn)
        action_chain.perform()
        time.sleep(DELAY)
        print('[click] Vote')
    except Exception as exc:
        print("An error occurred:\n %s" % (exc))
        pass
    finally:
        browser.close()


def add_token(driver, url, token='abc'):
    # JavaScript code to recreate the localStorage object, has to be executed after each reload on discord's sites.
    recreate_localStorage_script = '''
    const iframe = document.createElement('iframe');
    document.head.append(iframe);
    const pd = Object.getOwnPropertyDescriptor(iframe.contentWindow, 'localStorage');
    iframe.remove();    
    Object.defineProperty(window, 'localStorage', pd);
    '''

    print('[add_token] url:', url)

    # Opens the URL
    driver.get(url)

    # Waits for delay time after the site loaded fully
    time.sleep(DELAY)

    try:
        driver.execute_script(
            recreate_localStorage_script)  # Recreates the localStorage Object after it gets deleted by discord
        driver.execute_script(
            f"window.localStorage.setItem('token', '\"{token}\"');")  # Adds the token to login with to the localStorage
        # Refreshes the Site
        driver.refresh()

        # If you get redirected to https://discord.com/app it worked.
        # Otherwise the token probably doesn't work.

        # Checking if the token is in the localStorage
        driver.execute_script(
            recreate_localStorage_script)  # Recreating the localStorage Object again, has to be done after every reload
        print('[add_token] get token:', driver.execute_script(
            f"return window.localStorage.getItem('token');"))  # Gets the token value from the localStorage

    except Exception as ex:
        # If an exception occurs, it gets printed out here.
        print('[Exception]', ex)


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tokens.txt")) as f:
        tokenlist = f.read().splitlines()
    for i in range(len(tokenlist)):
        main(tokenlist[i], BOT_ID)
