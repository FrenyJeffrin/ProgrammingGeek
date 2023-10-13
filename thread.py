import time
import threading 
def myfunc(name):
    print(f'my func started with {name}')
    time.sleep(10)
    print('myfunc ended')

if __name__ == '__main__':
    print('main started')
    t=threading.Thread(target=myfunc, args=['real python'])
    t.start()
    print('main ended')
