import time

millichabis = 0
chabist = 0
chabiscount = 0
chabis = (time.time() / 8640)
print(time.time())
print("seconds since epoch")
print(chabis)
print("chabis since epoch")
while True:
  time.sleep(0.8640)
  chabiscount = chabiscount+1



  print(chabiscount, "decimillichabis")
  if millichabis == 1000:
    millichabis = 0
    chabist = chabist+1
    print(chabist, "chabis and")
