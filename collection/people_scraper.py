from person_scraper import scrape_person

def scrape_people(driver):
    people = []

    # number of result pages
    number_of_pages_xpath = '/html/body/div[5]/div/div/div[3]/section/footer/div[2]/div/div[2]/nav/span/span'
    number_pages_elem = driver.find_element_by_xpath(number_of_pages_xpath)
    num_pages = int(number_pages_elem.text)

    for i in range(num_pages):
        people_link_xpath = '/html/body/div[5]/div/div/div[3]/section/div/div/div[2]/ol/li/div[1]/div/div[1]/div/a'
        people_link_elems = driver.find_elements_by_xpath(people_link_xpath)
        people_links = [elem.get_attribute('href') for elem in people_link_elems]

        for people_link in people_links:
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(people_link)
            people.append(scrape_person(driver))
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            
        if i != num_pages - 1:
            next_button_xpath = '/html/body/div[5]/div/div/div[3]/section/footer/div[2]/div/div[2]/nav/a[2]'
            next_button = driver.find_element_by_xpath(next_button_xpath)
            next_button.click()

    return people