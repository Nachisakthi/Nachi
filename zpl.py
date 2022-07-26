import time
import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path=r"C:\selenium web drivers\geckodriver.exe")

def loginzen():
    """this function logs in the zen portal"""

    url = "https://www.zenclass.in/login"
    requests.get(url)
    driver.get(url)
    time.sleep(3)
    driver.maximize_window()
    driver.find_element(
        by=By.XPATH,
        value="//*[@id='root']/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input"
    ).send_keys("rajamuthaiah25@gamil.com")
    driver.find_element(
        by=By.XPATH,
        value="//*[@id='root']/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input"
    ).send_keys("Ramuamma@25")
    login_button = driver.find_element(
        by=By.XPATH,
        value="//*[@id='root']/div/div/div[1]/div[2]/div/div[1]/form/button")
    time.sleep(1)
    login_button.click()
    time.sleep(3)
    assert "class" in driver.current_url

def fetch_details():
    """this function document the information from the left panel
     of guvi zen portal into a csv file"""
    hover_over = driver.find_element(
        by=By.XPATH,
        value="//*[@id='root']/div[1]/nav/ul/div[1]/li/span/div/div[1]")
    achains = ActionChains(driver)
    achains.move_to_element(hover_over).perform()
    xpath = "/html/body/div[1]/div[1]/nav/ul"
    details = driver.find_element(by=By.XPATH,value="xpath")
    export = details.text
    str_1 = export
    list_1 = str_1.split()
    document = ['Document']
    with open('new.csv','w' ,encoding="utf-8") as write_f:
        write = csv.write(write_f)
        write.writerow(document)
        write.writerow(list_1)

def cancel_instancesolution():
    """this function cancels the instance solution to create a new query"""
    hover_over_leftpanel = driver.find_element(
        by=By.XPATH,
        value="//*[@id='root']/div[1]/nav/ul/div[1]/li/span/div/div[1]"
    )
    achains =ActionChains(driver)
    achains.move_to_element(hover_over_leftpanel).perform()
    click_query = driver.find_element(
        by=By.XPATH,
        value="//*[@id='root']/div[1]/nav/ul/div[6]/li/span/div/div[2]")
    click_query.click()
    hover_over_away = driver.find_element(
        by=By.XPATH,
        value="/html/body/div/div[2]/div/div[1]/div[2]/input")
    achains = ActionChains(driver)
    achains.move_to_element(hover_over_away).perform()

def create_query():
    """this function raises 5 queries as per requirement"""
    count =0
    while count < 5:
        click_createquery = driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div[2]/div/div[1]/div[1]/button")
        click_createquery.click()
        click_cancel = driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section[3]/div[2]/button[1]")
        click_cancel.click()
        click_category =driver.find_element(
            by=By.XPATH,
            value="//*[@id='root']/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select")
        click_category.click()
        click_dd = Select(click_category)
        click_dd.select_by_index(1) #selecting the options
        language_1 = driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[4]/select")
        language_1.click()
        click_dd = Select(language_1)
        click_dd.select_by_index(1)
        scroll =driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/div/lable[3]")
        driver.execute_script("arguments[0].scrollintoview():", scroll)
        query_title = driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/div/input")
        query_title.send_keys("Guvi Python AT - 1&2 Automation Project")
        query_description = driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/textarea")
        query_description.send_keys(
            "This is a project Test code running for the python automation - "
            "1&2 Project given by mentor Mr. Suman Gangopadhyay")
        click_create = driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div[2]/div/div[2]/div/div/form/div[13]/div/button"
        )
        click_create.click()

        time.sleep(3)
        print(count)
        count = count + 1
    driver.close()