# import sys

# # sys.exit()

# print(sys.argv)

# print(sys.path)

# pickle
import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)    # 파일 쓰기
f.close()

import pickle
f = open("test.txt", 'rb')
data = pickle.load(f)   # 파일 읽기
print(data)

# import os
# print(os.environ)

import time
# print(time.time())

# start = time.time() # 시작 시각 기록
# for i in range(100000):
#     print(i, end=' ')

# end = time.time() # 종료 시각 기록
# print(end - start)

print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print(time.strftime)
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d', time.localtime(time.time())))

# import time
# for i in range(10):
#     print(i)
#     time.sleep(0.5)

# import calendar
# print(calendar.calendar(2021))
print('=' * 80)

import random
# # random.shuffle(data)
# print(random.random) # 0~1사이 난수 출력
# print(random.randint(1,45)) #1~10사이 정수 출력

# def random_pop(data):
#     number = random.randint(0, len(data)-1)
#     return data.pop(number)

# data = [1,2,3,4,5]
# while data:
#     print(random_pop(data))
#     print(random.shuffle(data))
# print('=' * 40)

# data = [1,2,3,4,5]
# print(random.choice(data))
# print(random.choices(data))

print('=' * 50)
# 음식 메뉴 추천 프로그램
# menu = ['백반','짜장면','분식','떡볶이','햄버거']
# print(random.choice(menu))
print('=' * 50)
category = {
    '한식': ['백반','뼈해장국','고등어구이'],
    '일식': ['초밥','우동','가라아게'],
    '중식': ['짜장면','짬뽕','탕수육'],
    '간편식': ['햄버거','김밥','샌드위치'],
    '특식': ['삼계탕','피자','보쌈'],
}

menu = input('한식/일식/중식/간편식/특식')

koreafood = random.choice(category['한식'])
japanfood = random.choice(category['일식'])
chinafood = random.choice(category['중식'])
fastfood = random.choice(category['간편식'])
specialfood = random.choice(category['특식'])
print(koreafood)
print(japanfood)
print(chinafood)
print(fastfood)
print(specialfood)

food = random.choice(category.get(menu,['굶으세요','뷔페']))
print(food)
print('=' * 50)


import time
import threading  # 스레드를 생성하기 위해서는 threading 모듈이 필요하다.

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)  # 스레드를 생성한다.
    threads.append(t) 

for t in threads:
    t.start()  # 스레드를 실행한다.

for t in threads:
    t.join()  # join으로 스레드가 종료될때까지 기다린다.
print("End")
# 컴퓨터에서 동작하고 있는 프로그램을 프로세스(Process)라고 한다. 
# 보통 1개의 프로세스는 한 가지 일만 하지만 스레드(Thread)를 사용하면
#  한 프로세스 안에서 2가지 또는 그 이상의 일을 동시에 수행할 수 있다.

