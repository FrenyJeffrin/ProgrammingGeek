import time
import threading
def myfunc(names):
    print(f'myfunc started {names}')
    time.sleep(10)
    print('myfunc ended')

if __name__ =='__main__':
    print('main started')
    t=threading.Thread(target=myfunc, args=['real python'], daemon=True)
    t.start()
    print('main ended')
