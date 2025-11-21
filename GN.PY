#猜數字遊戲
import random
def guess_number_game():
# 隨機產生一個 1 到 100 的整數答案。
    answer = random.randint(1, 100)
    attempts = 0
# 玩家每次輸入猜測數字，程式提示「大了」或「小了」  
    while True:
        try:
            guess = int(input("請猜一個 1 到 100 之間的數字: "))
            if guess < 1 or guess > 100:
                print("請輸入 1 到 100 之間的數字！")
                continue
            attempts += 1
            if guess < answer:
                print("小了")
            elif guess > answer:
                print("大了")
#答對時顯示「恭喜通過！」並結束遊戲 
            else:
                print(f"恭喜通過！你總共猜了 {attempts} 次。")
#程式需記錄猜測次數，顯示學員的持續進步 
                break
        except ValueError:
            print("請輸入有效的數字！")
guess_number_game()


 
