from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# Launch the browser with 4 tabs.


def launchBrowser():
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
# Disables infobar: 'Chrome is being controlled by automation blah blah.' Check: https://github.com/GoogleChrome/chrome-launcher/blob/master/docs/chrome-flags-for-tools.md#--enable-automation if anything goes wrong.
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
# Ignores certificate and ssl errors.
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
# Doesn't work!
    options.add_experimental_option('detach', True)
# Reject chrome notifications.
    prefs = {'profile.default_content_setting_values.notifications': 2}
    options.add_experimental_option('prefs', prefs)
# This line works for both the maximization of the window and the notifications preference.
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\Bernardo\Desktop\Python Projects\Automations\chromedriver.exe')
    
# Main browser, first tab - River.
    driver.get('https://lapaginamillonaria.com/')
    cookies_button = driver.find_element_by_class_name('fc-button.fc-cta-manage-options.fc-secondary-button')
    ActionChains(driver).move_to_element(cookies_button).click(cookies_button).perform()
    interes_legitimo = driver.find_element_by_class_name('fc-preference-legitimate-interest.purpose') 
    if interes_legitimo.get_attribute('checked') == 'true':
        ActionChains(driver).move_to_element(interes_legitimo).click(interes_legitimo).perform()
        enviar_button = driver.find_element_by_class_name('fc-button.fc-save-continue.fc-primary-button')
        ActionChains(driver).move_to_element(enviar_button).click(enviar_button).perform()
    else:
        print("Couldn't proceed with our task, master Rari.")


# Second tab - La Nación.
    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")
    driver.get('https://www.lanacion.com.ar/')


# Third tab - BBC.
    driver.execute_script("window.open('about:blank', 'tab3')")
    driver.switch_to.window("tab3")
    driver.get('https://www.bbc.com/')
    cookies_button = driver.find_element_by_class_name('fc-button.fc-cta-manage-options.fc-secondary-button')
    ActionChains(driver).move_to_element(cookies_button).click(cookies_button).perform()
    interes_legitimo = driver.find_element_by_class_name('fc-preference-legitimate-interest.purpose') 
    if interes_legitimo.get_attribute('checked') == 'true':
        ActionChains(driver).move_to_element(interes_legitimo).click(interes_legitimo).perform()
        enviar_button = driver.find_element_by_class_name('fc-button.fc-save-continue.fc-primary-button')
        ActionChains(driver).move_to_element(enviar_button).click(enviar_button).perform()
        accept_continue = driver.find_element_by_class_name('continue-button.banner-button')
        ActionChains(driver).move_to_element(accept_continue).click(accept_continue).perform()
    else:
        print("Couldn't proceed with our task, master Rari.")

    take_me_to_news = driver.find_element_by_class_name('orb-nav-newsdotcom')
    ActionChains(driver).move_to_element(take_me_to_news).click(take_me_to_news).perform()


launching = launchBrowser()

#user_inp = input("Enter 'done' when done reading/browsing: ")

#while user_inp != 'done':
 #   continue
#if user_inp == 'done':
 #   quit()
