from selenium import webdriver
from time import sleep
import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



url="https://newerp.kluniversity.in/"

username='2100080026'
password=''


from selenium import webdriver

from selenium.webdriver.chrome.service import Service

# opts=Options()
# opts.add_experimental_option('detach',True)
# driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=opts)

from selenium.webdriver.chrome.service import Service

service = Service(executable_path=r'C:\Users\Dell\Downloads\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get(url)
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//*[@id="mobile_bg"]/div[1]/div[1]/div/div/div/a[1]/span').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@id="loginform-username"]').send_keys(username)
driver.find_element(By.XPATH,'//*[@id="loginform-password"]').send_keys(password)
sleep(15)
driver.find_element(By.XPATH,'//*[@id="login-form"]/div[7]/button').click()
sleep(3)
driver.find_element(By.XPATH,'//*[@id="mainlayout_sidenav"]/div/div/ul/li[5]/a').click()
driver.find_element(By.XPATH,'//*[@id="mainlayout_sidenav"]/div/div/ul/li[5]/ul/li[4]/a').click()
driver.find_element(By.XPATH,'//*[@id="dynamicmodel-academicyear"]').click()
driver.find_element(By.XPATH,'//*[@id="dynamicmodel-academicyear"]/option[3]').click()
driver.find_element(By.XPATH,'//*[@id="dynamicmodel-semester"]').click()
driver.find_element(By.XPATH,'//*[@id="dynamicmodel-semester"]/option[3]').click()
driver.find_element(By.XPATH,'//*[@id="w0"]/div/div[3]/button[1]').click()
sleep(2)
rows=int(driver.find_element(By.CSS_SELECTOR,'#w0 > div > b').get_attribute("innerHTML"))
subjects=dict()
subpath1='//*[@id="w0"]/table/tbody/tr['
subpath2=']/td[5]'
linkspath1='//*[@id="w0"]/table/tbody/tr['
linkspath2=']/td[6]'
altpathforlink1='#w0 > table > tbody > tr:nth-child('
altpathforlink2=') > td:nth-child(6) > a:nth-child('

for i in range(1,rows+1):
    if(True):
        subpath=subpath1+str(i)+subpath2
        sleep(0.2)
        subname=driver.find_element(By.XPATH,subpath).text
        subjects[subname]=[0,0]
        j=1
        while(True):
            try:
               
                linkpath=linkspath1+str(i)+linkspath2+"/a["+str(j)+"]"
                try:
                    driver.find_element(By.XPATH,linkpath).click()
                except:
                    # print("error in in while try")
                    altpathforlink=altpathforlink1+str(i)+altpathforlink2+str(j*2)+')'
                    driver.get(driver.find_element(By.CSS_SELECTOR,altpathforlink).get_property("href"))
                sleep(0.2)
                for t in range(1,30):
                    try:
                        looppath='//*[@id="w0"]/table/thead/tr/th['+str(t)+']'
                        text=driver.find_element(By.XPATH,looppath).text
                        if(text=='Weight'):
                            weight=t  
                        if(text=='Weighted Marks'):
                            mweight=t
                            break  
                    except:
                        # print("error in for loop try")
                        pass
                weightpath='//*[@id="w0"]/table/tbody/tr/td['+str(weight)+']'
                gainpath='//*[@id="w0"]/table/tbody/tr/td['+str(mweight)+']'
                try:
                    weightmarks=float(driver.find_element(By.XPATH,weightpath).text)
                    gainmarks=float(driver.find_element(By.XPATH,gainpath).text)
                except:
                    # print("error in adding")
                    weightmarks,gainmarks=0,0
                subjects[subname][0]+=gainmarks
                subjects[subname][1]+=weightmarks
                # print(weightmarks,gainmarks)
                driver.back()
                sleep(0.1)
                driver.back()
                sleep(0.1)
                driver.find_element(By.XPATH,'//*[@id="w0"]/div/div[3]/button[1]').click()
                sleep(0.2)
                j+=1
            except:
                # print("error in while try")
                break    



print()
print(subjects)



driver.quit()

