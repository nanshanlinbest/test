import time

def focus_timer(minutes):
  seconds = minutes * 60
  while seconds > 0:
    print("Focus on your task for the next", minutes, "minutes!")
    time.sleep(60)
    seconds -= 60
    minutes -= 1
  print("Good job! You have completed your focused work session.")

# 使用方法：
# 调用 focus_timer() 函数并传入您想要专注的分钟数作为参数
focus_timer(25)
