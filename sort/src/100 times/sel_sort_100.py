import time  # 시간 측정 위해 time 모듈 추가
import random  # 리스트를 무작위로 섞기위해 random 모듈 추가
from typing import MutableSequence


# 선택 정렬
def sel_sort(a):
    n = len(a)

    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

time1 = []
sel_time_t = 0

ls = []  # 빈 리스트 생성
for i in range(5, 21):
    for j in range(100):
        j += 1
        n = 2 ** i
        ls.append(n)
        random.shuffle(ls)  # 정렬하기 전 무작위로 섞기

        start = time.time()
        sel_sort(ls)  # 선택 정렬 실행 시간
        sel_time = (time.time() - start) * 1000

        sel_time_t = sel_time_t + sel_time

    time1.append(sel_time_t/100)

print(time1)
print(len(time1))