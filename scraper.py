from selenium import webdriver
from chromedriver import get_chromedriver_path
from options_selector import submit_search_options
from people_scraper import scrape_people

print("Hello! In a few seconds, this program will open up Selenium, a browser for webscraping.")
filepath = get_chromedriver_path()
driver = webdriver.Chrome(filepath)
driver.get('https://guides.library.cornell.edu/egenealogy/essentials')
print("Please click on Ancestry and login. Once you are done please press enter.")
input("Press enter to continue: ")

people = []
races = ["Chinese", "Japanese", "Vietnamese", "Korean"]
for race in races:
    driver.get('https://www.ancestrylibrary.com/search/categories/35/')
    
    # select and submit some options
    submit_search_options(driver, race)

    # wait for next page to load
    driver.implicitly_wait(2)

    # collect all people links and hover over them to get info on them
    people += scrape_people(driver)

