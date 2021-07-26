from high_order_framework_requests_python import utils_chrome_selenium
from File_Class import File_Excel
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

list_nguoi_gui = []
list_thoi_gian_gui = []
list_ndung_mail = []

os = 'windows'
isLoadImage =True
isHeadless = False
folder_save=r'C:\Users\asus\AppData\Local\Google\Chrome\User Data\Buoi10' 
proxy=''
chrome_auto1 = utils_chrome_selenium.Chrome_auto(os,isLoadImage,isHeadless,folder_save, proxy)

driver1 = chrome_auto1.initDriver()
driver1.get('https://gmail.com')

# Doi load page
try:
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="aDP"]'))
    WebDriverWait(driver1, 20).until(element_present)
except TimeoutException:
    print('Timed out waiting for page to load')

so_mail_can_doc = 2
for index in range(0,so_mail_can_doc):
    #Mail chua doc : document.querySelectorAll('tr[class="zA zE"]')  || mail da doc : document.querySelectorAll('tr[class="zA yO"]')
    # Click mail chua doc
    element = WebDriverWait(driver1 , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr[class="zA zE"]')))
    element.click()

    # Nguoi gui
    element = WebDriverWait(driver1 , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'td[class="gF gK"]')))
    nguoi_gui = element.get_attribute('innerText')  

    # Thoi gian gui
    element = WebDriverWait(driver1 , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'td[class="gH bAk"]')))
    thoi_gian = element.get_attribute('innerText')  
    try:
        # noi_dung
        element = WebDriverWait(driver1 , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class=""]')))
        noi_dung_mail = driver1.find_elements_by_css_selector('div[class=""]')[1].get_attribute('innerText')
    except:
        # noi_dung
        element = WebDriverWait(driver1 , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class=""]')))
        noi_dung_mail = driver1.find_elements_by_css_selector('div[class=""]')[0].get_attribute('innerText') 
    
    list_nguoi_gui.append(nguoi_gui)
    list_thoi_gian_gui.append(thoi_gian)
    list_ndung_mail.append(noi_dung_mail)

    driver1.get('https://mail.google.com/mail/u/0/#inbox')
    try:
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="aDP"]'))
        WebDriverWait(driver1, 20).until(element_present)
    except TimeoutException:
        print('Timed out waiting for page to load')

driver1.quit()

File_Excel1 = File_Excel('data.xlsx')
sheet_name = 'Sheet1'
File_Excel1.update_cell(sheet_name,'A1','Người gửi')
File_Excel1.update_cell(sheet_name,'B1','Thời gian')
File_Excel1.update_cell(sheet_name,'C1',"Nội dung")

for index in range(0,len(list_ndung_mail)):
    nguoi_Gui = list_nguoi_gui[index]
    thoi_Gian = list_thoi_gian_gui[index]
    noi_dung = list_ndung_mail[index]
    cell_name_nguoi_gui ="A%s"%(index+2)
    cell_name_thoi_gian ="B%s"%(index+2)
    cell_name_noi_dung ="C%s"%(index+2)
    File_Excel1.update_cell(sheet_name,cell_name_nguoi_gui,nguoi_Gui)
    File_Excel1.update_cell(sheet_name,cell_name_thoi_gian,thoi_Gian)
    File_Excel1.update_cell(sheet_name,cell_name_noi_dung,noi_dung)