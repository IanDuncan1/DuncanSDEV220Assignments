import multiprocessing as mp
import random as rand
import time
from datetime import datetime
num = rand.randint(0,1)


today = open ('today.txt')
today_string = today.read()

print(datetime.strptime(today_string, '%m/%d/%Y'))

def f():
    time.sleep(num)
    print(time.time())
if __name__=='__main__':
    for n in range(3):
        p = mp.Process(target=f)
    p.start()
