# solo dm, no likes
# loggea con usuarios, busca hashtags, se va al perfil de cada hashtag (total de 6 por usuario), y les envia dm
from logging import exception
from weakref import ref
from selenium import webdriver
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.utils import download_file



from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager as CM

f = open('accounts.json',)
datas = (json.load(f))




def doesnt_exist(driver, classname):
    try:
        driver.find_element_by_class_name(classname)
    except NoSuchElementException:
        return True
    else:
        return False

def doesnt_existxpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return True
    else:
        return False

with open('usernames.txt', 'r') as f:
    usernames = [line.strip() for line in f]

#with open('messages_rap.txt', 'r') as f:
with open('messages_au_giveaway.txt', 'r') as f:
    messages = [line.strip() for line in f]

with open('messages_au_giveawaylink.txt', 'r') as f:
    messageslink = [line.strip() for line in f]

#with open('tagsrap.txt', 'r') as f:
with open('tagsau.txt', 'r') as f:
    tags = [line.strip() for line in f]



between_messages = 5
refresht = 4

options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options, executable_path=CM().install())


#
def main(data):
    
    browser.get('https://instagram.com')
    
    time.sleep(random.randrange(3,4))
    # inicio de sesion
    

    input_username = browser.find_element_by_name('username')
    input_password = browser.find_element_by_name('password')

    input_username.send_keys(data["username"])
    time.sleep(random.randrange(1,2))
    
    input_password.send_keys(data["password"])
    time.sleep(random.randrange(1,2))

    input_password.send_keys(Keys.ENTER)

    print('Iniciando sesion con ---> ' + data["username"])
    time.sleep(6)

    # ==========================================

    # Fetching posts============================



    browser.get('https://instagram.com/guararmusic/')
    time.sleep(2)
    


        #comprueba si el div exite, true = no inciado sesion        false = si inicio sesion
    if doesnt_existxpath(browser, '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/span'):

        
        tag = random.choice(tags)
        print('Fetching posts for this tag----> ' + tag)
        link = "https://www.instagram.com/explore/tags/" + tag


        browser.get(link)
        time.sleep(4)
        

        try:
            for i in range(1):
                ActionChains(browser).send_keys(Keys.END).perform()
                time.sleep(2)

            row1 = browser.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]')
            row2 = browser.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div[2]/div/div[2]')
        except NoSuchElementException:
            browser.refresh()
            time.sleep(refresht)
            
            for i in range(1):
                ActionChains(browser).send_keys(Keys.END).perform()
                time.sleep(2)

            row1 = browser.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]')
            row2 = browser.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div[2]/div/div[2]')

        r_link1 = row1.find_elements_by_tag_name('a')
        r_link2 = row2.find_elements_by_tag_name('a')
        links = r_link1 + r_link2

        urls = []

        for i in links:
            if i.get_attribute('href') != None:
                urls.append(i.get_attribute('href'))

        # ========================================================

        for url in urls:
            print('Starting on this post---> ' + url)
            
            browser.get(url)
            browser.implicitly_wait(1)
            browser.execute_script("window.scrollTo(0, 0)")
            time.sleep(6)
    
            
            user = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[1]/div/span/a').text
            print("Trabajando con ---->" + user)

            #click messenger btn
            browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
            time.sleep(random.randrange(2,3))

            if doesnt_existxpath(browser, '/html/body/div[6]/div/div/div/div[3]/button[2]'):
                print('not now pasado')
            else:
                #click not now
                browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
                time.sleep(random.randrange(2,3))

            #click new msj
            browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()

            #input para el username a enviar
            browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)

            #clicke el primer perfil
            time.sleep(random.randrange(2,3))
            browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]').find_element_by_tag_name('button').click()

            #click next
            time.sleep(random.randrange(3,4))
            browser.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click()

            #estabelece el textarea
            time.sleep(random.randrange(4,5))
            text_area = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            text_area.send_keys('Hello ' + user + random.choice(messages))
            time.sleep(random.randrange(3,5))
            text_area.send_keys(Keys.ENTER)
            text_area = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            text_area.send_keys(messageslink)
            time.sleep(random.randrange(3,5))
            text_area.send_keys(Keys.ENTER)
            print(f'Message successfully sent to {user}')
                

                
                
                
            
                    
            time.sleep(random.randrange(10,19))
    else:
        print('There was a proble, skipping to next account')
                

            





   # browser.close()

while True:
    for data in datas:
        main(data)

# Sending messages:
# def send_message(users, messages):
def send_message():

    browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
    time.sleep(random.randrange(3,5))
    browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
    time.sleep(random.randrange(1,2))
    browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()
    for user in usernames:
        time.sleep(random.randrange(1,2))
        browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
        time.sleep(random.randrange(2,3))
        browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]').find_element_by_tag_name('button').click()
        time.sleep(random.randrange(3,4))
        browser.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click()
        time.sleep(random.randrange(3,4))
        text_area = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        text_area.send_keys('Hello ' + user + random.choice(messages))
        time.sleep(random.randrange(2,4))
        text_area.send_keys(Keys.ENTER)
        print(f'Message successfully sent to {user}')
        # hasta aqui se envio el msj, ahora vamos a clickear perfil para los likes
        time.sleep(random.randrange(2,4))

        #click perfil link
        browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button').click()
        time.sleep(random.randrange(2,4))

        if doesnt_exist(browser, 'v1Nh3'):
            print('Skiped - no tiene posts')
        else:

            #click primer post
            browser.find_element_by_class_name('v1Nh3').click()

            i = 1
            while i <= 9:
                time.sleep(2)
                #click like
                browser.find_element_by_class_name('fr66n').click()
                time.sleep(1)

                if doesnt_exist(browser, 'l8mY4'):
                    print(f'Skiped - {user} no tiene mas posts')
                    i =+ 10
                else:
                #click next arrow
                    
                    browser.find_element_by_class_name('l8mY4').click()
                    i += 1
            
            time.sleep(between_messages)

            # click x
            browser.find_element_by_xpath('/html/body/div[6]/div[1]').find_element_by_tag_name('button').click()
            time.sleep(random.randrange(3,4))

        # click messenger btn
        browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        time.sleep(random.randrange(3,4))

        # click send message
        browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()
        



