from selenium import webdriver
import csv
from time import sleep
from parsel import Selector
from selenium.webdriver.common.keys import Keys
import parameters 

writer= csv.writer(open(parameters.result_file, 'w'))
writer.writerow(['name', 'job_title', 'location', 'ln_url'])

driver=webdriver.Chrome('C:/bin/latest/chromedriver')
driver.maximize_window()
sleep(0.5)

driver.get('https://www.linkedin.com/')
sleep(0.5)

driver.find_element_by_xpath("//a[text()='Sign in']").click()
sleep(0.5)
username_input= driver.find_element_by_name("session_key")
username_input.send_keys(parameters.username)
sleep(0.5)
username_password= driver.find_element_by_name("session_password")
username_password.send_keys(parameters.password)
sleep(0.5)

#Click Sign in Button
Sign_in_button= driver.find_element_by_xpath("//button[text()='Sign in']")
Sign_in_button.click()
sleep(5)

driver.get('https://www.google.com/')
sleep(0.5)

search_input=driver.find_element_by_name ("q")
sleep(2)
search_input.send_keys(parameters.search_query)

search_input.send_keys(Keys.RETURN)
sleep(3)

profiles= driver.find_elements_by_xpath("//div[@class='r']/a")
sleep(3)
profiles=[profile.get_attribute("href") for profile in profiles]
sleep(3)
for profile in profiles:
    driver.get(profile)
    sleep(5)

    sel=Selector(text=driver.page_source)
    name= sel.xpath("//title/text()").get().split(' | ')[0]
    job_title= sel.xpath("//h2[@class='mt1 t-18 t-black t-normal']/text()").get().strip()
    location=sel.xpath("//li[@class='t-16 t-black t-normal inline-block']/text()").get().strip()
    ln_url=driver.current_url

    print('/n')
    print(name)
    print(job_title)
    print(location)
    print(ln_url)
    print('/n')


    writer.writerow([name, job_title, location, ln_url])

driver.quit()
