from utils import *
import threading

for i in range(1,65):
    t = threading.Thread(target=crawl_data, args=(i,))
    t.start()
    
t.join()
print('Done!')
