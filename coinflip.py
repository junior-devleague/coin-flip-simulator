import random

def flip(times):
  flipList = []
  for i in range(times):
    result = random.randint(0, 1)
    if (result == 0):
      flipList.append("Heads")
      print("Heads")
    else:
      flipList.append("Tails")
      print("Tails")
  print(str(flipList.count("Heads")) + str(flipList.count("Tails")))

count = input("How many times will you flip?: ")
flip(count)
