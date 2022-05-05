import time  # 시간 측정 위해 time 모듈 추가
import random  # 리스트를 무작위로 섞기위해 random 모듈 추가
from typing import MutableSequence

# 삽입 정렬
def insertion_sort(ls):
    for i in range(1, len(ls)):
        j = i - 1
        key = ls[i]
        while ls[j] > key and j >= 0:
            ls[j+1] = ls[j]
            j = j -1
        ls[j+1] = key
    return ls

time1 = []
time_t = 0

ls = []  # 빈 리스트 생성
for i in range(5, 21):
    for j in range(100):
        j += 1
        n = 2 ** i
        ls.append(n)
        random.shuffle(ls)  # 정렬하기 전 무작위로 섞기

        start = time.time()
        insertion_sort(ls)  # 삽입 정렬 실행 시간
        insetion_time = (time.time() - start) * 1000

        time_t = time_t + insetion_time

    time1.append(time_t / 100)

print(time1)
print(len(time1))


