import time
import script

def smth():
    cnt = 0
    while True:
        if cnt <= 202:
            cnt += 1
            script.casino = True

        else:
            script.casino = False
            cnt = 0
        print(cnt)
        time.sleep(5)



smth()

