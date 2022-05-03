row_xpath = '/html/body/main/div[2]/div[1]/div[1]/section/div[2]/section/div/div[4]/div[1]/table/tbody/tr'
label_cell_xpath = '/html/body/main/div[2]/div[1]/div[1]/section/div[2]/section/div/div[4]/div[1]/table/tbody/tr[{}]/th'
value_cell_xpath = '/html/body/main/div[2]/div[1]/div[1]/section/div[2]/section/div/div[4]/div[1]/table/tbody/tr[{}]/td'

def scrape_person(driver):
    rows = len(driver.find_elements_by_xpath(row_xpath))
    person = {}
    for i in range(1, rows-1):
        label_cell = driver.find_element_by_xpath(label_cell_xpath.format(i))
        value_cell = driver.find_element_by_xpath(value_cell_xpath.format(i))
        if label_cell is not None and value_cell is not None:
            person[label_cell.text] = value_cell.text
    return person