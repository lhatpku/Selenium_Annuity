from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pprint import pprint

browser = webdriver.Chrome('/Users/luh/Documents/chromedriver/chromedriver')
browser.get('https://www.immediateannuities.com/')

def find_by_name_select(selection_name,option_name):
    print(f"//select[@name={selection_name}]")
    select_input = browser.find_element_by_xpath(f"//select[@name='{selection_name}']")
    select = Select(select_input)
    select.select_by_visible_text(option_name)

def scrape_Annuity_Info(annuity_info):
    invest_amount = annuity_info['invest_amount']

    invest_amount_input = browser.find_element_by_css_selector('#premium')
    invest_amount_input.send_keys(annuity_info['invest_amount'])

    income_begin_input = browser.find_element_by_css_selector('#income_start_date')
    income_begin_select = Select(income_begin_input)
    income_begin_select.select_by_visible_text(annuity_info['deferral_period'])

    find_by_name_select('age',annuity_info['age'])
    find_by_name_select('gender',annuity_info['gender'])
    find_by_name_select('state',annuity_info['state'])

    '''
    Click the button
    '''
    time.sleep(0.5)

    submit_input_1 = browser.find_element_by_css_selector('#calc-submit > input')
    submit_input_1.click()

    '''
    Scarping the annuity information
    '''
    for row_num in range(5):

        name_css = f'.ar-annuity-table-main tbody tr:nth-of-type({row_num+2}) td:nth-of-type(2)'
        payout_amount_css = f'.ar-annuity-table-main tbody tr:nth-of-type({row_num+2}) td:nth-of-type(3)'

        field_name = browser.find_element_by_css_selector(name_css).text
        field_value = browser.find_element_by_css_selector(payout_amount_css).text

        annuity_info[field_name] = field_value
    
    return annuity_info


    