from selenium import webdriver
from Helper.annuity_premium import AnnuityPremium,InputOptions
from collections import namedtuple
from itertools import product
from config import chrome_driver_loc
import csv

browser = webdriver.Chrome(chrome_driver_loc)

input_page = InputOptions(driver=browser)
input_page.go()

premium_selections = ['1,000,000']
income_start_selections = input_page.income_start()['text'][1:]
# age_selections = input_page.age()['text'][1:]
age_selections = list(map(lambda x:str(x),list(range(55,76))))
gender_selections = ['Male','Female']
state_selections = ['IL']

inputs_list = list(product(*[premium_selections,income_start_selections,age_selections,gender_selections,state_selections]))
Annuity_Record = namedtuple("AnnuityInput",["Premium","Income_Start","Age","Gender","State"])
inputs_list_tuple = list(map(lambda x: Annuity_Record(*x),inputs_list))

def getAnnuityData(input_tuples):

    annuity_payout_dict = {}

    ap_page = AnnuityPremium(driver=browser)
    ap_page.go()

    for input_tuple in input_tuples:
        ap_page.income_start(input_tuple.Income_Start)
        ap_page.premium(input_tuple.Premium)
        ap_page.age(input_tuple.Age)
        ap_page.gender(input_tuple.Gender)
        ap_page.state(input_tuple.State)
        ap_page.submit()
        annuity_payout_dict[input_tuple] = ap_page.output(2)
        ap_page.back()

    return annuity_payout_dict

annuity_payout_dict = getAnnuityData(inputs_list_tuple)

with open('annuity.csv','w') as f:
    w = csv.writer(f)
    w.writerow(("Premium","Income_Start","Age","Gender","State","Monthly_Income"))
    w.writerows([(input_tuple.Premium,input_tuple.Income_Start,input_tuple.Age,input_tuple.Gender,input_tuple.State,annuity_payout_dict[input_tuple]) for input_tuple in inputs_list_tuple])


