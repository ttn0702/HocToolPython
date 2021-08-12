import threading
from utils_db import *
from utils import *
from datetime import datetime

class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name=name
    
    # cac tac vu trong thread se chay o day
    def run(self):
        print('Thread: ', self.name)
        # cong viec cua 1 thread can phai chay
        while True:
            if  self.name == "thread1":
                L_jobs = Score.select().where(Score.id%5==0)
            if  self.name == "thread2":
                L_jobs = Score.select().where(Score.id%5==1)
            if  self.name == "thread3":
                L_jobs = Score.select().where(Score.id%5==2)
            if  self.name == "thread4":
                L_jobs = Score.select().where(Score.id%5==3)
            if  self.name == "thread5":
                L_jobs = Score.select().where(Score.id%5==4)

            if len(L_jobs) == 0:
                break
            else:
                for row in L_jobs:
                    if row.is_run == 0:
                        row.is_run = 1
                        row.save()
                        handle_one_row(row)

thread1 = myThread('thread1')
thread2 = myThread('thread2')
thread3 = myThread('thread3')
thread4 = myThread('thread4')
thread5 = myThread('thread5')

# main thread   
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

print('Doneeeeeeeeeeeeeee!')