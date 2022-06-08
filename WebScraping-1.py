import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
Browser=webdriver.Chrome("C:/Users/91920/Desktop/Module3/Projects/P127/chromedriver.exe")
Browser.get(START_URL)
time.sleep(10)

def Scrape():
    headers=["Name","Distance","Mass","Radius"]
    stars_data=[]
    for i in range(0,98):
        soup=BeautifulSoup(Browser.page_source,"html.parser")
        for th_tag in soup.find_all("th",attrs={"class","listofstars"}):
            tr_tags=th_tag.find_all("tr")
            empty_list=[]
            for index,tr_tag in enumerate(tr_tags):
                if index==0:
                    empty_list.append(tr_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        empty_list.append(tr_tag.contents[0])    
                    except :
                        empty_list.append("")
            stars_data.append(empty_list)            
        Browser.find_element_by_xpath('https://en.wikipedia.org/w/resources/src/jquery.tablesorter.styles/images/sort_up.svg?2ff5c')    
    with open("Scraping.csv","w")as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)
Scrape()        