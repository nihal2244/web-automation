
from selenium import webdriver
import math
from PyQt5 import Qt
import sys
from tkinter import *

driver=webdriver.Chrome()

def drivelog():

    usn=e1.get()
    pwd=e2.get()
    
    driver.get("https://christuniversity.in/StudentLogin.html")
    driver.implicitly_wait(40)
    driver.switch_to_default_content()
    driver.switch_to.frame(0)

    a=driver.find_element_by_xpath("//*[@id=\"username\"]")
    b=driver.find_element_by_xpath("//*[@id=\"password\"]")
    a.send_keys(usn)
    b.send_keys(pwd)
    driver.find_element_by_xpath("//*[@id=\"Login\"]").click()

    driver.switch_to_default_content()
    driver.switch_to.frame(0)
    driver.find_element_by_xpath("//*[@id=\"att\"] ").click()
    driver.find_element_by_xpath("//*[@id=\"att\"]/ul/li[1]/a").click()

    p=driver.find_element_by_css_selector(".table > tbody:nth-child(1) > tr:nth-last-child(2) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(3) > div:nth-child(1) > b:nth-child(1)")
    c=driver.find_element_by_css_selector(".table > tbody:nth-child(1) > tr:nth-last-child(2) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > b:nth-child(1)")
    percent=driver.find_element_by_css_selector(".table > tbody:nth-child(1) > tr:nth-last-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(5) > div:nth-child(1) > b:nth-child(1)")
    calculation(p,c,percent)


def calculation(p,c,percent):

    present=float(p.text)
    conduct=float(c.text)
    attend=float(percent.text)/100
    required=float(e3.get())/100
    print(present,conduct,attend,required)

    if(attend>required):

        x=math.ceil((present/required)-conduct)
        back="can bunk"
    elif(attend<required):

        x=math.ceil((conduct*required-present)/(1-required))
        back="to attend"
    else:
        x=0
        back="to attend/bunk"

    app = Qt.QApplication(sys.argv)
    systemtray_icon = Qt.QSystemTrayIcon()
    systemtray_icon.show()
    systemtray_icon.showMessage('Attendance Now : ' + str(attend * 100), str(x) + " classes " + back)
    driver.quit()


master = Tk()
Label(master, text="User Id").grid(row=0)
Label(master, text="password").grid(row=1)
Label(master, text="percentile required").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=drivelog).grid(row=3, column=1, sticky=W, pady=4)

mainloop()