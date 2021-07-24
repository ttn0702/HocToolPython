from high_order_framework_requests_python import utils_chrome_selenium,utils_class
import time 
import os

list_image = os.listdir('C:\\Users\\asus\\Downloads\\image')
list_link_image = []

os = 'windows'
isLoadImage =True
isHeadless = False
folder_save='' 
proxy=''
chrome_auto1 = utils_chrome_selenium.Chrome_auto(os,isLoadImage,isHeadless,folder_save, proxy)

driver1 = chrome_auto1.initDriver()
driver1.get('http://oldwp.nghiahsgs.com/wp-admin/')

# Nhap user
driver1.find_element_by_css_selector('input[type="text"]').send_keys('nghiahsgs')

# Nhap password
driver1.find_element_by_css_selector('input[type="password"]').send_keys('261997')

# Click vao login
driver1.find_element_by_css_selector('input[type="submit"]').click()

# Click Media
driver1.find_elements_by_css_selector('.wp-menu-name')[2].click()

# Click Add new
driver1.find_elements_by_css_selector('a[href="http://oldwp.nghiahsgs.com/wp-admin/media-new.php"]')[1].click()

for i in list_image:
    path_image = f'C:\\Users\\asus\\Downloads\\image\\{i}'
    # # Upload File
    driver1.find_element_by_css_selector('input[type="file"]').send_keys(path_image)
    time.sleep(2)   # Nghỉ 2s để kịp Upload ảnh lên thì mới tìm được attrubute src của anh vừa up

for i in range(0,len(list_image)):
    # Lay link anh vua upload
    link = driver1.find_elements_by_css_selector('div[class="centered"] img')[i].get_attribute("src")
    list_link_image.append(link)
    time.sleep(2)

utils_class.File_Interact('link.txt').write_file_from_list(list_link_image)
driver1.quit()