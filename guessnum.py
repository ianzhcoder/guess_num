#終極密碼遊戲
import random

start = int(input("請輸入隨機範圍開始值:"))
end = int(input("請輸入隨機範圍結束值:"))
r = random.randint(start, end)
#n = 1
#t = 100
#r = random.randint(1, 100)

#加入猜了幾次
count = 0
while True:
    num = int(input("請猜一個數字:"))
    #count += 1
    count =count + 1
    if num == r:
        print ("你猜對了!")
        break
    elif num < r :
        start = num
        print ("該數字介於", start, "到", end, "之間")
    #elif num > r :
    else : 
        end = num
        print ("該數字介於", start, "到", end, "之間")
    print ("目前猜了", count, "次!")
print ("總共猜了", count, "次!")

#