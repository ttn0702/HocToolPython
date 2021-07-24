from high_order_framework_requests_python import utils_chrome_selenium,utils_class
import time

title = 'Gia thế Nobita'
ndung= '''Căn nhà mà Nobita sống có từ thời ông bà với chỉ hai tầng và một cái vườn nhỏ. Trong gia đình Nobi, bố của Nobita là một nhân viên văn phòng bình thường, hàng ngày đi làm bằng tàu điện ngầm. Còn mẹ của Nobita ở nhà làm công việc nội trợ và thường hỏi con câu hỏi kinh điển: "Đã làm bài tập về nhà chưa mà đi chơi?"
Ông Nobisuke, bố của Nobita có sở thích câu cá, hút thuốc và đánh Golf, dù vậy cả bố mẹ ít khi nào đáp ứng sở thích của Nobita như mua đồ chơi, đi du lịch... Ngay cả sở thích xem tivi của Nobita cũng gặp nhiều trắc trở khi chiếc tivi liên tục dở chứng nhưng ông Nobisuke nhất quyết không sắm sửa cái mới vì... tốn tiền.'''

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

# Click Post
driver1.find_elements_by_css_selector('.wp-menu-name')[1].click()

# Click Add new
driver1.find_elements_by_css_selector('a[href="http://oldwp.nghiahsgs.com/wp-admin/post-new.php"]')[2].click()

# Nhap title
driver1.find_element_by_css_selector('input[name="post_title"]').send_keys(title)
time.sleep(2)
# Nhap noi dung
driver1.find_element_by_css_selector('button[id="content-html"]').click()
# Nhap noi dung
driver1.find_element_by_css_selector('textarea[class="wp-editor-area"]').send_keys(ndung)
time.sleep(2)

# Click chen anh
driver1.find_element_by_css_selector('button[id="insert-media-button"]').click()
time.sleep(2)

# Upload File
driver1.find_element_by_css_selector('input[type="file"]').send_keys('C:\\Users\\asus\\Downloads\\image\\nobita.jpg')
time.sleep(2)   # Nghỉ 2s để kịp Upload ảnh lên thì mới tìm được attrubute src của anh vừa up

# Nhap 
driver1.find_element_by_css_selector('button[class="button media-button button-primary button-large media-button-insert"]').click()
time.sleep(2)

# Click publish
driver1.find_element_by_css_selector('input[name="publish"]').click()
time.sleep(2)

driver1.quit()