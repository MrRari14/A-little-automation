import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select


web = webdriver.Chrome()
web.get('https://formulier.amsterdam.nl/thema/sociaal/onderwijs-jeugd/aanmelden-taalcursus/')

time.sleep(2)

# Email
e_mail = "johndoe@gmail.com"
mail = web.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[4]/div[1]/div/div/div/div/div[1]/div/div/div[2]/div/input')
mail.send_keys(e_mail)

# First name

firstName = "John"
first = web.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[4]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/fieldset/table/tbody/tr/td[1]/div/div/input')
first.send_keys(firstName)

# Middle name

midName = "Doe"
mid = web.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[4]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/fieldset/table/tbody/tr/td[2]/div/div/input')
mid.send_keys(midName)

# Last name

lastName = "Doe"
last = web.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[4]/div[1]/div/div/div/div/div[1]/div/div/div[3]/div/fieldset/table/tbody/tr/td[3]/div/div/input')
last.send_keys(lastName)

# Street name

streetName = os.environ.get('STREET_NAME')
street = web.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[4]/div[1]/div/div/div/div/div[1]/div/div/div[4]/div/fieldset/table/tbody/tr/td[1]/div/div/input')
street.send_keys(streetName)

# House number

houseNumber = os.environ.get('HOUSE_NUMBER')
housenum = web.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[4]/div[1]/div/div/div/div/div[1]/div/div/div[4]/div/fieldset/table/tbody/tr/td[2]/div/div/input')
housenum.send_keys(houseNumber)

# Postal code

postalCode = "111"
postal = web.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[4]/div[1]/div/div/div/div/div[1]/div/div/div[5]/div/fieldset/table/tbody/tr/td[1]/div/div/input')
postal.send_keys(postalCode)

# Place name

placeName = "Diemen"
place = web.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[4]/div[1]/div/div/div/div/div[1]/div/div/div[5]/div/fieldset/table/tbody/tr/td[2]/div/div/input')
place.send_keys(placeName)

# District

select_drd = Select(web.find_element_by_id('Main_ctl162'))
select.Select(web.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[4]/div[1]/div/div/div/div/div[1]/div/div/div[6]/div/select')).select_by_index(6)


# BSN

bsnNumber = os.environ.get('BSN')
bsn = web.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[4]/div[1]/div/div/div/div/div[1]/div/div/div[8]/div/input')
bsn.send_keys(bsnNumber)

# Other Notes

otherNotes = "Ik wil die Nederlands taal leren omdat Ik hou heel veel die Nederlands praten en land. Ik heb die Gemeente boek en werkboek. Pick me!"
remarks = web.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[4]/div[1]/div/div/div/div/div[1]/div/div/div[9]/div/textarea')
remarks.send_keys(otherNotes)

# Next
next_button = web.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[4]/div[1]/div/div/div/div/div[2]/input')
ActionChains(web).move_to_element(next_button).click(next_button).perform()

# Finally submit form
submit_button = web.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[4]/div[1]/div/div/div/div/div[3]/input[2]')
ActionChains(web).move_to_element(submit_button).click(submit_button).perform()

time.sleep(10)