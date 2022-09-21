from datetime import datetime
print(datetime.now())

# 날짜 구하기
dday = datetime(2023,4,5)
now = datetime.now()
date = dday - now
print(date.days)


#시간 구하기
sleeptime = datetime(2023,1,1,22,0,0)
waketime = datetime(2023,1,2,7,0,0)
result = waketime - sleeptime
print(result)
sec=result.seconds
print(sec) # 초로 환산
hour = sec /(60*60)
print(hour) # 시간으로 환산
print("I will be sleeping for ",str(hour),"hours on next January 1.")