#終極密碼遊戲
import random

n = 1
t = 100
r = random.randint(1, 100)
while True:
    num = int(input("請猜一個數字:"))
    if num == r:
        print ("你猜對了!")
        break
    elif num < r :
        n = num
        print ("該數字介於", n, "到", t, "之間")
    else :
        t = num
        print ("該數字介於", n, "到", t, "之間")
