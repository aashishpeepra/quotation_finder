# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 22:07:06 2018

@author: hp
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
##----------------------------------------------------- 
print("QUOTATION ---------------BY AASHISH")
input("PRESS ANY KEY TO CONTINUE")
driver=webdriver.Chrome()
driver.get("https://www.brainyquote.com/")
time.sleep(8)
i=2
def type_checker(s):
    try:
        rr=int(input(s))
        return rr
    except:
        print("INVALID INPUT-- TRY INTEGERS")
        type_checker(s)
##-------------------------------------------------------------------------
##this shows the attributes !! WARNING: FEW LINKS DOESN;T WORK !!
def show_case():
    try:
        row1=driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/div[2]/div/div[1]')
        print(row1.text)
    except:
        print("ERROR IN FINDING ROWS IN PAGE")
    
def printing():    
    choice_r=input("ENTER YOUR CHOICE")
    try:
        op=driver.find_element_by_link_text('%s'%(choice_r))
        op.click()
    except:
        print("WRONG CHOICE!! SPELL CORRECTLY")
        print("RECALLING")
        printing()

##-------------------------------------------------------------------------
def quote_inrange(i):  ## prints quoatation
    if i<32:
        box1=driver.find_element_by_xpath('//div[@id="qpos_1_%d"]'%(i))
        print(box1.text)
    else:
        print("LIMIT REACHED")
    print("-----------------------------------------------")
##----------------------------------------------------------------------------
## actual execution works here
def quote_time(i):
    choice=0
    while choice!=3:
        choice=type_checker("Press 1 to see  quotation || press 2 to go back to choice menu || press 3 to exit")
        if choice==1:
            if i!=11 and i!=18 and i!=25 and i!=4:
                quote_inrange(i)
                if i==35:
                    break
            i+=1
        elif choice==2:
            driver.back()
            show_case()
            printing()
            quote_time(2)
        elif choice==3:
            print("PLEASE COPY YOUR QUOTATION:-")
            print("--------------------------------")
            print("THANKS FOR USING QUOTATION-SEARCHER BY AASHISH")
            break
        else:
            print("WRONG INPUT ")
            print("RECALLING")
            quote_time(2)
##------------------------------------------------------------------------------------
show_case()
printing()
quote_time(2)
