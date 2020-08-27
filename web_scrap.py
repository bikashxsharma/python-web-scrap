import csv
import sys
import fileinput
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import *
import tkinter as tk
from tkinter import simpledialog
from tkmacosx import Button

# actual function to get data based on argument passed


def get_csv_data_scrap(start_date_data, end_date_data, city_code):
    driver = webdriver.Chrome()

    driver.get("https://virre.prh.fi/novus/publishedEntriesSearch?execution=e2s1")

    start_date = driver.find_element_by_id("startDate")
    start_date.send_keys(start_date_data)
    end_date = driver.find_element_by_id("endDate")
    end_date.send_keys(end_date_data)

    registration_typeCode = driver.find_element_by_id("registrationTypeCode")
    selectType = Select(registration_typeCode)
    selectType.select_by_value("kltu.U")

    location_type = driver.find_element_by_id("domicileCode")
    select_city = Select(location_type)
    select_city.select_by_value(city_code)

    search_button = driver.find_element_by_id('_eventId_search')
    search_button.send_keys(Keys.ENTER)

    # get total number of rows in the first page
    rows = driver.find_elements_by_xpath(
        "//*[@id='foundPublishedEntries']/tbody/tr")

    # write file in csv

    def file_write_csv(c_name, c_email):
        with open('./companydata.csv', mode='a') as csv_file:
            fieldnames = ['company_name', 'company_email']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'company_name': c_name,
                             'company_email': c_email})

    # function to click each page, get data and go back

    def get_company_name_email(i):
        company = driver.find_element_by_xpath(
            "//*[@id= 'foundPublishedEntries']/tbody/tr[{}]/td[1]/a".format(i))
        company.send_keys(Keys.ENTER)
        delay = 5
        company_name = driver.find_element_by_xpath(
            "//*[@id='main-content-wrapper']/section/div/div[1]/div/div/table/tbody/tr[1]/td[2]").text
        email_xpath = driver.find_elements_by_xpath(
            "//*[contains(text(), 'Sähköposti')]")
        if(email_xpath):
            company_email = driver.find_element_by_xpath(
                "//*[contains(text(), 'Sähköposti')]/following::td").text
            file_write_csv(company_name, company_email)
        else:
            print("email does not exist")
        driver.back()

    i = 1
    while i < len(rows):
        get_company_name_email(i)
        i += 1

    driver.close()

    # replacing (a) with @
    with fileinput.FileInput('./companydata.csv', inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('(a)', '@'), end='')


root = Tk()
root.geometry('500x500')
root.title("Web Scarp V1")

startD = StringVar()
endD = StringVar()
cityD = StringVar()


def main_program():
    start_d = startD.get()
    end_d = endD.get()
    city_d = c.get()
    final_city_code = None
    if(city_d == "Helsinki"):
        final_city_code = "091"
    elif (city_d == "Vantaa"):
        final_city_code = "092"
    elif(city_d == "Espoo"):
        final_city_code = "049"
    elif(city_d == "Turku"):
        final_city_code = "853"
    elif(city_d == "Tampere"):
        final_city_code = "837"
    get_csv_data_scrap(start_d, end_d, final_city_code)


label_0 = Label(root, text="Web Scrap v1", anchor="center",
                width=20, font=("bold", 20))
label_0.place(x=120, y=53)


start_date = Label(root, text="Start Date", anchor='e',
                   width=20, font=("bold", 10))
start_date.place(x=40, y=130)

start_date_input = Entry(root, textvar=startD)
start_date_input.place(x=200, y=130)

end_date = Label(root, text="End Date", anchor='e',
                 width=20, font=("bold", 10))
end_date.place(x=40, y=180)

end_date_input = Entry(root, textvar=endD)
end_date_input.place(x=200, y=180)


city = Label(root, text="City", width=20, anchor='e', font=("bold", 10))
city.place(x=40, y=230)

city_list = ['Helsinki', 'Vantaa', 'Espoo', "Turku", "Tampere"]
c = StringVar()
droplist = OptionMenu(root, c, *city_list)
droplist.config(width=18)
c.set('Select city')
droplist.place(x=200, y=230)


Button(root, text='Make CSV', width=340, height=30, bg='#42f5bf',
       fg='black', borderless=1, command=main_program).place(x=100, y=280)

root.mainloop()
