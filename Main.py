from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path

source1 = "https://www.flipkart.com/redmi-note-12-lunar-black-64-gb/p/itm6756d6e7a86be?pid=MOBGNYHZJGGE3ZHM&lid=LSTMOBGNYHZJGGE3ZHMWSTXBO&marketplace=FLIPKART&cmpid=content_mobile_20026631677_u_8965229628_gmc_pla&tgi=sem,1,G,11214002,u,,,656126793764,,,,c,,,,,,,&gclid=CjwKCAjwpuajBhBpEiwA_ZtfhaN854a7dzATpGIQr6z2b6678MD-M4LZlFgf3pJgGTUI4JuYOMO2lRoCELcQAvD_BwE"
source2 = "https://www.amazon.in/Redmi-AMOLED-Snapdragon%C2%AE-Triple-Camera/dp/B0BQ3MMPX6/ref=asc_df_B0BQ3MMPX6/?tag=googleshopdes-21&linkCode=df0&hvadid=619923075326&hvpos=&hvnetw=g&hvrand=5450066762833772083&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9302026&hvtargid=pla-1943758498993&psc=1"
source3 = "https://www.croma.com/redmi-note-12-5g-6gb-ram-128gb-matte-black-/p/267289"

# create a webdriver object for chrome-option and configure
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
# wd = webdriver.Chrome(r'C:\Users\ec\Downloads\chromedriver.exe',options=CO)
wd = webdriver.Chrome('chromedriver.exe', options=CO)
print("********* \n")
print("                     Starting Program, Please wait ..... \n")


print("Connecting to Flipkart")
wd.get(source1)
wd.implicitly_wait(wait_imp)
f_price = wd.find_element("xpath", "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]")
pr_name = wd.find_element("xpath", "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span")
product = pr_name.text
r_price = f_price.text
# print(r_price[1:])
print(" ---> Successfully retrieved the price from Flipkart \n")
time.sleep(2)

print("Connecting to Amazon")
wd.get(source2)
wd.implicitly_wait(wait_imp)
a_price = wd.find_element("xpath", "/html/body/div[2]/div[2]/div[5]/div[3]/div[4]/div[11]/div[3]/div[1]/span[2]/span[2]/span[2]")
raw_p = a_price.text
# print(raw_p[2:8])
print(" ---> Successfully retrieved the price from Amazon \n")
time.sleep(2)

print("Connecting to Croma")
wd.get(source3)
wd.implicitly_wait(wait_imp)
c_price = wd.find_element("xpath", "/html/body/main/div[3]/div[1]/div[2]/div[1]/div/div/div/div[3]/div/ul/li[1]/div[2]/div[1]/div/span")
raw_c = c_price.text
# print(raw_c[1:7])
print(" ---> Successfully retrieved the price from Croma\n")
time.sleep(2)

# Final display
print("#------------------------------------------------------------------------#")
print("Price for [{}] on all websites, Prices are in INR \n".format(product))
print("Price available at Flipkart is: " + r_price[1:])
print("  Price available at Amazon is: " + raw_p[2:8])
print("   Price available at Croma is: " + raw_c[1:7])