
def fill_out_textbox(driver, xpath, value):
    textbox = driver.find_element_by_xpath(xpath)
    if textbox is not None:
        textbox.send_keys(value)

def click_elem(driver, xpath):
    elem = driver.find_element_by_xpath(xpath)
    if elem is not None:
        elem.click()

def submit_search_options(driver, race):
    # fill out residence box
    residence_textbox_xpath = '/html/body/div[3]/div/div/div/section[1]/div/div/div/div/div/form/div[1]/div/fieldset[2]/div[3]/div/input[1]'
    fill_out_textbox(driver, residence_textbox_xpath, 'Ithaca, Tompkins, New York, USA')

    # fill out race box
    race_textbox_xpath = '/html/body/div[3]/div/div/div/section[1]/div/div/div/div/div/form/div[1]/div/div[5]/div[2]/input'
    fill_out_textbox(driver, race_textbox_xpath, race)

    # check off to get exact results
    race_exact_checkbox_xpath = '/html/body/div[3]/div/div/div/section[1]/div/div/div/div/div/form/div[1]/div/div[5]/div[2]/div/input[1]'
    click_elem(driver, race_exact_checkbox_xpath)

    # search button
    search_button_xpath = '/html/body/div[3]/div/div/div/section[1]/div/div/div/div/div/form/div[1]/div/div[6]/div[1]/input'
    click_elem(driver, search_button_xpath)
