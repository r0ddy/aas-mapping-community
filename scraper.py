from selenium import webdriver
from chromedriver import get_chromedriver_path
from selenium.webdriver.common.action_chains import ActionChains

print("Hello! In a few seconds, this program will open up Selenium, a browser for webscraping.")
filepath = get_chromedriver_path()
driver = webdriver.Chrome(filepath)
driver.get('https://guides.library.cornell.edu/egenealogy/essentials')
print("Please click on Ancestry and login. Once you are done please press enter.")
input("Press enter to continue: ")
driver.get('https://www.ancestrylibrary.com/search/categories/35/')
# fill out residence box
residence_textbox_xpath = '/html/body/div[3]/div/div/div/section[1]/div/div/div/div/div/form/div[1]/div/fieldset[2]/div[3]/div/input[1]'
residence_textbox = driver.find_element_by_xpath(residence_textbox_xpath)
residence_textbox.send_keys('Ithaca, Tompkins, New York, USA')

# fill out race box
race_textbox_xpath = '/html/body/div[3]/div/div/div/section[1]/div/div/div/div/div/form/div[1]/div/div[5]/div[2]/input'
race_textbox = driver.find_element_by_xpath(race_textbox_xpath)
race_textbox.send_keys('Chinese')

# check off to get exact results
race_exact_checkbox_xpath = '/html/body/div[3]/div/div/div/section[1]/div/div/div/div/div/form/div[1]/div/div[5]/div[2]/div/input[1]'
race_checkbox = driver.find_element_by_xpath(race_exact_checkbox_xpath)
race_checkbox.click()

# search button
search_button_xpath = '/html/body/div[3]/div/div/div/section[1]/div/div/div/div/div/form/div[1]/div/div[6]/div[1]/input'
search_button = driver.find_element_by_xpath(search_button_xpath)
search_button.click()

# wait for next page to load
driver.implicitly_wait(2)

# collect all people links and hover over them to get info on them
people_link_xpath = '/html/body/div[5]/div/div/div[3]/section/div/div/div[2]/ol/li/div[1]/div/div[1]/div/a'
people_link_elems = driver.find_elements_by_xpath(people_link_xpath)
people_links = [elem.get_attribute('href') for elem in people_link_elems]

for people_link in people_links:
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(people_link)
    name_field_xpath = '/html/body/main/div[2]/div[1]/div[1]/section/div[2]/section/div/div[4]/div[1]/table/tbody/tr[1]/td'
    name_field = driver.find_element_by_xpath(name_field_xpath)
    print(name_field.text)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

driver.close()