import time
import concurrent.futures
def myfunc(names):
    print(f'myfunc started {names}')
    time.sleep(10)
    print(f'myfunc ended with {name}')
if __name__ =="__main__":
    print("main begins")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:
        e.map(myfunc,['foo','bar','baz'])
    print("main ended")